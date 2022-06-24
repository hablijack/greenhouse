#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.MagnetValves import MagnetValves

if __name__ == '__main__':
    MagnetValves().switch(1, False)
    MagnetValves().switch(2, False)
    MagnetValves().switch(3, False)
    MagnetValves().switch(4, False)