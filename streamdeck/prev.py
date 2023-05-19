/#!/usr/local/bin/python3
from pythonosc.udp_client import SimpleUDPClient

SimpleUDPClient("localhost", 53000).send_message("/PREV", [])
