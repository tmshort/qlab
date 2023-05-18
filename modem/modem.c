#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>

#define MAXLINE 1024

int main(int argc, char *argv[])
{
  char buffer[MAXLINE];
  fd_set rset;
  int fd;
  struct timeval tv;
  int ready;
  ssize_t bytes_read;
  ssize_t bytes_written;
  int wait = 1;

  if (argc < 3) {
    printf("Usage: %s <device> <text>\n", argv[0]);
    exit(1);
  }

  if (argc == 4) {
    wait = atoi(argv[3]);
  }

  fd = open(argv[1], O_RDWR);

  if (fd == -1) {
    perror("open()");
    exit(1);
  }

  memset(buffer, 0, sizeof(buffer));
  bytes_read = snprintf(buffer, sizeof(buffer), "%s\r", argv[2]);
  if (bytes_read == -1) {
    perror("snprintf()");
    exit(1);
  }
  if (bytes_read >= sizeof(buffer)) {
    printf("<text> too long\n");
    exit(0);
  }

  bytes_written = write(fd, buffer, bytes_read);
  if (bytes_written == -1) {
    perror("write()");
    exit(1);
  }

  // get maxfd
  while (1) {
    FD_ZERO(&rset);
    FD_SET(fd, &rset);
    tv.tv_sec = wait;
    tv.tv_usec = 0;

    ready = select(fd + 1, &rset, NULL, NULL, &tv);
    if (ready == -1) {
      perror("select()");
      exit(1);
    }

    if (ready == 1) {
      /* READ */
      memset(buffer, 0, sizeof(buffer));
      bytes_read = read(fd, buffer, sizeof(buffer));
      if (bytes_read == -1) {
	perror("read()");
	exit(1);
      }
      bytes_written = write(1, buffer, bytes_read);
      if (bytes_written == -1) {
	perror("write()");
	exit(1);
      }
    }
    if (ready == 0) {
      /* DONE! */
      exit(0);
    }
  }
}
