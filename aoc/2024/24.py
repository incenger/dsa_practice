"""
time python3 24.py
python3 24.py  0.03s user 0.02s system 84% cpu 0.056 total
"""
import collections

SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


class Gate:

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
        return f"Gate(name = {self.name}, value  = {self.value}, inputs = {inputs_repr}, op = {self.op})"


def read_input(file):
    initial = True
    gates = {}
    gate_output = {}
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                initial = False
            elif initial:
                gate_name, value = line.split(":")
                gates[gate_name] = Gate(gate_name, value=int(value))
            else:
                inputs, output_gate_name = map(str.strip, line.split("->"))
                gate_a, op, gate_b = map(str.strip, inputs.split())
                gate_output[(gate_a, gate_b, op)] = output_gate_name

                output_gate = gates.setdefault(output_gate_name,
                                               Gate(output_gate_name))
                gate_a = gates.setdefault(gate_a, Gate(gate_a))
                gate_b = gates.setdefault(gate_b, Gate(gate_b))
                output_gate.op = op
                output_gate.inputs = [gate_a, gate_b]
    return gates, gate_output


def part_1(file):
    gates, _ = read_input(file)
    bits = []
    for gate_name in sorted(gates):
        if gate_name.startswith("z"):
            bits.append(gates[gate_name].output())
    answer = 0
    for idx, val in enumerate(bits):
        answer += val * (1 << idx)
    print("ANSWER", answer)


def full_adder_logic(input_x, input_y, input_carry, gate_output, swapped):
    """
    Full adder logic:
    - X XOR Y -> M (intermediate sum)
    - X AND Y -> N (intermediate carry)
    - C AND M -> R (carry for intermediate sum)
    - C XOR M -> Z (final sum)
    - R OR N  -> C_out (final carry)
    """

    def get_output_gate(input_1, input_2, op):
        return gate_output.get((input_1, input_2, op), None) \
            or gate_output.get((input_2, input_1, op), None)

    M = get_output_gate(input_x, input_y, "XOR")
    N = get_output_gate(input_x, input_y, "AND")

    if input_carry:
        R = get_output_gate(input_carry, M, "AND")
        if not R:
            # There must be intermediate carry
            # If we can't find it, that means the intermediate sum
            # and intermediate carry were swapped
            M, N = N, M
            swapped.extend([M, N])
            R = get_output_gate(input_carry, M, "AND")

        Z = get_output_gate(input_carry, M, "XOR")

        # If any of the intermediates starts with Z, we need to swap
        if M and M.startswith("z"):
            M, Z = Z, M
            swapped.extend([M, Z])

        if N and N.startswith("z"):
            N, Z = Z, N
            swapped.extend([N, Z])

        if R and R.startswith("z"):
            R, Z = Z, R
            swapped.extend([R, Z])

        C_out = get_output_gate(R, N, "OR")
    else:
        Z = M
        C_out = N
    return Z, C_out


def part_2(file):
    gates, gate_output = read_input(file)

    input_x = []
    input_y = []
    output_z = []
    for gate_name in sorted(gates):
        if gate_name.startswith("x"):
            input_x.append(gate_name)
        if gate_name.startswith("y"):
            input_y.append(gate_name)
        if gate_name.startswith("z"):
            output_z.append(gate_name)

    carry = None
    swapped = []
    for x, y in zip(input_x, input_y):

        output_sum, output_carry = full_adder_logic(x, y, carry, gate_output,
                                                    swapped)

        # The last z output does not need x and y inputs
        if output_carry and output_carry.startswith(
                "z") and output_carry != output_z[-1]:
            output_carry, output_sum = output_sum, output_carry
            swapped.extend([output_carry, output_sum])

        carry = output_carry

    print("ANSWER", ",".join(sorted(swapped)))


if __name__ == "__main__":
    part_1(SAMPLE_FILE)
    part_1(INPUT_FILE)
    part_2(INPUT_FILE)
