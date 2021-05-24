//lps.c
#include "lps.h"

// finds the LPS of the second string inputed using LCS and reverse strings
char *LPS(char *p2) {

  int i, j, k, temp, mid, longest = 0;
  int n = strlen(p2);
  char *LPS;
  LPS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
  // splits string into all possible combinations to find LCS
  for(i=1; i<n-1; i++) {
    // resets str1 and str2
    char *str1;
    str1 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    char *str2;
    str2 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    k = 0;
    for(j=0; j<i; j++) { // first part of string
      *(str1+j) = *(p2+j);
    }
    for(j=i; j<n; j++){ // second part of string
      *(str2+k) = *(p2+j);
      k++;
    }
    reverse(str2); // uses reverse of second part of string to compute LCS
    temp = strlen(LCS(str1, str2)); // compare lengths of LCS
    if(temp > longest) { // if the longest LCS
      longest = temp;
      LPS = LCS(str1, str2);
    }
    //free(str1);
    //free(str2);
  }

  for(i=0; i<longest; i++) {
    *(LPS+longest+i-1) = *(LPS+longest-1-i);
  }
  return LPS;
}

// computes LCPS by iterating over string and finding LCSs of the strings
char *LCPS(char *p1, char *p2) {

  int i, j, k, p, m, n, temp, longest = 0;
  int n1 = strlen(p1);
  int n2 = strlen(p2);
  //initialize string
  char *LCPS;
  LCPS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

  // iterarate over the first string spliting it into 2
  for(i=1; i<n1-1; i++) {
    char *str1;
    str1 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    char *str2;
    str2 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    k = 0;
    for(m=0; m<i; m++) {
      *(str1+m) = *(p1+m);
    }
    for(m=i; m<n1; m++) {
      *(str2+k) = *(p1+m);
      k++;
    }
    // iterarate over the second string spliting it into 2
    for(j=1; j<n2-1; j++){
      char *str3;
      str3 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
      char *str4;
      str4 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
      p = 0;
      for(n=0; n<i; n++) {
        *(str3+n) = *(p1+n);
      }
      for(n=i; n<n1; n++) {
        *(str4+p) = *(p1+n);
        p++;
      }
      // reverse back half of each string and find LCS of the 4 strings
      reverse(str2);
      reverse(str4);
      temp = strlen(DLCS(str1, str2, str3, str4)); // compare lengths of LCS
      if(temp > longest) { // if the longest LCS
        longest = temp;
        LCPS = DLCS(str1, str2, str3, str4);
      }
    }
  }
  // copy the string reversely as it is the first half of the LCPS
  for(i=0; i<longest; i++) {
    *(LCPS+longest+i-1) = *(LCPS+longest-1-i);
  }
  return LCPS;
}
