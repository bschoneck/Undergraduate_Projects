//prodcon

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

int TransSave = 0;

// create Summary vars
int *thread_complete;
int num_work = 0;
int num_ask = 0;
int num_receive = 0;
int num_complete = 0;
int num_sleep = 0;


// create queue
int *work_queue;
int queue_max = 0;
int queue_start = 0;
int queue_end = 0;
int queue_size = 0;

// signal end of file reached
int EOF_signal = 0;

//create id counter
int counter = 1;

// timer vars
clock_t start_time, end_time;

// tst shared var
int test = 0;

// file ptr
FILE *f;

// mutex for entire queue
pthread_mutex_t queue_mutex = PTHREAD_MUTEX_INITIALIZER;

// mutex for file
pthread_mutex_t file_mutex = PTHREAD_MUTEX_INITIALIZER;

// wait condition for empty
pthread_cond_t is_empty = PTHREAD_COND_INITIALIZER;

void Sleep( int n );
void Trans( int n );
char *get_file_name(int num_args, char *id);
void *thread_work(void *var);

void Trans( int n ) {
	long i, j;

	// Use CPU cycles
	j = 0;
	for( i = 0; i < n * 100000; i++ ) {
		j += i ^ (i+1) % (i+n);
	}
	TransSave += j;
	TransSave &= 0xff;
}

void Sleep( int n ) {
	struct timespec sleep;

	// Make sure pass a valid nanosecond time to nanosleep
	if( n <= 0 || n >= 100 ) {
		n = 1;
	}

	// Sleep for less than one second
	sleep.tv_sec  = 0;
        sleep.tv_nsec = n * 10000000 + TransSave;
	if( nanosleep( &sleep, NULL ) < 0 ) {
		perror ("NanoSleep" );
	}
}

char *get_file_name(int num_args, char *id) {

  // initialize file parts
  char start_file[10] = "prodcon.";
  char end_file[4] = "log";
  char *outfile = (char*) malloc(20 * sizeof(char));

  // insert start to file
  for(int i = 0; i < strlen(start_file); i++) {
    outfile[i] = start_file[i];
  }

  int outfile_len = strlen(outfile);

  // get file name
  // if id given
  if(num_args > 2 && atoi(id) > 0) {
    // add id to string
    for(int i = 0; i < strlen(id); i++) {
      outfile[outfile_len + i] = id[i];
    }

    // add '.' to string and incement
    outfile_len = strlen(outfile);
    outfile[outfile_len] = '.';
    outfile_len++;
  }

  // add ending to file
  for(int i = 0; i < strlen(end_file); i++) {
    outfile[outfile_len + i] = end_file[i];
  }

  return outfile;
}


void *thread_work(void *id) {

  long thread_id = (long) id;
  int current_size;
  int thread_inst;
  double current_time;

  //printf("thread id = %ld\n", thread_id);

  while(1){
    // WAIT FOR CHANCE TO WRITE TO FILE
    end_time = clock();
    current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    pthread_mutex_lock(&file_mutex);

    fprintf(f, "%8.3lf ID=%2ld      Ask\n", current_time, thread_id);
    num_ask++;
    pthread_mutex_unlock(&file_mutex);

    // WAIT FOR QUEUE ACCESS
    pthread_mutex_lock(&queue_mutex);
    // ACCESS QUEUE HERE

    while(queue_size <= 0 || work_queue[queue_start] == 0) {
      if(EOF_signal) {
        pthread_mutex_unlock(&queue_mutex);
				pthread_cond_broadcast(&is_empty);
        pthread_exit(NULL);
      }
      pthread_cond_wait(&is_empty, &queue_mutex);
    }
    thread_inst = work_queue[queue_start];
    work_queue[queue_start] = 0;
    queue_start++;
    if(queue_start == queue_max) {
      queue_start = 0;
    }
    //queue_size--;
    current_size = --queue_size;
    pthread_mutex_unlock(&queue_mutex);


    end_time = clock();
    current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    // WAIT FOR CHANCE TO WRITE TO FILE
    pthread_mutex_lock(&file_mutex);

    fprintf(f, "%8.3lf ID=%2ld Q=%2d Receive      %3d\n", current_time, thread_id, current_size, thread_inst);
    num_receive++;
    pthread_mutex_unlock(&file_mutex);

    // PREFORM WORK
    Trans(thread_inst);

    end_time = clock();
    current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
    // WAIT FOR CHANCE TO WRITE TO FILE
    pthread_mutex_lock(&file_mutex);

    fprintf(f, "%8.3lf ID=%2ld      Complete     %3d\n", current_time, thread_id, thread_inst);
    num_complete++;
    thread_complete[thread_id - 1]++;
    pthread_mutex_unlock(&file_mutex);
  }

  return NULL;
}

int main(int argc, char **argv) {

  // start timer
  start_time = clock();

  // set to proper int
  int nthreads = atoi(argv[1]);
  queue_max = 2 * nthreads;

  // get file name
  char *outfile;
  outfile = get_file_name(argc, argv[2]);

  // open file
  f = fopen(outfile, "w");

  // initialize thread complete counter
  thread_complete = (int *) malloc(nthreads * sizeof(int));
  for(int i = 0; i < nthreads; i++) {
    thread_complete[i] = 0;
  }

  // initialize queue
  work_queue = (int *) malloc(queue_max * sizeof(int));
  for(int i = 0; i < queue_max; i++) {
    work_queue[i] = 0;
  }

  // create threads
  pthread_t thread[nthreads];
  for(long i = 0; i < nthreads; i++) {
    pthread_create(&thread[i], NULL, thread_work, (void *) (i+1));
  }

  // MASTER THREAD WORK HERE

  int current_size;
  double current_time;

  // collect work from input
  char work_inst = getc(stdin);
  int work_val = 0;
  while(work_inst != EOF) {
    //printf("%s", work_inst);

    if(work_inst == 'T') {

      scanf("%d", &work_val);

      // CHECK IF ROOM TO ADD AND WAIT IF FULL
      while(queue_size >= queue_max || work_queue[queue_end] != 0) {
      }

      // ADD TO WORK QUEUE
      work_queue[queue_end] = work_val;
      queue_end++;
      if(queue_end == queue_max) {
        queue_end = 0;
      }
      current_size = ++queue_size;

      // BROADCAST WORK ADDED (maybe not?!)
      pthread_cond_broadcast(&is_empty);
			//pthread_cond_signal(&is_empty);



      end_time = clock();
      current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
      // WAIT FOR CHANCE TO WRITE TO FILE
      pthread_mutex_lock(&file_mutex);

      fprintf(f, "%8.3lf ID= 0 Q=%2d Work         %3d\n", current_time, current_size, work_val);
      num_work++;
      pthread_mutex_unlock(&file_mutex);


    }
    else if(work_inst == 'S'){

      scanf("%d", &work_val);

      // WAIT FOR CHANCE TO WRITE TO FILE
      end_time = clock();
      current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
      pthread_mutex_lock(&file_mutex);
      fprintf(f, "%8.3lf ID= 0      Sleep        %3d\n", current_time, work_val);
      num_sleep++;
      pthread_mutex_unlock(&file_mutex);

      // CALL SLEEP
      Sleep(work_val);

    }
    work_inst = getc(stdin);
  }
	printf("producer got thru\n");
  EOF_signal = 1;
  end_time = clock();
  current_time = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
  pthread_mutex_lock(&file_mutex);
  fprintf(f, "%8.3lf ID= 0      End\n", current_time);
  pthread_mutex_unlock(&file_mutex);

  // wait for consumers to finish
  for(int i = 0; i < nthreads; i++) {
    pthread_join(thread[i], NULL);
  }


  // SUMMARY

  fprintf(f, "Summary:\n");
  fprintf(f, "    Work          %3d\n", num_work);
  fprintf(f, "    Ask           %3d\n", num_ask);
  fprintf(f, "    Receive       %3d\n", num_receive);
  fprintf(f, "    Complete      %3d\n", num_complete);
  fprintf(f, "    Sleep         %3d\n", num_sleep);

  for(int i = 0; i < nthreads; i++) {
    fprintf(f, "    Thread %3d    %3d\n", i+1, thread_complete[i]);
  }
  double tps = num_complete / (((double) (end_time - start_time)) / CLOCKS_PER_SEC);
  fprintf(f, "Transactions per second: %3.3lf\n", tps);

  pthread_mutex_destroy(&queue_mutex);
  pthread_mutex_destroy(&file_mutex);
  pthread_cond_destroy(&is_empty);
  pthread_exit(NULL);

  free(outfile);
  free(work_queue);
  fclose(f);
  return 0;
}
