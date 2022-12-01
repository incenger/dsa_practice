
def part_1(input_file):
    calories = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    calo = 0
    for line in lines:
        line = line.strip()
        if not line:
            calories.append(calo)
            calo = 0
        else:
            calo += int(line)
    print(max(calories))


def part_2(input_file):
    calories = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    calo = 0
    for line in lines:
        line = line.strip()
        if not line:
            calories.append(calo)
            calo = 0
        else:
            calo += int(line)

    calories.sort(reverse=True)
    print(sum(calories[:3]))

if __name__ == "__main__":
    part_1("input.txt")
    part_2("input.txt")

