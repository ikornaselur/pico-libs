# Assumes device port
PYB=python .pyboard.py --device /dev/tty.usbmodem0000000000001

.pyboard.py:
	@wget -q https://raw.githubusercontent.com/micropython/micropython/master/tools/pyboard.py -O .pyboard.py

lib: .pyboard.py
	@$(PYB) -f ls | grep "lib/" >/dev/null|| ($(PYB) -f mkdir lib)

deploy_shift: lib
	@echo "Deploying SN74HC595N library to /lib"
	@$(PYB) -f cp shift/shift.py :lib/shift.py

deploy_dht: lib
	@echo "Deploying DHT11 library to /lib"
	@$(PYB) -f cp dht/dht.py :lib/dht.py
