/*****************************************************************************/
/* Assignment 1: 2-D/ Matrix Multiplication **********************************/
/*****************************************************************************/
/*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
int **mm_alloc( int rows, int columns )
{
    /*make an array of pointers to ints(rows),
	fill each with cols number of ints*/
	int i;
	int **arr = (int **)malloc(rows*sizeof(int *));
	for (i=0;i<rows;i++) {
		arr[i] = (int *)malloc(columns*sizeof(int));
	}
    return arr;
}

void mm_free( int **matrix, int rows, int columns )
{
	/*delete each row, then delete top array*/
	int i;
	for (i=0;i<rows;i++) {
		free(matrix[i]);
	}
	free(matrix);
	matrix = NULL; //to prevent any further calls from giving errors
}

void mm_read( int **matrix, int rows, int columns )
{
	//reads in each value and saves in the matrix 
	int r,c,n;
	printf("Please enter the values for the %d x %d matrix:\n"
	,rows,columns);
	for (r=0;r<rows;r++) {
		for (c=0;c<columns;c++) {
			scanf("%d",&n);
			matrix[r][c] = n; 
		}
	}
}

void mm_print( int **matrix, int rows, int columns )
{
	//prints each value of matrix to screen in a grid
	int r,c;
	for (r=0;r<rows;r++) {
		for(c=0;c<columns;c++) {
			//this just gives proper spacing at the end of a line
			if (c==(columns-1)) {
				printf("%d",matrix[r][c]);
			} else {
				printf("%d ",matrix[r][c]);
			}
		}
		printf("\n");
	}
}

void mm_mult( int **m1, int m1_rows, int m1_cols,
              int **m2, int m2_rows, int m2_cols,
              int **results)
{
	//Performs matrix multiplication and saves answer to result matrix
	int r,c,i,sum = 0;
	//r = rows of result matrix, c = cols of result matrix
	// i is the dimension they are multiplied across (m1_cols&m2_rows)
	for (r = 0; r < m1_rows; r++) {
		for (c = 0; c < m2_cols; c++) {
			for (i = 0; i < m2_rows; i++) {
				sum = sum + m1[r][i]*m2[i][c];
			}
			results[r][c] = sum;
			sum = 0;
		}	
	}
}

int main()
{
    /*
     * You must keep this function AS IS.
     * You are not allowed to modify it!
     */
    int **matrix1 = NULL;
    int **matrix2 = NULL;
    int **results_matrix = NULL;

    int m1_rows, m1_columns;
    int m2_rows, m2_columns;

    printf("How many rows are in the first matrix? \n");
    scanf("%d", &m1_rows);
    printf("How many columns are in the first matrix? \n");
    scanf("%d", &m1_columns);

    printf("How many rows are in the second matrix? \n");
    scanf("%d", &m2_rows);
    printf("How many columns are in the second matrix? \n");
    scanf("%d", &m2_columns);

    printf("\n");

    if (m1_columns != m2_rows) {
        printf("Invalid matrix multiplication!\n");
        exit(-1);
    }

    matrix1 = mm_alloc(m1_rows, m1_columns);
    matrix2 = mm_alloc(m2_rows, m2_columns);
	
    results_matrix = mm_alloc(m1_rows, m2_columns);

    mm_read( matrix1, m1_rows, m1_columns );
    mm_read( matrix2, m2_rows, m2_columns );

    printf("\n");

    mm_mult(matrix1, m1_rows, m1_columns, matrix2, m2_rows, m2_columns, results_matrix);

    mm_print( matrix1, m1_rows, m1_columns );
    printf("\n");
    printf("multiplied by\n\n");
    mm_print( matrix2, m2_rows, m2_columns );
    printf("\n");
    printf("is: \n\n");
    mm_print( results_matrix, m1_rows, m2_columns );
    mm_free( matrix1, m1_rows, m1_columns );
    mm_free( matrix2, m2_rows, m2_columns );
    mm_free( results_matrix, m1_rows, m2_columns );

    return 0;
}
