#-*- coding: utf-8 -*-

num = int(raw_input("Give me a number."))

def build_pyramid(bacis_num):

    brick = '*'

    # 一次增加兩階
    for i in range(1, bacis_num + 1, 2):
        bricks = brick * i
        print(bricks.center(bacis_num, ' '))

build_pyramid(num)
