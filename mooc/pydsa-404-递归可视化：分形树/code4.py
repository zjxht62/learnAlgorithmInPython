# 递归作图：螺旋

import turtle

t = turtle.Turtle()


def draw_spiral(t: turtle.Turtle, length):
    if length > 0: # 最小规模0，直接退出
        t.forward(length)
        t.left(90)
        draw_spiral(t, length - 5) # 减小规模，边长-5，调用自身


draw_spiral(t, 100)
turtle.done()
