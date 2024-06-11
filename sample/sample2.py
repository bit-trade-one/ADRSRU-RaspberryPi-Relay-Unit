#!/usr/bin/env python3
# - coding: utf-8 -
#
# ビット・トレード・ワン ADRSRUx リレー制御拡張基板(2,4,8回路)サンプルプログラム
# 　著作権者:(C) 2024 ビット・トレード・ワン社
# 　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： python3 sample.py [2|4|8]
#  機能　　： 出力ポートを1秒毎に順にON/OFF

import sys
from gpiozero import DigitalOutputDevice
from time import sleep

port_list = []
relay = []

# GPIO setup
def setupGPIO() :
    global relay
    relay = [DigitalOutputDevice(port) for port in port_list]

# GPIO write
def writeGPIO(port, value) :
    if value:
        relay[port].on()
    else :
        relay[port].off()

# main
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2 :
        print('Usage : python3 sample.py [2|4|8]')
        sys.exit(1)
    else :
        if   args[1] == '2' :
            port_list = [4, 17]                            # 2回路
        elif args[1] == '4' :
            port_list = [4, 17, 27, 22]                    # 4回路
        else :
            port_list = [4, 17, 27, 22, 18, 23, 24, 25]    # 8回路

        setupGPIO()

        for port in range(len(port_list)):
            print('port on :', port_list[port])
            writeGPIO(port, True)
            sleep(1)

        for port in range(len(port_list)):
            print('port off:', port_list[port])
            writeGPIO(port, False)

