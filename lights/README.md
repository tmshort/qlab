Light Cue Tracker
=================

This script helps users keep track of light cues. Light cues modify the
state of the DMX output, and after the light cue fade completes, the DMX
state remains. So, QLab effectively remains "in the light cue".

Stage managers and board ops will often ask "what light cue are we in?" and
QLab doesn't offer a way to view this in the main window. The cue is displayed
the Light DashBoard, but that window usually isn't visible (or desireable) in
show mode.

This script keeps track of the light cues that are invoked by QLab and displays
the result. It also offers the ability to back up to the previous light cue.

This gives some functionality of a lightboard to QLab.

Requirements
------------

These scripts are designed for Macs that have installed python3 via [HomeBrew](https://brew.sh/). The scripts assume python3 is in `/usr/local/bin/python3`.

Also required is [python-ocs](https://pypi.org/project/python-osc/).

QLab is assumed to be listening on UDP port 53000.

Setup
-----

1. Create a script cue named `LASTLIGHT` with the following script:
```
do shell script "/Users/<you>/git/qlab/lights/light-cues.py"
```
The cue name is important, as the name of the script is updated to reflect
the last light cue executed.

2. _Optional:_ Configure a Network output, if you want to do 3, below:

| Type | Network | Interface | Destination | Passcode |
|------|---------|-----------|-------------|----------|
| OSC Message | UDP | Automatic | 127.0.0.1 53001| |

3. _Optional:_ Create Network OSC cues to send commands to the Light Cue Tracker. Use hot keys (e.g. `B`) to quickly invoke them.

Possible commands (proably case-sensitive):
* `/clear` - clear cue data
* `/quit` - terminate the script
* `/pause` - temporarily pause the collecting of cue data
* `/resume` - continue collecting cue data
* `/back` - undo the previous light cue by running the Light cue prior to that. Reset the playhead to the previous Light cue. Useful when someone hit **GO**, one too many times.
* `/undo` - like `/back`, but don't reset the playhead, helps avoid re-running non-Light cues. If Light cues are not collated, this may result in unexpected behavior.

Running
-------

Start the `LASTLIGHT` cue, it will show up in the Active Cue list, and remain there. As light cues are executed, the name
of the `LASTLIGHT` cue will change to be the name of the Light cue just executed. If the `/back` option is sent, the prior
light cue is invoked, and the playhead is moved to the last light cue.

At least two light cues must have been run before `/back` has any effect.

Example:

* Light cue 1 was run
* Light cue 2 was run
* Playhead is now on light cue 3

The `LASTLIGHT` cue will be named `2`.

If `/back` is executed, then Light cue 1 is run again, and the playhead is moved to Light cue 2. The `LASTLIGHT` cue will be named `1`.

If `/undo` is executed, then Light cue 1 is run again, but the playhead remains at Light cue 3. The `LASTLIGHT` cue will be named `1`.

Hitting `ESC` or doing a panic, will terminate the script.

The `light-cues.py` script can be run outside of QLab, but the last light cue run will not show up in the Active cues.

Notes
-----

The script works best in a theatrical setting, where only one light cue is running at a time. If multiple Light cues
are run simultaneously, the program will still work, but the assumption is that the last invoked Light cue is the last
Light cue run, even if a prior light cue is still running. This is generally not compatible with the **collate** option,
however.

The **collate** option, which makes QLab more "light board"-like, will make the Light cues work better in this context.
No checks are made to see if the *colate* option is enabled.

When cues are auto-continued or auto-followed, it is generally better to have the Light cue at the end of the chain.

Non-Light cues are ignored when the playhead is reset via `/back`.
Thus, it might be possible that other cues (e.g. audio) are replayed because of this.
Hence, the "end-of-the-chain" recommendation.

Of course, if you end up skipping back over other types of cues, then it's likely those cues occured at the wrong time.
The `/undo` command may be more useful than `/back` in this case.
