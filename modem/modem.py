#!/usr/local/bin/python3
import sys
import serial.tools.list_ports as stools
import serial
import select
import os
import time

def send(modem, str, wait=0.1):
    start = time.time()
    end = time.time() + wait
    str += "\r"
    os.write(modem, str.encode('utf-8'))
    now = time.time()
    while now < end:
        readers, _, _ = select.select([modem], [], [], end - now)
        for reader in readers:
            read = os.read(modem, 32)
            print(f"Read: {read}")
        now = time.time()

def ring(modem):
    send(modem, "ATH1", 20)
    send(modem, "ATH0Z0", 1)

def hangup(modem):
    send(modem, "ATH0Z0")

def reset(modem):
    send(modem, "ATZ0")

if len(sys.argv) < 2:
    print("Usage:")
    print(f"{sys.argv[0]} <command> [<device>]")
    print("Where command is one of 'ring' or 'hangup' or 'reset'")
    sys.exit(1)

# Look for a modem
if len(sys.argv) < 3:
    ports = list(stools.grep(r"cu\.usbmodem"))
    if len(ports) == 0:
        print("No modems found")
        sys.exit(1)
    elif len(ports) != 1:
        print("More (or less) than one modem found:")
        for p in ports:
            print(p)
        sys.exit(1)
    dev = ports[0].device
else:
    dev = sys.argv[2]

modem = os.open(dev, os.O_RDWR)

if sys.argv[1] == "ring":
    ring(modem)
elif sys.argv[1] == "hangup":
    hangup(modem)
elif sys.argv[1] == "reset":
    reset(modem)
else:
    print(f"Unknown command {sys.argv[1]}")
    sys.exit(1)

os.close(modem)
