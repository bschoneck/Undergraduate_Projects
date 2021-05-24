/************************************************************************************************/
/* Submitting student: Bryland Schoneck                                                         */
/* Collaborating classmates: N/A                                                                */
/* Other collaborators: N/A                                                                     */
/* References:                                                                                  */
/* N/A                                                                                          */
/************************************************************************************************/
/* Computing an LCTS and an LCPS for any two given sequences of length up to                    */
/* 10, 000 over the digit alphabet and are able to compute an LCS, an LTS, and                  */
/* an LPS.                                                                                      */
/* Name: a3                                                                                     */
/* Author: Bryland Schoneck                                                                     */
/* December 6, 2019                                                                             */
/************************************************************************************************/
/* Timing for the program:                                                                      */
/*         50         100        200        500        1000       2000      5000      10000     */
/* -c    0m0.007    0m0.007    0m0.008    0m0.014     0m0.022   0m0.0840   0m0.408    0m1.457   */
/* -t    0m0.008    0m0.012    0m0.029    0m0.291     0m2.316   0m18.690   4m58.284  40m35.283  */
/* -p    0m0.008    0m0.012    0m0.030    0m0.287     0m2.240   0m18.943   4m57.321  40m54.322  */
/* -ct   0m18.580   8m5.535      ---        ---         ---       ---        ---        ---     */
/* -cp   0m18.463   8m12.34      ---        ---         ---       ---        ---        ---     */
/*  Some took way too long for realistic testing                                                */
/************************************************************************************************/

//main.c
#include "main.h"

int main(int argc, char * argv[]) {

  char * inputfilename;
  char * outputfilename;
  int dogen = 0;
  int dolcs = 0;
  int dolts = 0;
  int dolps = 0;
  int dolcts = 0;
  int dolcps = 0;
  int doinput = 0;
  int dooutput = 0;
  char * vaildinputs[] = {"-g", "-c", "-t", "-p", "-ct", "-cp", "-i", "-o"};

  // determine which inputs/commands are used
  for(int i = 1; i < argc; i++) {
    if(!(strcmp(argv[i], vaildinputs[0]))) {
      dogen = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[1]))){
      dolcs = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[2]))){
      dolts = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[3]))){
      dolps = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[4]))){
      dolcts = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[5]))){
      dolcps = 1;
    }
    else if(!(strcmp(argv[i], vaildinputs[6]))){
      doinput = 1;
      i += 1;
      inputfilename = argv[i];
    }
    else if(!(strcmp(argv[i], vaildinputs[7]))){
      dooutput = 1;
      i += 1;
      outputfilename = argv[i];
    }
    else {
      printf("\
        Invalid option entered, valid options include:\n\
        -g: to generate an instance consisting of two sequences over the digit alphabet\n\
        -c: to compute an LCS for the two input sequences\n\
        -t: to compute an LTS for the input sequence\n\
        -p: to compute an LPS for the input sequence\n\
        -ct: to compute an LCTS for the two input sequences\n\
        -cp: to compute an LCPS for the two input sequences\n\
        -i inputfilename: to read in sequence(s) from file \"inputfilename\"\n\
        -o outputfilename: to write all the results into the file \"outputfilename\"\n\
      ");
      return 0;
    }
  }

  //initialize seqence pointers
  char *p1, *p2; // pointers
  p1 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1
  p2 = (char *) malloc(MAXSIZE * sizeof(char)); // allocate memory for string sizeof(char) = 1

  //if -g is used
  if(dogen) {
    generateString(dooutput, outputfilename);
    return 0;
  }
  //if a outputfile is inputed
  if(dooutput) {
    outfile = fopen(outputfilename, "a");
  }

  //if we need 2 sequences
  if(dolcs || dolcts || dolcps) {
    if(!(doinput)) {
      printf("Enter the first sequence: ");
      scanf("%s", p1);
      valid1Seq(p1);
      printf("Enter the second sequence: ");
      scanf("%s", p2);
      valid1Seq(p2);
    }
    else {
      infile = fopen(inputfilename, "r");
      fscanf(infile, "%s\n%s", p1, p2);
    }
    if(dolcs) {
      char *lcs = LCS(p1, p2);
      if(dooutput) {
        fprintf(outfile, "# an LCS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcs), lcs);
      }
      else {
        printf("# an LCS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcs), lcs);
      }
    }
    if(dolcts) {
      char *lcts = LCTS(p1, p2);
      if(dooutput) {
        fprintf(outfile, "# an LCTS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcts), lcts);
      }
      else {
        printf("# an LCTS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcts), lcts);
      }
    }
    if(dolcps) {
      char *lcps = LCPS(p1, p2);
      if(dooutput) {
        fprintf(outfile, "# an LCPS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcps), lcps);
      }
      else {
        printf("# an LCPS (length = %lu) for the 2 sequences is:\n%s\n", strlen(lcps), lcps);
      }
    }
    if(dolts) {
      char *lts = LTS(p1);
      if(dooutput) {
        fprintf(outfile, "# an LTS (length = %lu) for the sequence is:\n%s\n", strlen(lts), lts);
      }
      else {
        printf("# an LTS (length = %lu) for the sequence is:\n%s\n", strlen(lts), lts);
      }
    }
    if(dolps) {
      char *lps = LPS(p1);
      if(dooutput) {
        fprintf(outfile, "# an LPS (length = %lu) for the sequence is:\n%s\n", strlen(lps), lps);
      }
      else {
        printf("# an LPS (length = %lu) for the sequence is:\n%s\n", strlen(lps), lps);
      }
    }
  }

  //if we only need 1 sequence
  else {
    if(!(doinput)) {
      printf("Enter the sequence:");
      scanf("%s", p1);
      valid1Seq(p1);
    }
    else{
      infile = fopen(inputfilename, "r");
      fscanf(infile, "%s", p1);
    }
    if(dolts) {
      char *lts = LTS(p1);
      if(dooutput) {
        fprintf(outfile, "# an LTS (length = %lu) for the sequence is:\n%s\n", strlen(lts), lts);
      }
      else {
        printf("# an LTS (length = %lu) for the sequence is:\n%s\n", strlen(lts), lts);
      }
    }
    if(dolps) {
      char *lps = LPS(p1);
      if(dooutput) {
        fprintf(outfile, "# an LPS (length = %lu) for the sequence is:\n%s\n", strlen(lps), lps);
      }
      else {
        printf("# an LPS (length = %lu) for the sequence is:\n%s\n", strlen(lps), lps);
      }
    }
  }
  fclose(infile);
  fclose(outfile);
  return 0;
}
