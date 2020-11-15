# coding: utf-8
"""
编写一个类，整理常见的概率分布
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class Common_Probability:
    def __init__(self):
        self.rng = np.random.default_rng()               # 构造一个默认位生成器

    '''均匀分布'''
    def uniform(self, low=-1, high=1, size=10):
        random_num = self.rng.uniform(low, high, size)
        return random_num

    '''标准正太分布'''
    def standard_normal(self, size=10):
        random_num = self.rng.standard_normal(size)
        return random_num

    '''正太分布'''
    def normal(self, miu=0, sigma=1, size=10):
        random_num = self.rng.normal(miu, sigma, size)
        return random_num

    '''二项分布'''
    def binomial(self, n=100, p=0.5, size=10):
        random_num = self.rng.binomial(n, p, size)
        return random_num

    '''卡方分布'''
    def chisquare(self, df=2, size=10):
        random_num = self.rng.chisquare(df, size)
        return random_num

    '''指数分布'''
    def exponential(self, lam=1, size=10):
        random_num = self.rng.exponential(lam, size)
        return random_num

    '''F分布'''
    def F(self, dfnum=2, dfden=2, size=10):
        random_num = self.rng.f(dfnum, dfden, size)
        return random_num

    '''伽马分布'''
    def gamma(self, shape=2, scale=2, size=3):
        random_num = self.rng.gamma(shape, scale, size)
        return random_num

    '''贝塔分布'''
    def beta(self, a=0.5, b=0.5, size=10):
        random_num = self.rng.beta(a, b, size)
        return random_num

    '''几何分布'''
    def geometric(self, p=0.2, size=10):
        random_num = self.rng.geometric(p, size)
        return random_num

    '''逻辑斯蒂分布'''
    def logistic(self, loc=10, scale=1, size=10):
        random_num = self.rng.logistic(loc, scale, size)
        return random_num

    '''泊松分布'''
    def poisson(self, lam=5, size=3):
        random_num = self.rng.poisson(lam, size)
        return random_num

    '''学生t分布'''
    def standard_t(self, df=10, size=10):
        random_num = self.rng.standard_t(df, size)
        return random_num

    def statistic_quantity(self, data):
        # data = np.array(data)
        '''计算均值'''
        data_mean = np.mean(data)
        '''计算方差'''
        data_var = np.var(data)
        '''计算标准差'''
        data_std = np.std(data)
        '''计算极差'''
        data_range = np.ptp(data)

        return  data_mean, data_var, data_std, data_range



if __name__ == '__main__':
    com_pro = Common_Probability()              # 实例化
    '''生成均匀分布的随机数'''
    uni_num = com_pro.uniform(low=-2, high=2, size=10)    # 生成均匀分布随机数
    data_mean, data_var, data_std, data_range = com_pro.statistic_quantity(uni_num)    #计算生成的随机数的均值、方差、标准差和极差
    print(f'生成的均匀分布的随机数为：\n{uni_num}')
    print(f'生成的均匀分布随机数的均值为：{data_mean}, 方差为：{data_var}, 标准差为：{data_std}, 极差为：{data_range}')

    '''生成标准正太分布的随机数'''
    st_norm_num = com_pro.standard_normal(20)
    st_data_mean, st_data_var, st_data_std, st_data_range = com_pro.statistic_quantity(st_norm_num)  # 计算生成的随机数的均值、方差、标准差和极差
    print(f'生成的标准正太分布的随机数为：\n{st_norm_num}')
    print(f'生成的标准正太分布随机数的均值为：{st_data_mean}, 方差为：{st_data_var}, 标准差为：{st_data_std}, 极差为：{st_data_range}')




