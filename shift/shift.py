from machine import Pin


class ShiftRegister:
    def __init__(self, serial, oe, register_clock, serial_clock, serial_clear):
        self.serial = Pin(serial, Pin.OUT, Pin.PULL_DOWN, value=0)
        self.oe = Pin(oe, Pin.OUT, Pin.PULL_UP, value=1)
        self.register_clock = Pin(register_clock, Pin.OUT, Pin.PULL_DOWN, value=0)
        self.serial_clock = Pin(serial_clock, Pin.OUT, Pin.PULL_DOWN, value=0)
        self.serial_clear = Pin(serial_clear, Pin.OUT, Pin.PULL_UP, value=1)

    def clear(self):
        self.serial_clear.value(0)
        self.register_clock.value(1)
        self.register_clock.value(0)
        self.serial_clear.value(1)

    def enable(self):
        self.clear()
        self.oe.value(0)

    def disable(self):
        self.oe.value(1)

    def write_bits(self, bits):
        self.clear()

        self.oe.value(1)

        for bit in bits:
            self.serial.value(bit)
            self.serial_clock.value(1)
            self.serial_clock.value(0)
            self.register_clock.value(1)
            self.register_clock.value(0)

        self.oe.value(0)

    def write_int(self, integer, le=False):
        bits = [int(bit) for bit in "{:08b}".format(integer)]
        if le:
            bits = bits[::-1]
        self.write_bits(bits)
