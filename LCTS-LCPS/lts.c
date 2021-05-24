//lts.c
#include "lts.h"

// computes LTS by iterating over string and finding LCSs of the string
char *LTS(char *p1) {

  int i, j, k, temp, longest = 0;
  int n = strlen(p1);
  char *LTS;
  LTS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

  // splits string into all possible combinations to find LCS
  for(i=1; i<n-1; i++) {
    // resets str1 and str2
    char *str1;
    str1 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    char *str2;
    str2 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
    k = 0;
    for(j=0; j<i; j++) { // first part of string
      *(str1+j) = *(p1+j);
    }
    for(j=i; j<n; j++){ // second part of string
      *(str2+k) = *(p1+j);
      k++;
    }
    temp = strlen(LCS(str1, str2)); // compare lengths of LCS
    if(temp > longest) { // if the longest LCS
      longest = temp;
      LTS = LCS(str1, str2);
    }
  }
  // print string twice as it is repeat
  for(i=0; i<longest; i++) {
    *(LTS+longest+i) = *(LTS+i);
  }
  return LTS;
}


// computes LTS by iterating over string and finding LCSs of the string
char *LCTS(char *p1, char *p2) {

  int i, j, k, p, m, n, temp, longest = 0;
  int n1 = strlen(p1);
  int n2 = strlen(p2);
  //initialize string
  char *LCTS;
  LCTS = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

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
      // compare 2 strings of str2 over every interation of the 2 strings of str1
      temp = strlen(DLCS(str1, str2, str3, str4)); // compare lengths of LCS
      if(temp > longest) { // if the longest LCS
        longest = temp;
        LCTS = DLCS(str1, str2, str3, str4);
      }
    }
  }

  // copy and put the string at the end of current string as it is first have of tandum
  for(i=0; i<longest; i++) {
    *(LCTS+longest+i) = *(LCTS+i);
  }
  return LCTS;
}
