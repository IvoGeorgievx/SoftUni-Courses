def result(*args):
    positive_sum = 0
    negative_sum = 0
    for i in args:
        if i < 0:
            negative_sum += i
        else:
            positive_sum += i
    return positive_sum, negative_sum


nums = [int(x) for x in input().split()]
positive_sum, negative_sum = result(*nums)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")