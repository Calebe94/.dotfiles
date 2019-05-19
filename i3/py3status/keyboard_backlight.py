# -*- coding: utf-8 -*-
"""
author: Edimar Calebe Castanho(Calebe94)

Module to control my keyboard backlight brightness
"""

class Py3status:
    percent = str()
    def keyboard_backlight(self):
        with open("/sys/class/leds/smc::kbd_backlight/brightness", "r") as brightness:
            self.percent = brightness.read()
            self.percent = ' {}%'.format(int(int(self.percent.strip())*100/255))

        return {
            'full_text': self.percent,
            'cached_until': self.py3.time_in()
        }
