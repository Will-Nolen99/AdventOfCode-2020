#Day 2 pt 1

#Answer 458

class password:
    def __init__(self, information):
        self.info = information

        self.lower = int(self.info[0:self.info.index('-')]) + 1

        self.upper = int(self.info[self.info.index('-') + 1: self.info.index(' ')]) + 1

        self.target = self.info[self.info.index(' ') + 1]

        self.count = self.info.count(self.target)

        self.valid = self.count >= self.lower and self.count <= self.upper




passwords = []
lines = []


with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]


passwords = [password(line) for line in lines]

count = 0

for psd in passwords:
    if psd.valid:
        count += 1

print("Valid passowrds: ", count)
