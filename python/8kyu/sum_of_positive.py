# Sum of positive
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

print(positive_sum([1, 2, 3]))

def positive_sum2(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum2([10, 11, 12]))