def vc_count(word):
    if(len(word)==0):
        return [0, 0]
    else:
        output = [0, 0]
        prev = vc_count(word[1:])
        output[0] += prev[0]
        output[1] += prev[1]
        if(isVowel(word[0])):
            output[0] += 1
        else:
            output[1] += 1
        return output


def isVowel(letter):
    return letter in ["a","e","i","o","u","A","E","I","O","U"]

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()
