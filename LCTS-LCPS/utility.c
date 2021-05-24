//utility.c
#include "utility.h"

// gets 1 sequence and checks validity
void valid1Seq(char *p1) {
  
  // check for valid input, digits only
  for(int i=0; i<strlen(p1); i++) {
    if(!(isdigit(*(p1+i)))) {
      printf("Error, non-digit character detected! Please try again\n");
      exit(0);
    }
  }
}

// reverses inputed strings
void reverse(char *str) {

  int temp;
  char *end;
  end = str + (strlen(str) - 1);

  // iterarate over string swaping oppisite ended characters until middle
  while(end > str) {
    temp = *str;
    *str = *end;
    *end = temp;
    str++;
    end--;
  }
}

// returns max of 4 inputed integers
int max(int n1, int n2, int n3, int n4) {

  int max = n1;
  if(n2 > max){
    max = n2;
  }
  if(n3 > max){
    max = n3;
  }
  if(n4 > max){
    max = n4;
  }
  return max;
}

// generates 2 random digit strings of desired lengths and prints it out
void generateString(int dooutput, char outputfilename[]) {

  int lenstr1, lenstr2;
  int i;

  // scan string lengths
  printf("Enter the lengths of two sequences: ");
  scanf("%d%d", &lenstr1, &lenstr2);

  char *str1, *str2;
  str1 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
  str2 = (char *) malloc(MAXSIZE * sizeof(char));

  srand(time(NULL));

  // fill in str1 with random int, coverted to char
  for(i = 0; i < lenstr1; i++) {
    str1[i] = (rand() % 10) + '0';//randon int
  }

  // fill in str2 with random int, coverted to char
  for(i = 0; i < lenstr2; i++) {
    str2[i] = (rand() % 10) + '0';//randon int
  }

  // output to file if needed or print
  if(dooutput) {
      FILE *outfile = fopen(outputfilename, "a");
      fprintf(outfile, "%s\n%s\n", str1, str2);
  }
  else {
    printf("%s\n%s\n", str1, str2);
  }

  free(str1);
  free(str2);
  return;
}
