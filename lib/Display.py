#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Display:

    OLED_DISPLAY = Adafruit_SSD1306.SSD1306_128_64(rst=None)

    def render(self, current_values):
        self.OLED_DISPLAY.begin()
        self.OLED_DISPLAY.clear()
        self.OLED_DISPLAY.display()
        font = ImageFont.truetype("monofont.ttf", 8)
        image = Image.new('1', (self.OLED_DISPLAY.width, self.OLED_DISPLAY.height))
        draw = ImageDraw.Draw(image)

        draw.rectangle((0,0,self.OLED_DISPLAY.width,self.OLED_DISPLAY.height), outline=0, fill=0)

        draw.text((0, 0), str(current_values['air_temp_inside']), font=font, fill=255)
        #draw.text((0, 8), str(current_values['light_inside']), font=font, fill=255)
        #draw.text((0, 16), str(current_values['humidity_inside']), font=font, fill=255)

        # Display image.
        self.OLED_DISPLAY.image(image)
        self.OLED_DISPLAY.display()
