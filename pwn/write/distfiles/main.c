#include <stdlib.h>
#include <string.h>
#include <unistd.h>

ssize_t array[10];

void win(void) {
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

#define getval(msg)                             \
  ({                                            \
    char buf[0x20] = {};                        \
    write(STDOUT_FILENO, msg, strlen(msg));     \
    read(STDIN_FILENO, buf, sizeof(buf)*0x20);  \
    atoll(buf);                                 \
  })

int main() {
  ssize_t index, value;
  index = getval("index: ");
  value = getval("value: ");
  array[index] = value;
  return 0;
}
