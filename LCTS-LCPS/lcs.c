//lcs.c
#include "lcs.h"

// computes longest common subsequence and returns said sequence
char *LCS(char *seq1, char *seq2) {

  size_t i, j;
  int n1 = strlen(seq1);
  int n2 = strlen(seq2);
  //initialize table and LCS string
  int *table;
  table = (int *) malloc((n1+1) * (n2+1) * sizeof(int));
  char *LCS;
  LCS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

  // filling out table
  for(i=0; i<n1+1; i++) {
    for(j=0; j<n2+1; j++) {
      if(i<1 || j<1) { // priliminary 0's for first row/column
        *(table + (i*n2) + j) = 0;
      }
      else {
        *(table + (i*n2) + j) = *(table + ((i-1)*n2) + j-1);
        if(*(seq1+i-1) == *(seq2+j-1)) { // check if match
          *(table + (i*n2) + j) += 1; // increment match
        }
        else{
          if(*(table + ((i-1)*n2) + j) < *(table + ((i)*n2) + j-1)) { // check up or left is bigger
            *(table + (i*n2) + j) = *(table + ((i)*n2) + j-1);
          }
          else {
            *(table + (i*n2) + j) = *(table + ((i-1)*n2) + j);
          }
        }
      }
    }
  }

  i = strlen(seq1);
  j = strlen(seq2);
  int len = *(table + (i*n2) + j)-1;

  while(i>0 && j>0) {
          // adding the matching digit to LCS string and moving diagonal
          if(*(seq1+i-1) == *(seq2+j-1)) {
              *(LCS+len) = *(seq1+i-1);
              len--; // add digit to last position to get correct order
              i--;
              j--;
          }
          // moving left or up depending on which is bigger
          else if(*(table + ((i-1)*n2) + j) > *(table + ((i)*n2) + j-1)) {
              i--;
          }
          else {
              j--;
          }
      }
  free(table);
  return LCS;
}

// computes longest common subsequence of 4 seq and returns said sequence
char *DLCS(char *seq1, char *seq2, char *seq3, char *seq4) {

  int i, j, k, p;
  int n1 = strlen(seq1);
  int n2 = strlen(seq2);
  int n3 = strlen(seq3);
  int n4 = strlen(seq4);

  //initialize 4-D matrix allocating room for each level
  int ****table;
  table = (int ****) malloc((n1+1) * sizeof(int ***));
  for(i=0; i<n1+1; i++) {
    table[i] = (int ***) malloc((n2+1) * sizeof(int **));
    for(j=0; j<n2+1; j++) {
      table[i][j] = (int **) malloc((n3+1) * sizeof(int **));
      for(k=0; k<n3+1; k++) {
        table[i][j][k] = (int *) malloc((n4+1) * sizeof(int));
      }
    }
  }

  //initialize string
  char *DLCS;
  DLCS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

  // filling out matrix
  for(i=0; i<n1+1; i++) {
    for(j=0; j<n2+1; j++) {
      for(k=0; k<n3+1; k++) {
        for(p=0; p<n4+1; p++) {
          if(i<1 || j<1 || k<1 || p<1) { // priliminary 0's for first row/column
            table[i][j][k][p] = 0;
          }
          else {
            table[i][j][k][p] = table[i-1][j-1][k-1][p-1];
            if(seq1[i-1] == seq2[j-1] && seq1[i-1] == seq3[k-1] && seq1[i-1] == seq4[p-1]) { // check if match
              table[i][j][k][p] += 1; // increment match
            }
            else{
              table[i][j][k][p] = max(table[i-1][j][k][p], table[i][j-1][k][p], table[i][j][k-1][p], table[i][j][k][p-1]);
            }
          }
        }
      }
    }
  }

  i = strlen(seq1);
  j = strlen(seq2);
  k = strlen(seq3);
  p = strlen(seq4);
  int len = 0;


  while(i>0 && j>0 && k>0 && p>0) {
    // adding the matching digit to LCS string and moving diagonal

    if(seq1[i-1] == seq2[j-1] && seq1[i-1] == seq3[k-1] && seq1[i-1] == seq4[p-1]) {
      DLCS[len] = seq1[i-1];
      //printf("%c\n", LCS[len]);
      //printf("hi\n");
      len++; // add digit to last position to get correct order
      i--;
      j--;
      k--;
      p--;
    }
    // check which path yeilds the highest number
    else{
      int biggest = table[i-1][j][k][p];
      if(table[i][j-1][k][p] > biggest) {
        biggest = table[i][j-1][k][p];
      }
      if(table[i][j][k-1][p] > biggest) {
        biggest = table[i][j][k-1][p];
      }
      if(table[i][j][k][p-1] > biggest) {
        biggest = table[i][j][k][p-1];
      }
      // check which path is the largest and take that path
      if(table[i-1][j][k][p] == biggest) {
        i--;
      }
      else if(table[i][j-1][k][p] == biggest) {
        j--;
      }
      else if(table[i][j][k-1][p] == biggest) {
        k--;
      }
      else {
        p--;
      }
    }
  }
  
  free(table);
  return DLCS;
}
