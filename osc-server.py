#!/usr/local/bin/python3
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
from pythonosc.udp_client import SimpleUDPClient
import asyncio
import json

ip = "127.0.0.1"
listenPort = 53001
sendPort = 53000
update_cue = "LASTLIGHT"

client = SimpleUDPClient(ip, sendPort)

# Program state
run_program = True
pause = False

# Lists/Dicts of light cues, indexed by long cue name
# Map long light cue name to short cue number
cue_numbers = dict()
# List of light cues run
cues_run = list()

workspace = ""
def clear_handler(address, *args):
    cue_numbers = dict()
    cues_run = list()

def quit_handler(address, *args):
    run_program = False

def pause_handler(address, *args):
    pause = True

def resume_handler(address, *args):
    pause = False
    
def back_handler(address, *args):
    # Back up one light cue, but we need 2
    if len(cues_run) > 1:
        next_cue = cues_run.pop()
        rerun_cue = cues_run[-1]
        print(f"rerun: {cue_numbers[rerun_cue]}")
        print(f"next: {cue_numbers[next_cue]}")
        client.send_message(f"/workspace/{workspace}/cue_id/{rerun_cue}/start", [])
        client.send_message(f"/workspace/{workspace}/cue/{update_cue}/name", [f"{cue_numbers[rerun_cue]}",])
        client.send_message(f"/workspace/{workspace}/cue/{cue_numbers[next_cue]}/loadAndSetPlayhead", [])
    
def filter_handler(address, *args):
    print(f"{address}: {args}")

def update_handler(address, *args):
    # Check the type
    s = address.split("/");
    #print(f"update_handler: {s}")
    c = s[-1]
    if len(c) == 36:
        # Get the type and the number to save them
        client.send_message(f"/workspace/{s[3]}/cue_id/{s[5]}/type", [])
        client.send_message(f"/workspace/{s[3]}/cue_id/{s[5]}/number", [])

def type_handler(address, *args):
    # Check if running
    s = address.split("/");
    #print(f"type_handler: {s}")
    c = s[-2]
    if len(c) == 36:
        d = json.loads(args[0])
        t = d['data']
        if t == "Light":
            # this is a light cue, so determine if it is running
            print(f"Cue {c} type: {d['data']}")
            client.send_message(f"/workspace/{s[3]}/cue_id/{s[5]}/isActionRunning", [])

def number_handler(address, *args):
    # Save the short ID
    s = address.split("/");
    #print(f"number_handler: {s}")
    c = s[-2]
    if len(c) == 36:
        d = json.loads(args[0])
        cue_numbers[c] = d['data']
            
def running_handler(address, *args):
    # Check if running
    s = address.split("/");
    #print(f"running_handler: {s}")
    c = s[-2]
    if len(c) == 36:
        d = json.loads(args[0])
        running = d['data']
        # if it's running, and it's not the last cue on the list, add to the list
        #print(f"is running? {running}")
        global workspace
        workspace = s[3]
        if running:
            if (len(cues_run) == 0 or cues_run[-1] != c):
                #print(f"Adding cue {c} to cues_run")
                cues_run.append(c)
                # Update last cue running
                client.send_message(f"/workspace/{s[3]}/cue/{update_cue}/name", [f"{cue_numbers[c]}",])
            
            
    
dispatcher = Dispatcher()
dispatcher.map("/reply/workspace/*/cue_id/*/type", type_handler)
dispatcher.map("/reply/workspace/*/cue_id/*/isActionRunning", running_handler)
dispatcher.map("/reply/workspace/*/cue_id/*/number", number_handler)
dispatcher.map("/update/workspace/*/cue_id/*", update_handler)
dispatcher.map("/clear", clear_handler)
dispatcher.map("/quit", quit_handler)
dispatcher.map("/pause", pause_handler)
dispatcher.map("/resume", resume_handler)
dispatcher.map("/back", back_handler)

async def loop():
    count = 0
    while run_program:
        await asyncio.sleep(5)
        count = count + 1
        if count == 10:
            count = 0
            client.send_message("/thump", [])


async def init_main():
    server = AsyncIOOSCUDPServer((ip, listenPort), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving
    print(f"Listening on port {listenPort}")

    client.send_message("/updates", ["1",])
    client.send_message("/thump", [])

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint

asyncio.run(init_main())
