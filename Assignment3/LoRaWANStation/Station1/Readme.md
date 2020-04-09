## Virtual Environmental Station 1

This application this application generates random values and sends them every 20 seconds to TTN


## USAGE

Run the application for the B-L072Z-LRWAN1 board

    $ make BOARD=b-l072z-lrwan1 flash term


If you use a node on IoT-LAB follow this [Tutorial](https://www.iot-lab.info/tutorials/riot-ttn/)


If you want to compile the code on you laptop and than flash it on a node on IoT-LAB:

    $ make all clean
   
use the new .elf file to flash it on the node.
