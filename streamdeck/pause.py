#!/usr/local/bin/python3
from pythonosc.udp_client import SimpleUDPClient

SimpleUDPClient("localhost", 53535).send_message("/PAUSE", [])
