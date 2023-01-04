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

    def _check_devices(self):
        self.devices = self.cli.get_devices_by_type(DeviceType.DEVICE_NAME)[0]
        if len(self.devices) < MIN_DEVICES:
            raise ValueError

    def clear(self):
        """
        """
        for device in self.devices:
            # write BLACK (0,0,0) to the stick
            pass
        
    def fill_buffer(self, message):
        pass

    def push_buffer(self):
        pass  


if __name__ == "__main__":
    pass
