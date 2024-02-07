# -*- coding: utf-8 -*-
"""
@original_author: MAPIR, Inc
@original_repository: https://github.com/mapircamera/camera-scripts

This is a downstream version adapted to work on Linux systems with the
help of Wine.
"""

import subprocess
import os

class ExifUtils:

    @staticmethod
    def copy_simple(inphoto, outphoto, startup_info):
        mod_path = os.path.dirname(os.path.realpath(__file__))
        exifout = subprocess.run(
            ['wine', mod_path + os.sep + r'exiftool.exe',
            r'-overwrite_original_in_place', r'-tagsFromFile',
            os.path.abspath(inphoto),
            r'-all:all<all:all',
            os.path.abspath(outphoto)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
            startupinfo=startup_info).stderr.decode("utf-8")

        data = subprocess.run(
                    args=['wine', mod_path + os.sep + r'exiftool.exe', '-m', r'-ifd0:imagewidth', r'-ifd0:imageheight', os.path.abspath(inphoto)],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE, startupinfo=startup_info).stderr.decode("utf-8")