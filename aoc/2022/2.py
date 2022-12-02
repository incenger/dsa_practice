SHAPE_SCORE = {
    'R': 1,
    'P': 2,
    'S': 3,
}

OUTCOME_SCORE = {
    'L': 0,
    'D': 3,
    'W': 6
}

SHAPE_MAPPING = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

OUTCOME_MAPPING = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}

def outcome(shape_1, shape_2):
    if shape_1 == shape_2:
        return 'D'

    if shape_1 == 'R':
        return 'W' if shape_2 == 'S' else 'L'
    elif shape_1 == 'P':
        return 'W' if shape_2 == 'R' else 'L'
    else:
        return 'W' if shape_2 == 'P' else 'L'

def part_1(input_file):
    score = 0
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        o, y = line.split()
        o = SHAPE_MAPPING[o]
        y = SHAPE_MAPPING[y]
        score += OUTCOME_SCORE[outcome(y, o)] + SHAPE_SCORE[y]

    print(score)



def part_2(input_file):
    score = 0

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        opponent, round_outcome = line.split()
        opponent = SHAPE_MAPPING[opponent]
        round_outcome = OUTCOME_MAPPING[round_outcome]

        for your in 'RPS':
            if outcome(your, opponent) == round_outcome:
                break
        score += SHAPE_SCORE[your] + OUTCOME_SCORE[round_outcome]

    print(score)


if __name__ == "__main__":
    part_1("input.txt")
    part_2("input.txt")
