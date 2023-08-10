Modem Scripts
=============

These scripts allow interaction with a USB modem to ring a telephone.

Setup
-----
```

[Mac] --> USB-modem --> [Viking DLE-200B](https://vikingelectronics.com/products/dle-200b/) --> Telephone

```

Scripts
-------

* `ring.sh` is used to start a call
* `hangup.sh` is used to hang up a call
* `reset_modem.sh` is used to reset the modem before or after use
* `modem.py` can be used to perform all of the above (commands = `ring`, `hangup` and `reset`)

Programs
--------

The file `modem.c` is used to interact with the USB serial port. Used by `ring.sh`. To build:
```
gcc -o modem modem.c
```


