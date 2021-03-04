def power(x,n):
    if(n==0):
        return 1
    elif(n>0):
        partial = power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result
    elif(n<0):
        return 1/power(x, -n)

def main():
    print(power(-2, 4))     # 16
    print(power(4, 3))      # 64
    print(power(-2, -3))# -0.125

if __name__ == '__main__':
    main()

