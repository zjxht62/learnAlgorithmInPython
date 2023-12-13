# 递归的应用：探索迷宫
## 探索迷宫
### 将海龟放在迷宫中间，如何能找到出口
### 首先，我们先将整个迷宫的空间（矩形）分为行列整齐的方格，区分出墙壁和通道。
给每个方格具有行列位置，并赋予“墙壁”、“通道”的属性
## 迷宫的数据结构
### 考虑采用矩阵的方式来实现迷宫的数据结构
采用“数据项为**字符列表**的**列表**”这种两级列表的方式来保存方格内容  
采用不同的字符来分别代表“墙壁+”、“通道 ”、“海龟投放点S“  
从一个文本文件逐行读入迷宫数据
## 迷宫的数据结构：Maze Class
```python
class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        colums_in_maze = 0
        maze_file = open(maze_file_name, 'r')
        self.maze_list = []
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col += 1
            rows_in_maze += 1
            self.maze_list.append(row_list)
            colums_in_maze = len(row_list)
```