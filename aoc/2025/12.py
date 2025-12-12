SAMPLE_FILE = "sample.txt"
INPUT_FILE = "input.txt"


def read_input(file):
    shapes = []
    regions = []
    with open(file, "r") as f:
        shape = []
        shape_idx = -1
        is_reading_shape = False
        for line in f.readlines():
            line = line.strip()
            if is_reading_shape:
                if line:
                    shape.append(line)
                else:
                    assert shape_idx == len(shapes)
                    shapes.append(shape)
                    is_reading_shape = False
                    shape = []
            elif line.endswith(":"):
                shape_idx = int(line[:-1])
                is_reading_shape = True
            elif line:
                region_area, shape_quantity = line.split(":")
                shape_quantity = list(map(int, shape_quantity.strip().split()))
                region_height, region_width = list(
                    map(int, region_area.split("x")))
                regions.append((region_height, region_width, shape_quantity))
    return shapes, regions


def get_area(shape):
    area = 0
    for row in shape:
        area += row.count("#")
    return area


def part_1(file):
    shapes, regions = read_input(file)
    shapes_area = [get_area(shape) for shape in shapes]
    answer = 0
    for height, width, shapes_quantity in regions:
        region_area = height * width
        total_shapes_area = sum(
            area * quantity
            for quantity, area in zip(shapes_quantity, shapes_area))
        if total_shapes_area <= region_area:
            answer += 1
    print(f"Part 1: {answer}")


if __name__ == "__main__":
    part_1(INPUT_FILE)
