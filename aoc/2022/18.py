CONNECTED_DISPLACEMENT = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]


def part_1(input_file):
    """For each cube, check each side (6 in total) and count"""
    with open(input_file, "r") as f:
        cubes = set(
            [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
        )

    total_surface_area = 0
    for cube in cubes:
        x, y, z = cube
        cube_surface_area = 6

        for dx, dy, dz in CONNECTED_DISPLACEMENT:
            if (x + dx, y + dy, z + dz) in cubes:
                cube_surface_area -= 1

        total_surface_area += cube_surface_area

    print("Part 1", total_surface_area)


def part_2(input_file):
    """Filling water to the whole space. The check surface touching the water."""
    with open(input_file, "r") as f:
        lava_cubes = set(
            [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
        )

    # Fill water, x, y, z is small enough for brute force
    xmin, xmax, ymin, ymax, zmin, zmax = (
        float("inf"),
        float("-inf"),
        float("inf"),
        float("-inf"),
        float("inf"),
        float("-inf"),
    )

    for x, y, z in lava_cubes:
        xmin = min(x - 1, xmin)
        ymin = min(y - 1, ymin)
        zmin = min(z - 1, zmin)

        xmax = max(x + 1, xmax)
        ymax = max(y + 1, ymax)
        zmax = max(z + 1, zmax)

    queue = [(xmin, ymin, zmin)]
    water_cubes = set(queue)
    while queue:
        next_queue = []

        for water_cube in queue:
            x, y, z = water_cube
            for dx, dy, dz in CONNECTED_DISPLACEMENT:
                nx, ny, nz = x + dx, y + dy, z + dz
                next_water_cube = (nx, ny, nz)

                if (
                    xmin <= nx <= xmax
                    and ymin <= ny <= ymax
                    and zmin <= nz <= zmax
                    and next_water_cube not in water_cubes
                    and next_water_cube not in lava_cubes
                ):
                    next_queue.append(next_water_cube)
                    water_cubes.add(next_water_cube)

        queue = next_queue

    total_surface_area = 0

    for point in lava_cubes:
        x, y, z = point
        cube_surface_area = 0

        for dx, dy, dz in CONNECTED_DISPLACEMENT:
            if (x + dx, y + dy, z + dz) in water_cubes:
                cube_surface_area += 1

        total_surface_area += cube_surface_area

    print("Part 2", total_surface_area)


if __name__ == "__main__":
    part_1("input.txt")
    part_2("input.txt")
