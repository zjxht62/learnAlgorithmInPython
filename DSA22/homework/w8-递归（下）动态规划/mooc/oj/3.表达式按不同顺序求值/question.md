## 3:表达式按不同顺序求值
总时间限制: 500ms 内存限制: 65536kB
### 描述
给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果

### 示例代码模板：
```python
def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    # code here

expr=input()
print(findWays(expr))
```

### 输入
一行字符串，仅包含0-9与运算符+、-与*

注：字符串保证三种运算符左右均为数字字符
### 输出
所有不重复的可能的结果，从小到大排序并以半角逗号","分隔
### 样例输入
```python
2*3-4*5
```
### 样例输出
```python
-34,-14,-10,10
```

### 提示
注：

(2*(3-(4*5))) = -34

((2*3)-(4*5)) = -14

((2*(3-4))*5) = -10

(2*((3-4)*5)) = -10

(((2*3)-4)*5) = 10