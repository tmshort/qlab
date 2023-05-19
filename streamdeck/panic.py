#!/usr/local/bin/python3
from pythonosc.udp_client import SimpleUDPClient
import time

client = SimpleUDPClient("localhost", 53535)
client.send_message("/PANIC", [])
time.sleep(0.2)
client.send_message("/PANIC", [])
