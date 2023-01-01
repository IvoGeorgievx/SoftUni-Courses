class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.sequence) == self.idx:
            self.idx = 0

        if self.number == 0:
            raise StopIteration

        result = self.sequence[self.idx]
        self.idx += 1
        self.number -= 1
        return result


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
