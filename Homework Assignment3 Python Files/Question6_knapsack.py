import copy

def knapsack_driver(capacity, weights, outList=[], allList=[[]]):
    allSum = sum(outList)
    if(allSum==capacity):
        allList.append(outList)
    if(allSum>=capacity):
        return
    for i in range(0, len(weights)):
        knapsack_driver(capacity, weights[i+1:], outList+[weights[i]],allList)
    return clearList(allList)

# add first digit from the weights to find outList
# def addFirstToCap(capacity, weights, outList=[]):
#     allSum = sum(outList)
#     if(allSum==capacity):
#         print(outList)
#     if(allSum>=capacity):
#         return
#     for i in range(0, len(weights)):
#         addFirstToCap(capacity, weights[i+1:], outList+[weights[i]])

# clears null subsets in the 2D array
def clearList(prev):
    for i in range(0, len(prev)-1):
        if(prev[i]==[]):
            prev.__delitem__(i)
    return prev

def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    # print(knapsack_driver(14, casts))
    print(knapsack_driver(14, casts))
if __name__ == '__main__':
    main()

