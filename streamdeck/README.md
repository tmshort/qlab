StreamDeck Files
================

These files support interaction between QLab and a StreamDeck or other controller (even the terminal).

For StreamDeck, I recommend the **MIDI** or **OSC Remote** plug-ins; they're a bit easier than using python.

Images
------

A number of images are located in the `img` directory.

Requirements
------------

These scripts are designed for Macs that have installed python3 via [HomeBrew](https://brew.sh/). The scripts assume python3 is in `/usr/local/bin/python3`.

Also required is [python-ocs](https://pypi.org/project/python-osc/).

QLab is assumed to be listening on UDP port 53000.

Scripts
-------

* `go.py` sends the `/GO` OSC command.
* `next.py` sends the `/NEXT` OSC command.
* `panic.py` sends the `/PANIC` OSC command, twice.
* `pause.py` sends the `/PAUSE` OSC command.
* `pauseall.py` sends the `/PAUSEALL` OSC command.
* `prev.py` sends the `/PREV` OSC command.
* `reset.py` sends the `/RESET` OSC command.
* `resumeall.py` sends the `/RESUMEALL` OSC command.
* `stop.py` sends the `/PANIC` OSC command.
