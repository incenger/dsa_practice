"""
"""

import threading
import multiprocessing

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
    state['a'] = int(state['a'] / 2**get_combo_operand(state, operand))
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
    state['b'] = int(state['a'] / 2**get_combo_operand(state, operand))
    state['ins'] += 2


def cdv(state, operand):
    state['c'] = int(state['a'] / 2**get_combo_operand(state, operand))
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
    registers, program = read_input(file)
    # Heuristic for the first value
    # b = a % 8
    # b ^= 6
    # c = a // 2**b
    # b ^= c
    # b ^= 7
    # a = a // 2**3
    # out(b % 8) == 2
    register_a = 1
    while True:
        program_state = {'ins': 0, 'out': []}
        for name, val in zip("abc", registers):
            program_state[name] = val

        program_state['a'] = register_a
        while program_state['ins'] < len(program):
            opcode = program[program_state['ins']]
            operand = program[program_state['ins'] + 1]
            OPCODE_MAP[opcode](program_state, operand)

            out_idx = len(program_state['out']) - 1
            if out_idx >= 0 and program_state['out'][out_idx] != program[
                    out_idx]:
                break
        if program_state['ins'] == len(
                program) and program_state['out'] == program:
            break
        register_a += 1
    print("ANSWER:", register_a)


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    # part_2(SAMPLE_FILE)
    # part_2(INPUT_FILE)
