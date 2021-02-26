def largest_ten(list1):
    output = []
    for i in range(0, len(list1)):
        if(len(output)==10):
            tar = list1[i]
            for k in range(0, len(output)):
                if(tar>output[k]):
                    output[k], tar = tar, output[k]
        else:
            output.append(list1[i])
    return output

def main():
    print(largest_ten([9,8,6,4,22,68,96,212,52,12,6,8,99]))

    print(largest_ten([42,10,90,75,79,98,11,90,92,11,21,8,47,72,25,94,99,54,69,60]))

if __name__ == '__main__':
    main()
    
