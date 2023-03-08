#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

ssize_t array[10];

void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

ssize_t getval(const char *msg) {
  char buf[0x20] = {};
  write(STDOUT_FILENO, msg, strlen(msg));
  read(STDIN_FILENO, buf, sizeof(buf)*0x20);
  return atoll(buf);
}

int main() {
  ssize_t index, value;

  index = getval("index: ");
  printf("0x%016lx\n", array[index]);
  fflush(stdout);

  index = getval("index: ");
  value = getval("value: ");
  array[index] = value;

  index = getval("index: ");
  value = getval("value: ");
  array[index] = value;

  return 0;
}
