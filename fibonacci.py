# coding: utf-8
"""
使用迭代器、生成器、矩阵三种方法实现斐波那契数列
"""

import numpy as np              # 导入numpy，在使用矩阵实现时使用

'''
使用迭代器实现斐波那契数列
定义迭代器实现斐波那契数列的类
'''
class IterFibonacci(object):
    def __init__(self, iter_out_num=10):                # 初始化变量
        self.val_1 = 0              # 定义斐波那契数列的第一个数
        self.val_2 = 1              # 定义斐波那契数列的第二个数
        self.out_num = iter_out_num             # 定义输入的斐波那契数列的长度
        self.now_num = 0                # 定义计算斐波那契数的次数
    
    def __iter__(self):             # 定义迭代器对象
        return self

    def __next__(self):             # 定义next方法
        while True:
            if self.now_num == 0:               # 判断第一次计算，输出斐波那契数列的第一个数（0）
                self.now_num += 1               # 计算次数加1
                return self.val_1   
            
            elif self.now_num < self.out_num:               # 计算斐波那契数列，指导达到输出个数要求
                self.now_num += 1               # 计算次数加1
                self.val_1, self.val_2 = self.val_2, self.val_1 + self.val_2                # 计算斐波那契数列，第三个数等于前两个数的和
                return self.val_1
            
            else:
                raise StopIteration             # 斐波那契数列个数达到输出要求后，停止计算


'''
使用生成器实现斐波那契数列
定义生成器实现斐波那契数列的类
'''
class GenFibonacci(object):
    def __init__(self, gen_out_num=10):             # 初始化变量
        self.val_1 = 0              # 定义斐波那契数列的第一个初始值
        self.val_2 = 1              # 定义斐波那契数列的第二个初始值
        self.out_num = gen_out_num              # 定义输出斐波那契数列的个数
        self.now_num = 0                # 定义计算斐波那契数列的次数
        
    def gen_creat_fibonacci(self):              # 定义生成器计算斐波那契数列的函数
        while True:
            if self.now_num == 0:               # 判断第一次计算，输出斐波那契数列的第一个数（0）
                self.now_num += 1               # 计算次数加1
                yield self.val_1                # 生成器yield返回结果
            elif self.now_num < self.out_num:               # 计算斐波那契数列，直到达到输出个数要求
                self.val_1, self.val_2 = self.val_2, self.val_1 + self.val_2                # 计算斐波那契数列，第三个数等于前两个数的和
                self.now_num += 1               # 计算次数加1
                yield self.val_1
            else:
                break               # 斐波那契数列个数达到输出要求后，停止计算


'''
使用矩阵实现斐波那契数列
定义矩阵实现斐波那契数列的类
'''
class MatFibonacci(object):
    def __init__(self, gen_out_num=10):             # 初始化变量
        self.creat_matrix = np.array([1,0])             # 定义初始向量[1,0]
        self.default_matrix = np.array([[1,1],[1,0]])               # 定义参数矩阵
        self.out_num = gen_out_num              # 定义输出斐波那契数列的个数
        self.now_num = 0                # 定义计算斐波那契数列的个数

    def mat_creat_fibonacci(self):              # 定义矩阵计算斐波那契数列的函数
        while True:
            if self.now_num == 0:               # 判断第一次计算，输出斐波那契数列的第一个数（0）
                self.now_num += 1               # 计算次数加1
                yield self.creat_matrix[1]              # yield返回斐波那契数列的第一个数
            elif self.now_num < self.out_num:               # 计算斐波那契数列，直到达到输出个数要求
                self.creat_matrix = np.dot(self.default_matrix, self.creat_matrix)              # 计算斐波那契数列
                self.now_num += 1               # 计算次数加1
                yield self.creat_matrix[1]              # yield返回斐波那契数列的值
            else:
                break               # 斐波那契数列个数达到输出要求后，停止计算


def main(out_num=10):
    '''使用迭代器实现斐波那契数列'''
    iter_fibonacci = IterFibonacci(out_num)
    print('使用迭代器计算得到的斐波那契数列为：')
    for num in iter_fibonacci:
        print(num, end=' ')

    '''使用生成器实现斐波那契数列'''
    gen_fibonacci = GenFibonacci(out_num)
    print('\n使用生成器计算得到的斐波那契数列为：')
    for num in gen_fibonacci.gen_creat_fibonacci():
        print(num, end=' ')

    '''使用矩阵实现斐波那契数列'''
    mat_fibonacci = MatFibonacci(out_num)
    print('\n使用矩阵计算得到的斐波那契数列为：')
    for num in mat_fibonacci.mat_creat_fibonacci():
        print(num, end=' ')


if __name__ =='__main__':
    while True:
        try:
            out_num = input('请输入想要获取斐波那契数列的个数:\n')
            if int(out_num) > 0 and out_num.isdigit():
                main(int(out_num))
                break
            else:
                print('请输入一个正整数，再试一次')

        except:
            print('请输入数字,再试一次')




