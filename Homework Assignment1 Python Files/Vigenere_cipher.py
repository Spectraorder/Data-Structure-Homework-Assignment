def vigenere_encrypt(plain, key):
    outString = ''
    key = sameLen(plain, key)
    k = 0
    while(k<len(plain)):
        pos = (ord(plain[k]) + ord(key[k]) - 2 * ord('A')) % 26
        outString += chr(pos + ord('A'))
        k += 1
    return outString

def vigenere_decrypt(cipher, key):
    outString = ''
    key = sameLen(cipher, key)
    i = 0
    while(i<len(cipher)):
        pos = (ord(cipher[i]) - ord(key[i])) % 26
        outString += chr(pos + ord('A'))
        i += 1
    return outString

def sameLen(String, key):
    if(len(key)>len(String)):
        key = key[:len(String)]
    else:
        diff = len(String) - len(key)
        i = 0
        while(i<diff):
            key += key[(i%len(key))]
            i += 1
    return key

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

if __name__ == '__main__':
    main()
