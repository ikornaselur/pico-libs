# Raspberry Pico libraries

A collection of libraries written for different modules and projects. Rather
than keeping them all in a separate repo, since they are fairly simple, I
decided to keep them in a single repo. This way I can also sort out scripts to
"deploy" these libraries to the Pico while developing

## Libs
The Pico comminucation is done with the `pyboard.py` script from MicroPython,
which is fetched for the first time any command that depends on it is run

### SN74HC595N shift register
Provides functionality to write out list of bits or an integer out to a
SN74HC595N shift register.

Add with `deploy_shift` make target

### DHT11 humidity and temperature sensor
Reads from a DHT11 sensor, providing air humidity and temperature values up to
once every second

Add with `deploy_dht` make target
