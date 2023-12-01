lines = open("../inputs/day01.txt").readlines()

NUMBERS = [
    "zero",  # padding so the index of one becomes 1 instead of 0
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


part1 = 0
part2 = 0

for line in lines:
    digits = [c for c in line if c.isdigit()]
    part1 += int(digits[0] + digits[-1])

    part2_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            part2_digits.append(c)
        for digit, word in enumerate(NUMBERS):
            if line[i:].startswith(word):
                part2_digits.append(str(digit))
    part2 += int(part2_digits[0] + part2_digits[-1])


print(part1)
print(part2)
