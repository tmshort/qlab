#!/bin/sh
# echo -e "ATH1\\r" >> /dev/cu.usbmodem123456781
# echo -e "ATS7=30A\\r" >> /dev/cu.usbmodem123456781
# echo -e "ATS6=30D\\r" >> /dev/cu.usbmodem123456781
# echo -e "ATZ0H1\\r" >> /dev/cu.usbmodem123456781
~/git/qlab/modem/modem /dev/cu.usbmodem123456781 "ATH1" 20
~/git/qlab/modem/modem /dev/cu.usbmodem123456781 "ATH0Z0"
