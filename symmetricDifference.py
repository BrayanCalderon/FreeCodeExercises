
def operation(set1,set2):
    resultSet = []
    nonValid = -1
    while set1 and set2:
        if set1 and set2:
            if set1[0] == set2[0]:
                set1.pop(0)
                nonValid = set2.pop(0)
            else:
                if set1[0] > set2[0]:
                    if set2[0] == nonValid:
                        set2.pop(0)
                    else:
                        resultSet.append(set2.pop(0))
                else:
                    if set1[0] == nonValid:
                        set1.pop(0)
                    else:
                        resultSet.append(set1.pop(0))
    if set1:
        while set1:
            if set1[0] == nonValid:
                set1.pop(0)
            else:
                newValue = set1.pop(0)
                resultSet.append(newValue)
                nonValid = newValue
                
    if set2:
        while set2:
            if set2[0] == nonValid:
                set2.pop(0)
            else:
                newValue = set2.pop(0)
                resultSet.append(newValue)
                nonValid = newValue
    return resultSet




def sym(sets):
    currentSet = []
    while sets:
        nextSet = sorted(sets.pop(0))
        currentSet = operation(currentSet,nextSet)    
    return currentSet
        


print(sym([[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]))