def has_duplicate(list1):
    for i in range(1, len(list1)):
        tar = list1[i]
        for k in range(0, i):
            if(list1[k]==tar):
                return True
    return False

# This function takes O(N^2) times where N is the number of elements in the list

def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

if __name__ == '__main__':
    main()