def minmax(list1):
    smallCan = []
    largeCan = []
    for i in range(0, len(list1)):
        if(i%2==0):
            largeCan.append(list1[i])
        else:
            smallCan.append(list1[i])
    if(len(smallCan)==len(largeCan)):
        minL = smallCan[0]
        maxL = largeCan[0]
        for i in range(0, len(smallCan)):
            minL = min(smallCan[i], largeCan[i])
            maxL = max(smallCan[i], largeCan[i])
    return '(' + str(minL) + ', '+ str(maxL) + ')'


def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

if __name__ == '__main__':
    main()