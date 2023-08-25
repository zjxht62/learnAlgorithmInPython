import turtle

def tree(t:turtle.Turtle, branch_len):
    if branch_len > 5: # 如果树干太短，就不画，即递归结束条件
        t.forward(branch_len) # 画树干
        t.left(20) # 左倾斜20
        tree(t, branch_len -15) # 画左子树，树干-15
        t.right(40) # 右倾斜40
        tree(t, branch_len -15) # 画右子树，树干-15
        t.left(20) # 左倾斜20 ，回正
        t.back(branch_len) # 退回原始位置

if __name__ == '__main__':
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.back(100)
    t.pendown()
    t.pencolor('green')
    t.pensize(2)
    tree(t, 75)
    t.hideturtle()
    turtle.done()