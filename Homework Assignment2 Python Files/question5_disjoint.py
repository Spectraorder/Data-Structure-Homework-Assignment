def three_way_disjoint(l1, l2, l3):
    l1.sort()
    l2.sort()
    l3.sort()
    inter12 = intersect(l1, l2)
    inter23 = intersect(l2, l3)
    interAll = intersect(inter12, inter23)
    if(interAll==[]):
        return True
    else:
        return False

def intersect(list1, list2):
    output = []
    if((list1==[])|(list2==[])):
        return output
    else:
        if((list1[len(list1)-1]>=list2[0])):
            if(list2[len(list2)-1]<list1[0]):
                return output
            else:
                for i in range(0, len(list2)):
                    if(list2[i]>list1[len(list1)-1]):
                        break
                    else:
                        try:
                            pos = list1.index(list2[i])
                            output.append(list1[pos])
                        except:
                            continue
    return output

def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10,11,12]
    l3 = [5,13,14,15,16]
    l4 = [5,6,7,8,9,10,11]

    print(three_way_disjoint(l1,l2,l3))   # True, yes three way disjoint.
    print(three_way_disjoint(l1,l4,l3))   # False, not three way disjoint.

if __name__ == '__main__':
    main()
