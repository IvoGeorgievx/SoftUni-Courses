number = int(input())
negatives = list()
positives = list()
positive_count = 0
negative_sum = 0

for i in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
        positive_count += 1
    else:
        negatives.append(current_number)
        negative_sum += current_number
print(positives)
print(negatives)
print(f'Count of positives: {positive_count}')
print(f'Sum of negatives: {negative_sum}')