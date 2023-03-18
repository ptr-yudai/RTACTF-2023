#include <stdlib.h>
#include <string.h>
#include <unistd.h>

size_t array[10];

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
  read(STDIN_FILENO, buf, sizeof(buf)*0x20);
  return atoll(buf);
}

int main() {
  for (int i = 0; i < 5; i++) {
    size_t index = getval("index: ");
    printval(array[index]);
  }
  return 0;
}
