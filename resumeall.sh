#!/bin/sh
nc -w 0 -u localhost 53535 <<EOF
/RESUMEALL
EOF
