"""
 time python3 17.py
python3 17.py  0.02s user 0.02s system 80% cpu 0.053 total
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def get_combo_operand(state, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return state['a']
    elif operand == 5:
        return state['b']
    elif operand == 6:
        return state['c']
    else:
        raise ValueError(f"Unexpected combo operand: {operand}")


def adv(state, operand):
    state['a'] >>= get_combo_operand(state, operand)
    state['ins'] += 2


def bxl(state, operand):
    state['b'] ^= operand
    state['ins'] += 2


def bst(state, operand):
    state['b'] = get_combo_operand(state, operand) % 8
    state['ins'] += 2


def jnz(state, operand):
    if state['a'] == 0:
        state['ins'] += 2
    else:
        state['ins'] = operand


def bxc(state, operand):
    state['b'] ^= state['c']
    state['ins'] += 2


def out(state, operand):
    state['out'].append(get_combo_operand(state, operand) % 8)
    state['ins'] += 2


def bdv(state, operand):
    state['b'] = state['a'] >> get_combo_operand(state, operand)
    state['ins'] += 2


def cdv(state, operand):
    state['c'] = state['a'] >> get_combo_operand(state, operand)
    state['ins'] += 2


OPCODE_MAP = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def read_input(file):
    registers = []
    program = []
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            val = line.split(":")[-1]
            if line.startswith("Register"):
                registers.append(int(val))
            else:
                program = list(map(int, val.split(",")))
    return registers, program


def part_1(file):
    registers, program = read_input(file)
    program_state = {'ins': 0, 'out': []}
    for name, val in zip("abc", registers):
        program_state[name] = val

    while program_state['ins'] < len(program):
        opcode = program[program_state['ins']]
        operand = program[program_state['ins'] + 1]
        OPCODE_MAP[opcode](program_state, operand)

    print("ANSWER:", ",".join(map(str, program_state['out'])))


def part_2(file):
    """
    The program uses the jump instruction to make a loop, and ends with a == 0.
    In each loop, a is shifted right by 3 bits.
    Each output value is determined soley by the value of a.
    We can do backward search to construct a (forward search won't work because we need the actual value of a).
    """
    registers, program = read_input(file)

    def compute_output(a):
        # b = a % 8
        # b = b ^ 6
        # c = a >> b
        # b = b ^ c
        # b = b ^ 7
        # a = a >> 3
        # out(b % 8)
        b = (a % 8) ^ 6
        c = a >> b
        out = (b ^ c ^ 7) % 8
        return out

    # BFS search
    # Because each value is determined by a and its last 3 bits
    # We need to do backward search
    answer = float('inf')
    queue = collections.deque([(0, len(program) - 1)])

    while queue:
        current_a, idx = queue.popleft()
        if idx == -1:
            answer = min(current_a, answer)
        else:
            for a_last_3_bits in range(8):
                next_a = (current_a << 3) + a_last_3_bits
                if compute_output(next_a) == program[idx]:
                    queue.append((next_a, idx - 1))

    if answer != float('inf'):
        program_state = {'ins': 0, 'out': []}
        for name, val in zip("abc", registers):
            program_state[name] = val
        program_state['a'] = answer
        while program_state['ins'] < len(program):
            opcode = program[program_state['ins']]
            operand = program[program_state['ins'] + 1]
            OPCODE_MAP[opcode](program_state, operand)

        if program_state['out'] == program:
            print("ANSWER", answer)


if __name__ == "__main__":
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
