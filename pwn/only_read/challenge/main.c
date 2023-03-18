#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define printval(_val)                                \
  {                                                   \
    size_t val = (_val);                              \
    char buf[0x20] = {}, *p = buf + sizeof(buf) - 1;  \
    *--p = '\n';                                      \
    do {                                              \
      *--p = '0' + (val % 10);                        \
      val /= 10;                                      \
    } while (val);                                    \
    write(STDOUT_FILENO, p, buf+sizeof(buf)-p-1);     \
  }                                                   \

#define getval(msg)                             \
  ({                                            \
    char buf[0x20] = {};                        \
    write(STDOUT_FILENO, msg, strlen(msg));     \
    read(STDIN_FILENO, buf, sizeof(buf)*0x20);  \
    atoll(buf);                                 \
  })

int main() {
  size_t array[10] = {};

  for (;;) {
    ssize_t index = getval("index: ");
    if (index >= 10) break;
    printval(array[index]);
  }

  return 0;
}
