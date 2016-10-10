PowerSwitch for Raspberry PI

@found from: http://www.forum-raspberrypi.de/Thread-tutorial-hoch-und-runterfahren-mittels-taster-incl-status-led

# Prepare
* sudo apt-get update
* sudo apt-get install python-dev
* sudo apt-get install python-rpi.gpio

# Software
* sudo chmod +x PATH/shutdown.py

###### add script to startup
* sudo nano /etc/rc.local

###### add line before "exit 0"
* sudo python PATH/shutdown.py &

# Hardware
* 1 Taster/Button
* 1 LED
* 1 Widerstand/Resistor 10k Ohm
* 1 Widerstand/Resistor 200 Ohm (for LED)

Connect GPIO-4 with 200 Ohm Resistor and LED to GND.

Connect 3.3V to 10k Ohm Resistor. Connect Resistor with GPIO-3 for Input and with the Button. Connect the Button also with GND.


