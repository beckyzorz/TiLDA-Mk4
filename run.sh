#!/bin/bash

os=$(uname -a)
case $os in
*Darwin*)
 screen /dev/tty.usbmodemTiLDA2 115200
;;
*Linux*) 
 minicom -D /dev/ttyACMO -b 115200
;;
*)
 printf "You're probably using Windows. \nOpen or download putty.\nOpen device manager to find the COM port your badge is using.\nConnect to COM port in putty.\n"
;;
esac
