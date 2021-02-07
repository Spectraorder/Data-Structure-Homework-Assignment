def number_of_times_divideby2(n):
    count = 0
    while(n>=2):
        n //= 2
        count += 1
    return count

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    print(number_of_times_divideby2(1000))   # 9
    print(number_of_times_divideby2(999))    # 9 
    print(number_of_times_divideby2(467382987338298))   # 48

if __name__ == '__main__':
    main()
