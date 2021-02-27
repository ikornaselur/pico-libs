# Raspberry Pico libraries

A collection of libraries written for different modules and projects. Rather
than keeping them all in a separate repo, since they are fairly simple, I
decided to keep them in a single repo. This way I can also sort out scripts to
"deploy" these libraries to the Pico while developing

## Make targets

Currently there is a `deploy_shift` and `deploy_dht` target, which ensures that
there's a `lib/` folder on the Pico and then copies the libraries over.

The communication is done with the `pyboard.py` script from MicroPython, which
is fetched for the first time any command that depends on it is run
