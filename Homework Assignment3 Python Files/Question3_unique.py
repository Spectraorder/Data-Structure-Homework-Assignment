def unique(s):
    if(len(s)==1):
        return True
    else:
        if(s[0] in s[1:]):
            return False
        else:
            return unique(s[1:])

def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True

if __name__ == '__main__':
    main()

