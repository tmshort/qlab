#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  useconds_t usec = 0;
  if (argc > 1)
    usec = atol(argv[1]);
  return usleep(usec);
}
