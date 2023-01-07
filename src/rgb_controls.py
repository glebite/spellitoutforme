#!/usr/bin/env python
"""
"""
import logging
import sys
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
import font


SHIFT_TIME_DELAY = 5
MIN_DEVICES = 4
DEVICE_NAME = "Corsair Vengeance Pro RGB"
MODE = "Direct"
MAX_LEDS = 10

# colours:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class RAMWords:
    """
    """
    def __init__(self):
        """
        """
        try:
            self.cli = OpenRGBClient()
        except Exception as e:
            logging.info(f'Connection problem: {e}')
            sys.exit(1)
        self.font = font.Font()

    def _check_devices(self):
        self.devices = self.cli.get_devices_by_type(DeviceType.DEVICE_NAME)[0]
        if len(self.devices) < MIN_DEVICES:
            raise ValueError

    def clear(self):
        """
        """
        for device in self.devices:
            # write BLACK (0,0,0) to the stick
            for led in range(0, MAX_LEDS):
                # set colour BLACK
                pass
        
    def fill_buffer(self, message):
         for character in message:
             # process the character using the font
             pass

    def push_buffer(self):
        pass  


if __name__ == "__main__":
    pass
