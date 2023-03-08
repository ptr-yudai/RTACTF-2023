#include <stdlib.h>
#include <string.h>
#include <unistd.h>

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
  return getval("value: ");
}
