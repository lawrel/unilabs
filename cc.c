#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>
#include <sys/types.h>
#include <string.h>
#include <sys/stat.h>
#include <ctype.h>

/*=====ALL VARIABLES TO BE REFERENCED BY MULT. FUNCTIONS=====*/
#define MAXWORD 128
int size;
char ** cache;
FILE *file;
char* line;
char* next;

unsigned int hash(char *word, int size) {
  /*=======HASH FUNCTION=======*/
  int hash = 0; 
  for (int i=0; *(word+i)!='\0'; i++ ) {
    hash += *(word+i);
  }
  return hash%size;
}

int fail() {
  /*=====FLUSH BUFFER AND FAIL IN ONE CUTE STEP=====*/
  fflush(stderr);
  return EXIT_FAILURE;
}

int main(int argc, char **argv) {
printf("check 1\n");
/*=======SETUP OF STRUCTURES//OPEN FILES//CHECK ARGC=======*/
  if (argc != 3) {
    perror("ERROR: Correct Usage is: ./hw1.out <size of cache> <file to be processed>");
    return fail();
  }
  size = atoi(*(argv+1));
  if(size<1) {
    perror("ERROR: Cache must have size >=1");
    return fail();
  }
  if ((file = fopen(*(argv+2),"r"))==NULL) {
    perror("ERROR: Could not open file provided");
    return fail();
  }
  char **cache = (char**) calloc(size, sizeof(char*));
  if (cache==NULL) {
    perror("ERROR: Failed on calloc for the cache structure");
    return fail();
  }
  char *next = (char*) calloc(MAXWORD,sizeof(char*));
  if (next == NULL) {
    perror("ERROR: Failed on calloc of next line");
    return fail();
  }
  printf("check 2\n");

/*=========PARSING INPUT (moved to parse())=========*/  
 while(fgets(next,MAXWORD,file)!=NULL) {
    char* entry;
    line = strtok(next,"., \n");
    while(line!=NULL) {
      int i=hash(line,size);

/*=====IF HASH INDEX IS UNUSED, CALLOC NEW SPACE=====*/
      if (*(cache+i)==NULL) {
        entry = (char*) calloc(strlen(line)+1,sizeof(char*));
        if (entry==NULL) {
          perror("ERROR: Failed on calloc(), could not allocate space");
          return fail();
        }
        *(cache+i) = entry;
        printf("Word \"%s\" ==> %d (calloc)\n", line, i);
        strcpy(*(cache+i), line);

/*=====IF INDEX IS USED, REALLOC EXISTING SPACE=====*/
      } else {
        entry = (char*) realloc(*(cache+i),(sizeof(char*)*strlen(line)+1));
        if (entry==NULL) {
          perror("ERROR: Failed on realloc(), could not reallocate space");
          return fail();
        }
        *(cache+i) = entry;
        printf("Word \"%s\" ==> %d (realloc)\n", line, i);
        strncpy(*(cache+i), line, strlen(line)*sizeof(char));
      }
    
      line = strtok(NULL, "., \n");
    }
  }

/*=========PRINT CONTENTS AND FREE MEMORY=========*/
  fclose(file);
  for(int i =0; i<size; i++) {
    if (*(cache+i)!=NULL) {
      printf("Cache index %d ==> \"%s\"\n",i,*(cache+i));
      free(*(cache+i));
      *(cache+i) = NULL;
    }
  }
  free(cache);
  free(next);
  free(line);

  /*if we make it all the way here they make an episode of "I Survived" about it*/
  return EXIT_SUCCESS;
}