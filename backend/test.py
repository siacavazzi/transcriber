# Written in python

test1 = [0,5,5,2]
test2 = [0,4,3,1,2,3,4,0]

def maxPair(array):
    maxSum = 0
    index = [0,0]
    for i in range(0, len(array)):
        if (i + 1) < len(array):
            currSum = array[i] + array[i+1]
            if currSum > maxSum:
                maxSum = currSum
                index[0] = i
                index[1] = i+1
    return index

print(maxPair(test2))
