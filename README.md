# GP1818MK-GPS-Module
Establishing data collection capabilities from the GP1818MK GPS Module from Sparkfun

## GPS Module Information
I acquired the [GP1818MK GPS Module (SKU: GPS-19166) from Sparkfun](https://www.sparkfun.com/gps-module-gp1818mk-56-channel.html). 
In particular, I have S/N 220107047. 
Documentation on this module can be found [here on Sparkfun](https://cdn.sparkfun.com/assets/f/2/4/6/d/GP-1818MK.pdf).

The objective of this repository is to provide python code which can read the GPS receiver data (NMEA-0183 Ver 3.01 Protocol Message) from a raspberry pi. In particular, I am using a Raspberry Pi 4b with the "Trixie" version of Raspian from Debian.

## GPS Module Modifications
By default, this module ships with a MOLEX connecter, but I ended up converting the three wires into individual DuPont connecters to make an easy interface with the Raspberry Pi GPIO Pins.
