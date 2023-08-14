class Test1:
    # 将n个盘子从1移动到3,2作为缓冲
    def move(self, n, one, two, three):
        # 如果只有一个盘子，那么直接从起始柱子挪到目标柱子
        if n == 1:
            print(f'将1个盘子从{one}移动到{three}')
            return
        # 否则，先将n-1个盘子，从1挪到2,3作为缓冲
        self.move(n-1, one, three, two)
        # 将第一个盘子从1移动到3
        self.move(1, one, two, three)
        # 再将n-1个柱子从2移动到3,1作为缓冲
        self.move(n-1, two, one, three)


if __name__ == '__main__':
    test = Test1()
    test.move(3, 1, 2, 3)