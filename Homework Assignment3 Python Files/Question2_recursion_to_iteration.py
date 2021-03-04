def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return 1 + recur(n // 10)

def iterative(n):
    output = 0
    while(n>=10):
        output += 1
        n //= 10
    if(n<0):
        return -1
    elif(n<10):
        return 1 + output


def main():
    print(recur(21512))
    print(recur(9891287412))
    print(recur(-9891287412))
    print(iterative(21512))
    print(iterative(9891287412))
    print(iterative(-9891287412))

if __name__ == '__main__':
    main()