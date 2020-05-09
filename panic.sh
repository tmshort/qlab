#!/bin/sh
nc -w 0 -u localhost 53535 <<EOF
/PANIC
EOF
./usleep 200000
nc -w 0 -u localhost 53535 <<EOF
/PANIC
EOF
