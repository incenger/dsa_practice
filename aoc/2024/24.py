"""
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


class Wire:

    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.inputs = None
        self.op = None

    def output(self):
        if self.value is None:
            if self.op == 'AND':
                self.value = self.inputs[0].output() & self.inputs[1].output()
            elif self.op == 'XOR':
                self.value = self.inputs[0].output() ^ self.inputs[1].output()
            elif self.op == "OR":
                self.value = self.inputs[0].output() | self.inputs[1].output()
            else:
                raise ValueError("Unexpected op:", self.op)
        return self.value

    def __repr__(self):
        if self.inputs:
            inputs_repr = str(tuple(wire.name for wire in self.inputs))
        else:
            inputs_repr = None
        return f"Wire(name = {self.name}, value  = {self.value}, inputs = {inputs_repr}, op = {self.op})"


def read_input(file):
    initial = True
    wires = {}
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                initial = False
            elif initial:
                wire_name, value = line.split(":")
                wires[wire_name] = Wire(wire_name, value=int(value))
            else:
                inputs, output_wire_name = map(str.strip, line.split("->"))
                output_wire = wires.setdefault(output_wire_name,
                                               Wire(output_wire_name))
                wire_a, op, wire_b = map(str.strip, inputs.split())
                wire_a = wires.setdefault(wire_a, Wire(wire_a))
                wire_b = wires.setdefault(wire_b, Wire(wire_b))
                output_wire.op = op
                output_wire.inputs = [wire_a, wire_b]
    return wires


def part_1(file):
    wires = read_input(file)
    bits = []
    for wire_name in sorted(wires):
        if wire_name.startswith("z"):
            bits.append(wires[wire_name].output())
    answer = 0
    for idx, val in enumerate(bits):
        answer += val * (1 << idx)
    print("ANSWER", answer)


def part_2(file):
    pass


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    # part_2(SAMPLE_FILE)
    # part_2(INPUT_FILE)
