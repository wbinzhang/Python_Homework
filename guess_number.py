import random

# 构造一个函数判断数字是否正确
def guess_num(num_guess, num_real):
    if num_guess == num_real:
        print('恭喜你，猜对了！')
        return False
    elif num_guess > num_real:
        print('你的数字猜大了，请继续猜测。')
        return True
    else:
        print('你的数字猜小了，请继续猜测。')
        return True

if __name__ == "__main__":
    # 生成一个随机整数
    num_real = int(random.randint(0, 100))
    # print(num_real)
    n = 1
    # 循环判断直到正确
    while True:
        try:
            num_guess = int(input('请猜想并输入一个0-100之间的数字：\n'))
            if 1 <= num_guess <= 100:
                m = guess_num(num_guess, num_real)
                if m == False:
                    break
                # n += 1

            else:
                print('继续游戏，请输入一个100以内的数字。\n')

        except:
            print('继续游戏，请输入0-100之间的数字。\n')

        n += 1

    print('这次游戏，你一共猜测了%d次。' % n)
