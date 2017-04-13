#-*- coding: utf-8 -*-

# 寬和高為多少的正方形
def window(width=1, height=1):

    # 檢查長寬是不是整數類型
    width = width if type(width) is int else 1
    height = height if type(height) is int else 1

    # 長或是寬各需要多少單位
    # 可直接更改
    w_amounts = 12
    h_amounts = 5

    # 檢查長或寬是否大於1，是的話還要加上裡面的多出來的單位
    h_extra = (height - 1 if height > 1 else 0) + 2
    w_extra = (width - 1 if width > 1 else 0) + 2

    # 會出現邊的座標
    w_corner = w_amounts + 1
    h_corner = h_amounts + 1

    corner_unit = '+'
    width_unit = '-'
    height_unit = '|'

    def is_w_corner(w, w_corner):
        return w == 0 or w % w_corner == 0

    def is_h_corner(h, h_corner):
        return h == 0 or h % h_corner == 0

    for h in range(height * h_amounts + h_extra):
        single_line = []

        for w in range(width * w_amounts + w_extra):

            if is_h_corner(h, h_corner) and is_w_corner(w, w_corner):
                single_line.append(corner_unit)

            elif is_h_corner(h, h_corner):
                single_line.append(width_unit)

            elif is_w_corner(w, w_corner):
                single_line.append(height_unit)

            else:
                single_line.append(' ')

        print(''.join(single_line))

window(3, 3)
