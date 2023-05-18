#!/usr/local/bin/python3
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient("localhost", 53535).send_message("/PREV", [])
