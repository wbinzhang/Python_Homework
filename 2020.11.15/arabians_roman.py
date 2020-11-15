# coding: utf-8
"""
编写一个类，用阿拉伯数字实例化后，可以得到相应的罗马数字
程序实现1-4000之间的阿拉伯数字的转换
"""

class Ara_Roman:
    def __init__(self):
        self.Roman = {
                    0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
                    1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
                    2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
                    3:("","M","MM","MMM")
                    }
        self.roman = ''

    def ara_Roman(self, ara_num):
        if not 0 < ara_num < 4000 and not int(ara_num) == ara_num:              # 当ara_num不符合条件时
            print('输入数字有误，请输入一个大于0，小于4000的整数')

        else:
            self.roman += self.Roman[3][int(ara_num/1000%10)]
            self.roman += self.Roman[2][int(ara_num/100%10)]
            self.roman += self.Roman[1][int(ara_num/10%10)]
            self.roman += self.Roman[0][int(ara_num%10)]
            return self.roman

if __name__ == '__main__':
    ara_roma = Ara_Roman()             # 实例化Ara_Roman
    print('-'*8,'阿拉伯数字转化罗马数字','-'*8)
    while True:
        ara_num = input('请输入一个大于0，小于4000的整数:\n')
        try:
            rom_num = ara_roma.ara_Roman(float(ara_num))
            print(f'阿拉伯数字【{ara_num}】对应的罗马数字为：{rom_num}')
            if input('是否继续转换（y/n):\n') == 'y':
                continue
            else:
                print('游戏结束！')
                break
        except:
            print('输入数字有误，请输入一个大于0，小于4000的整数')

