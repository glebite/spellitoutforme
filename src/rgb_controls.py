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
        """
        """
        for character in message:
            # process the character using the font
            self.buffer += self.font[character]

    def push_buffer(self):
        """
        """
        pass

    def output_buffer(self, message):
        """Need to incorporate recent whiteboard stuff.
        """
        self.buffer = self.font.sliced_buffer(message)
        print(len(self.buffer))
        for i in range(0, len(self.buffer)-4):
            shift = i % 4
            print(i, shift)
            for slice in self.buffer[i:i+4]:
                for pos, bit in enumerate(slice):
                    if bit:
                        self.devices[shift].leds[pos+1].set_color(GREEN)
                    else:
                        self.devices[shift].leds[pos+1].set_color(BLACK)


if __name__ == "__main__":
    x = RAMWords()
    x.clear()
    x.output_buffer("Hello")
