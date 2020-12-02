#Day 2 pt 2

#Answer 342

class password:
    def __init__(self, information):
        self.info = information

        self.first_pos = int(self.info[0:self.info.index('-')])

        self.second_pos = int(self.info[self.info.index('-') + 1: self.info.index(' ')]) 

        self.target = self.info[self.info.index(' ') + 1]

        self.password = self.info[self.info.index(' ') + 4:]
        print(self.password)

        self.valid = False

        if self.password[self.first_pos - 1] == self.target or self.password[self.second_pos - 1] == self.target:
            self.valid = True

        if self.password[self.first_pos - 1] == self.target and self.password[self.second_pos - 1] == self.target:
            self.valid = False
        



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
