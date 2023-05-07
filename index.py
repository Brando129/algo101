# Create a function that replaces any negative numbers with at zero.

def replace_negatives(list):

    for i in range(0,len(list)):
        if list[i] < 0:
            list[i] = 0

    return list

print(replace_negatives([2,1,-1,-2,1]))