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


Programs
--------

The file `modem.c` is used to interact with the USB serial port. To build:
```
gcc -o modem modem.c
```


