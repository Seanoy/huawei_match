import numpy as np
import threading
from collections import deque


# 处理每条转账记录
# index1是确认有没有人给A转账，有人转账给他就B插入到A的后面
# index2是确认存不存在这条记录，如果不存在
def loop(part, record):
    # print(part)
    # index1 = np.argwhere(record == part[0])
    # index2 = np.argwhere(record == part[1])
    # print(index1, index2)

    return


if __name__ == "__main__":
    # 打开文件
    filename = "./data/test_data1.txt"
    count = 0  # 记录符合条件的循环转账
    # result存储所有符合条件的转账记录
    # record存储所有链接信息
    # 最多7条转账记录，用于存储ID，第0位用作哨兵，bit==1则表示成环
    result = records = zero = np.zeros(8, dtype=int)
    try:
        with open(filename, mode='r') as file:
            for line in file:
                # ((line[0:-1]))
                line = line.strip().split(',')[0:-1]
                loop(line, records)
                print(np.argwhere(line == '175'))

    except IOError:
        print("open file %s failed" % filename)
