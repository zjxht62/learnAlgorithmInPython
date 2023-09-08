# 无限递归导致调用栈溢出
def tell_story():
    print("从前有座山，山里有座庙，，庙里有个老和尚讲故事，讲的是：")
    tell_story()

print("给你讲个故事")
tell_story()