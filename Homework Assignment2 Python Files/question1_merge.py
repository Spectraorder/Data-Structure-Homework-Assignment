def merge(I1, I2):
    output = []
    for i in I1:
        output.append(i)
    k = 0
    while(k<len(I2)):
        output.insert(2*k+1,I2[k])
        k += 1
    return output

def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))])
    print([i for i in merge(range(1),range(100,105))])

if __name__ == '__main__':
    main()