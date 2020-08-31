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

    def draw_underlined_text(self, draw, pos, text, font, **options):
        twidth, theight = draw.textsize(text, font=font)
        lx, ly = pos[0], pos[1] + theight
        draw.text(pos, text, font=font, **options)
        #  draw.line((lx, ly, lx + twidth, ly), **options)
        draw.line((0, ly, 128, ly), **options)

    def render(self, current_values):
        self.OLED_DISPLAY.begin()
        self.OLED_DISPLAY.clear()
        self.OLED_DISPLAY.display()
        font = ImageFont.truetype("monofonto.ttf", 12)
        image = Image.new('1', (self.OLED_DISPLAY.width, self.OLED_DISPLAY.height))
        draw = ImageDraw.Draw(image)

        draw.rectangle((0,0,self.OLED_DISPLAY.width,self.OLED_DISPLAY.height), outline=0, fill=0)
        air_temp_inside_text = "Luft: " + str(current_values['air_temp_inside']) + "°C"
        humidity_inside_text = str(current_values['humidity_inside']) + "%"
        soil_temp_inside_text = "Boden: 00°C"
        soil_moisture_inside_text = "00% 00% 00%"

        self.draw_underlined_text(draw, (98, 0), "Innen", font, fill=255)
        draw.text((0, 12), air_temp_inside_text, font=font, fill=255)
        draw.text((35, 26), humidity_inside_text, font=font, fill=255)
        draw.text((0, 38), soil_temp_inside_text, font=font, fill=255)
        draw.text((40, 52), soil_moisture_inside_text, font=font, fill=255)

        # Display image.
        self.OLED_DISPLAY.image(image)
        self.OLED_DISPLAY.display()
