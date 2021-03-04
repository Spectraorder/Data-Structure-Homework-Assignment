def pascal(n):
    if(n==1):
        return [[1]]
    else:
        prev = pascal(n-1)
        for i in range(0, len(prev[len(prev)-1])):
            if(i==0):
                output = [1]
            else:
                output.append(prev[len(prev)-1][i] + prev[len(prev)-1][i-1])
            if(i == len(prev[len(prev)-1])-1):
                output.append(1)
        prev.append(output)
        return prev


def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()




