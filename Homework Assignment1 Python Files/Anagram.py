def anagram(string1, string2):
    proString1 = eraseSpace(string1)
    proString2 = eraseSpace(string2)
    if(len(proString1)!=len(proString2)):
        return False
    else:
        check = [None] * len(proString1)
        i = 0
        while(i<len(proString1)):
            pos = proString2.index(proString1[i])
            if(check[pos]!=True):
                check[pos] = True
                proString2 = proString2[:pos] + ' '+ proString2[pos+1:]
            else:
                return False
            i += 1
        return True

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def eraseSpace(string):
    outString = ''
    i = 0;
    while(i<len(string)):
        if(string[i]!=' '):
            outString += string[i]
        i += 1
    return outString


def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))

if __name__ == '__main__':
    main()
