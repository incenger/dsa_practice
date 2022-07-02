"""
x, y, z
x, -y, -z
x, z, -y
x, -y, z

-x, -y, z
-x, y, -z
-x, -z, -y
-x, z, y

Given a coordinate (x, y, z), how can we generate 24 orientations:
It should +-x, +-y, +-z and x, y, z, y, z, x, x, y, y
-x,

Directly store 24 rotation function?
It's actually 24 rotation matrix

We starts with all beacons of the first scanner

for all absolute beacon bi in the first scanner
    For every beacon bj in the second scanner:
        Try map bj with bi  -> The offset vector dij maps bj to bi
        Then we try to map all bj of second scanner to the first scanner coordinate
        If the intersetion is larger than 12 -> Consider it as correct
            The add the new bj


"""
import numpy as np


def gen_rotation_matrix():
    """
    Generate 24 possible facing directions
    Six faces

    x, y, z -> (y, -x, z) ->  (-x, -y, z) -> (-y, x, z) -> (x, y, z)
    x, y, z -> (x, -z, y) ->  (x, -y, -z) -> (x, z, -y)
    """

    def turn_right(matrix):
        """(x, y, z) -> (y,-x, z)"""
        rotated_matrix = matrix.copy()
        rotated_matrix[:, [0, 1]] = rotated_matrix[:, [1, 0]]
        rotated_matrix[:, 1] *= -1

    # 6 facing directions
    FACING_DIRS = [x for i in [-1, 1] for x in [[i, 0, 0], [0, i, 0], [0, 0, i]]]

    rotation_matrix = []
    for face in FACING_DIRS:
        # Select up direction, the position of non-zero column must be different
        face = np.array(face)
        valid_up = [
            f
            for f in FACING_DIRS
            if all(abs(x) != abs(y) for x, y in zip(f, face) if x or y)
        ]
        for up in valid_up:
            up = np.array(up)
            right = np.cross(face, up)

            matrix = np.stack([face, up, right], axis=0)
            rotation_matrix.append(matrix)

    return rotation_matrix


ROTATION_MATRIX = gen_rotation_matrix()


def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()

    scanner_report = []
    current_report = None
    for line in lines:
        line = line.strip()
        if "scanner" in line:
            if current_report:
                scanner_report.append(current_report)
            current_report = []
        elif line:
            coords = list(map(int, line.split(",")))
            current_report.append(coords)

    if current_report:
        scanner_report.append(current_report)
    # Convert to matrix
    scanner_report = [
        np.array(report, dtype=np.int32).reshape(-1, 3) for report in scanner_report
    ]

    return scanner_report


def part_1(scanner_report):
    """
    Move the origin to the first beacon
    """
    found_beacons = set((tuple(coord) for coord in scanner_report[0]))

    scanner_to_check = scanner_report[1:]
    scanner_left = set(range(len(scanner_to_check)))
    scanners = set([(0, 0, 0)])

    while scanner_left:
        print("Remaining scanner", scanner_left)
        print(len(found_beacons))

        # Heuristic: Compare with all found beacons instead of beacons of one scanner
        new_found_beacons = found_beacons.copy()

        for align_to_beacon in found_beacons:
            # For every possible knonw beacon

            for i, scanner_beacon in enumerate(scanner_to_check):
                # For every scanner

                if i not in scanner_left:
                    continue

                for matrix in ROTATION_MATRIX:
                    # For every orientation

                    rotated_scanner_beacon = np.matmul(scanner_beacon, matrix)
                    for align_from_beacon in rotated_scanner_beacon:

                        tx, ty, tz = align_to_beacon
                        fx, fy, fz = align_from_beacon
                        dx, dy, dz = fx - tx, fy - ty, fz - tz

                        # Vector from found to candidate
                        aligned_vector = np.array([dx, dy, dz], dtype=np.int32)
                        aligned_vector = aligned_vector[np.newaxis, ...]
                        aligned_scanner_beacon = rotated_scanner_beacon - aligned_vector
                        aligned_scanner_beacon = set(
                            (tuple(coord) for coord in aligned_scanner_beacon)
                        )

                        intersection = new_found_beacons & aligned_scanner_beacon

                        if len(intersection) >= 12:
                            print("Found")
                            if i in scanner_left:
                                scanner_left.remove(i)
                            scanners.add((tuple([c for c in -aligned_vector[0]])))
                            new_found_beacons.update(aligned_scanner_beacon)
                            break

        found_beacons = new_found_beacons

    # Part 1 -> Return found_beacons

    max_dist = 0

    for sc1 in scanners:
        for sc2 in scanners:
            max_dist = max(sum([abs(c1 - c2) for c1, c2 in zip(sc1, sc2)]), max_dist)

    return max_dist


if __name__ == "__main__":
    scanner_report = read_input("input.txt")
    # found_beacons = part_1(scanner_report)
    max_dist = part_1(scanner_report)
    print(max_dist)
