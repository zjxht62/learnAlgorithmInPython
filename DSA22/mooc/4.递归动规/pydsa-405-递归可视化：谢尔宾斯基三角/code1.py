# 画谢尔宾斯基三角形
import turtle

def sierpinski(degree, points):
    colormap = ['blue', 'red' ,'green', 'white', 'yellow', 'orange']
    # 绘制等边三角形
    drawTriangle(points, colormap[degree])
    # 最小规模0，直接退出
    if degree > 0:
        # 减小规模，get_mid边长减半
        # 调用自身，左上右次序
        sierpinski(degree -1, {
            'left':points['left'],
            'top':get_mid(points['left'], points['top']),
            'right':get_mid(points['left'], points['right'])
        })
        sierpinski(degree -1, {
            'left':get_mid(points['left'], points['top']),
            'top':points['top'],
            'right':get_mid(points['top'], points['right'])
        })
        sierpinski(degree -1, {
            'left':get_mid(points['left'], points['right']),
            'top':get_mid(points['top'], points['right']),
            'right':points['right'],
        })

def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


# 获取两个点的中点
def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


t = turtle.Turtle()
# 外轮廓的三个点
points = {
    'left': (-200, -100),
    'top': (0, 200),
    'right': (200, -100)
}
sierpinski(5, points)
turtle.done()


