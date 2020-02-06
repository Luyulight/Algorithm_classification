def bubble_sort(seq):
    '''
    n-1-i轮小循环，每次完成一个数的冒泡,把最大的数放在最后
    n-1轮大循环，冒泡n-1个数
    '''
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if(seq[j] > seq[j+1]):
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
