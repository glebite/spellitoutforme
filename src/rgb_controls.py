#!/usr/bin/env python
"""
rgb_controls.py
"""
# import logging
import sys
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
import font


SHIFT_TIME_DELAY = 5
MIN_DEVICES = 4
DEVICE_NAME = "Corsair Vengeance Pro RGB"
MODE = "Direct"
MAX_LEDS = 10


# colours:
BLACK = RGBColor(0, 0, 0)
WHITE = RGBColor(255, 255, 255)
RED = RGBColor(255, 0, 0)
GREEN = RGBColor(0, 255, 0)
BLUE = RGBColor(0, 0, 255)


class RAMWords:
    """RAMWords - class for displaying text on RAM
    """
    def __init__(self):
        """
        """
        try:
            self.cli = OpenRGBClient()
            self._check_devices()
        except Exception as e:
            print(f'Connection problem: {e}')
            sys.exit(1)
        self.font = font.Font()

    def _check_devices(self):
        """
        """
        self.devices = self.cli.get_devices_by_name(DEVICE_NAME)
        if len(self.devices) < MIN_DEVICES:
            raise ValueError
        else:
            for device in self.devices:
                device.set_mode('direct')

    def __str__(self):
        return f"RAMWords {DEVICE_NAME=}"

    def clear(self):
        """
        """
        for device in self.devices:
            device.zones[0].set_color(BLACK)
        self.buffer = []

    def fill_buffer(self, message):
        for character in message:
            # process the character using the font
            self.buffer += self.font[character]

    def push_buffer(self):
        pass

    def output_buffer(self):
        """
        """
        self.buffer = self.font.rotate(65)
        for i in range(7, 6, -1):
            bit = pow(2, i)
            for counter, byte_set in enumerate(self.buffer):
                if bit & byte_set:
                    self.devices[0].leds[counter].set_color(GREEN)
                else:
                    self.devices[0].leds[counter].set_color(BLACK)
                print(i, bit, byte_set, bit & byte_set)

if __name__ == "__main__":
    x = RAMWords()
    x.clear()
    x.output_buffer()
