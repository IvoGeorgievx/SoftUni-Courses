class vowels:
    vowels_chars = 'aeouyi'

    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.word):
            if self.word[self.index].lower() not in self.vowels_chars:
                self.index += 1
                continue
            value_to_return = self.word[self.index]
            self.index += 1
            return value_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)