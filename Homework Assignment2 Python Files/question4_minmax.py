def minmax(list1):
    minL = list1[0]
    maxL = list1[0]
    for i in range(1, len(list1), 2):
        x = list1[i]
        if(i+1<len(list1)):
            y = list1[i+1]
        else:
            y = x
        if(x>=y):
            smallCan, largeCan = y, x
        else:
            smallCan, largeCan = x, y
        minL = min(smallCan, minL)
        maxL = max(largeCan, maxL)
    return (minL, maxL)


def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

if __name__ == '__main__':
    main()