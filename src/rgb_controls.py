#!/usr/bin/env python
"""
"""
import logging
import sys
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
import font


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
        devices = get_devices_by_type(DeviceType.DEVICE_NAME)[0]


if __name__ == "__main__":
    pass
