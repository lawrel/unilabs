#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

/*TYPEDEFS*/
typedef struct {
      int valid;
      int tag;
      int timestamp;
   } cacheline;
typedef struct {
      cacheline *lines;
   } cacheset;
typedef struct {
	int hitcount;
   	int misscount;
    int setcount; //# of sets 
    int assoc; // number of cachelines per set
    cacheset *data;//the actual cache, a beautiful boy
} cache;
cache Cache;

void LRU(){
	int i; int j; int time = 0;
	int address;
	int setid; 
	for (i=0;i<1000;i++) {
		int H=0; int empty = -1;
		int toevict = 0;
		scanf("%d",&address);
		setid = address%Cache.setcount;
		int oldest = INT_MAX;
		for(j=0;j<Cache.assoc;j++) {
			if (Cache.data[setid].lines[j].tag == address) {
				Cache.hitcount++; H++;
				Cache.data[setid].lines[j].timestamp = time;
				time++;
			}
			else if (Cache.data[setid].lines[j].timestamp<oldest) {
				oldest = Cache.data[setid].lines[j].timestamp;
				toevict = j;
			} else if (empty==-1) {
				empty = j;
			}
		}
			if(H==0){
				Cache.misscount++;
				if (empty!=-1) {
					Cache.data[setid].lines[empty].timestamp = time;
					Cache.data[setid].lines[empty].tag = address;
					Cache.data[setid].lines[empty].valid = 1;
				} else {
					Cache.data[setid].lines[toevict].timestamp = time;
					Cache.data[setid].lines[toevict].tag = address;
					
				}
				time++;
			}
	}
}
void Belady() {
	int input[1000];
	for (int i=0;i<1000;i++) {
		scanf("%d",&input[i]);
	}
	for (int i=0;i<1000;i++) {
		int H=0;int empty = -1;
		int toevict = 0;
		int setid = input[i]%Cache.setcount;
		for(int j=0;j<Cache.assoc;j++) {
			if (Cache.data[setid].lines[j].tag == input[i]) {
				Cache.hitcount++; H++;
			} else if (H==0) {
				int curr; int last = 0;
				for (int k=i;k<1000;k++) {
					if (input[k]==input[j]) {
						curr = k;
						break;
						}							
					}
				if (curr>last) {
					toevict=j;
				}
			}
			else if (empty==-1) {
					empty = j;
			}
		}
		if(H==0){
				Cache.misscount++;
				if (empty!=-1) {
					Cache.data[setid].lines[empty].tag = input[i];
					Cache.data[setid].lines[empty].valid = 1;
				} else {
					Cache.data[setid].lines[toevict].tag = input[i];
					Cache.data[setid].lines[toevict].valid = 1;
				}
			}
	}
}
int main() {
	/*VARIABLES*/
	int alg;
	/*CACHE SETUP*/
	printf("Enter associativity (1, 2, 4):\n");
	scanf("%d",&Cache.assoc);
	printf("\nCache size 256 items\n");
	printf("Cache has associativity of %d\n",Cache.assoc);
	Cache.setcount = 256/Cache.assoc;
	printf("Cache has %d sets\n",Cache.setcount);
	//create correct cache size and init all lines to empty
	Cache.data = malloc(Cache.setcount*sizeof(cacheset));
   	for (int i=0;i<Cache.setcount; i++) {
      Cache.data[i].lines = malloc(sizeof(cacheline)*Cache.assoc);
      for (int j=0;j<Cache.assoc;j++) {
      	Cache.data[i].lines[j].valid = 0;
      }
  	}
  	Cache.hitcount = 0;
  	Cache.misscount = 0;
  	/*ALGORITHM SELECTION AND MEMTRACE*/
	printf("\nChoose either 1) LRU or 2) Belady:\n");
	scanf("%d",&alg);
	if (alg==1) {
		LRU();
		printf("\nStarting Simulation...\n");
		printf("Statistics:\n");
		printf("LRU & Cache Associativity: %d\n",Cache.assoc);
	} else if(alg==2) {
		Belady();
		printf("\nStarting Simulation...\n");
		printf("Statistics:\n");
		printf("Belady & Cache Associativity: %d\n",Cache.assoc);
	} else {
		printf("ERROR: Invalid algorithm selected.");
		return 1;
	}
	int count = (Cache.hitcount+Cache.misscount);
	printf("Cache Accesses: %d\n",count);
	printf("Cache Hits: %d\n",Cache.hitcount);
	printf("Cache Misses: %d\n",Cache.misscount);
	printf("Overall Hit Rate: %.6f\n", (float)Cache.hitcount/(float)count);

	/*FREE CACHE MEMORY*/
	for (int i=0;i<Cache.setcount; i++) {
      free(Cache.data[i].lines); 
  	} free(Cache.data);

	return 0;
}