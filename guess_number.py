import random

# 构造一个函数判断数字是否正确
def guess_num(num_guess, num_real):
    if num_guess == num_real:
        print('恭喜你，猜对了！')
        return 0
    elif num_guess > num_real:
        print('你的数字猜大了，请继续猜测。')
        return 1
    else:
        print('你的数字猜小了，请继续猜测。')
        return 1

if __name__ == "__main__":
    # 生成一个随机整数
    num_real = int(random.randint(0,100))
    # print(num_real)
    m = 1
    n = 0
    # 循环判断指导正确
    while m > 0:     # 可以去掉这个条件，改为 True，然后在guess_num返回值为Flase时，使用break终止循环。
        num_guess = int(input('请猜想并输入一个0-100之间的数字：\n'))
        if 1 <= num_guess <= 100:
            m = guess_num(num_guess, num_real)
            n += 1

        else:
            print('重新开始游戏，请输入一个100以内的数字。\n')

    print('这次游戏，你一共猜测了%d次。' % n)
