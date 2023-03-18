#include <stdlib.h>
#include <string.h>
#include <unistd.h>

size_t array[10];

void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

void printval(size_t val) {
  char buf[0x20] = {}, *p = buf + sizeof(buf) - 1;
  *--p = '\n';
  do {
    *--p = '0' + (val % 10);
    val /= 10;
  } while (val);
  write(STDOUT_FILENO, p, buf+sizeof(buf)-p-1);
}

size_t getval(const char *msg) {
  char buf[0x20] = {};
  write(STDOUT_FILENO, msg, strlen(msg));
  read(STDIN_FILENO, buf, sizeof(buf));
  return atoll(buf);
}

int main() {
  size_t index, value;

  for (int i = 0; i < 3; i++) {
    switch (getval("1. read\n2. write\n> ")) {
      case 1: // read
        index = getval("index: ");
        printval(array[index]);
        break;

      case 2: // write
        index = getval("index: ");
        value = getval("value: ");
        array[index] = value;
        break;

      default:
        return 0;
    }
  }

  return 0;
}
