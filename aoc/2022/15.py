import re


def l1_distance(x0, y0, x1, y1):
  return abs(x1 - x0) + abs(y1 - y0)


def intersect(y, sensor, radius):
  """Compute the intersection between a horizontal line with the non-beacon area around a sensor.
  """
  x0, y0 = sensor
  if abs(y - y0) >= radius:
    # The line doesn't intersect with or just "touches" the non-beacon area.
    return []
  # |x - x0| + |y - y0| = radius
  # |x - x0| = radius - |y - y0|
  #  x = radius  - |y - y0| + x0 or x = |y - y0| - radius + x0
  x_intersections = [abs(y - y0) - radius + x0, radius - abs(y - y0) + x0]
  x_intersections.sort()
  return x_intersections


def segment_length(segment):
  return 1 + segment[1] - segment[0]


def part_1():
  """Solving part 1, not too slow solution.

  Ideas:
  - Find the intersection segment between the horizontal line with the
  non-beacon
  area around each sensor
  - Given all the segments, compute their union length.
  """
  with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]
    locations = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

  sensors = []
  beacons = []
  sensor_beacon_dist = []
  for x0, y0, x1, y1 in locations:
    sensors.append((x0, y0))
    beacons.append((x1, y1))
    sensor_beacon_dist.append(l1_distance(x0, y0, x1, y1))

  beacons_set = set(beacons)
  fixed_y = 2000000

  intersection_segment = []
  for sensor, radius in zip(sensors, sensor_beacon_dist):
    intersections = intersect(fixed_y, sensor, radius)
    if not intersections:
      continue

    segment_start, segment_end = intersections[0], intersections[1]
    if (intersections[0], fixed_y) in beacons_set:
      segment_start += 1
    if (intersections[1], fixed_y) in beacons_set:
      segment_end -= 1
    intersection_segment.append((segment_start, segment_end))

  assert intersection_segment
  intersection_segment.sort()
  non_beacon_cnt = segment_length(intersection_segment[0])
  prev_segment = intersection_segment[0]

  for i in range(1, len(intersection_segment)):
    cur_segment = intersection_segment[i]

    # Check if current segment intersect with previous segment
    if prev_segment[1] >= cur_segment[0]:
      union_segment = (
          min(prev_segment[0], cur_segment[0]),
          max(prev_segment[1], cur_segment[1]),
      )
      non_beacon_cnt -= segment_length(prev_segment)
      non_beacon_cnt += segment_length(union_segment)
      prev_segment = union_segment
    else:
      non_beacon_cnt += segment_length(cur_segment)
      prev_segment = cur_segment

  print("Part 1:", non_beacon_cnt)


def part_2():
  """Sweeping line. Takes around 1 minute to run."""
  with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]
    locations = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

  sensors = []
  beacons = []
  sensor_beacon_dist = []
  for x0, y0, x1, y1 in locations:
    sensors.append((x0, y0))
    beacons.append((x1, y1))
    sensor_beacon_dist.append(l1_distance(x0, y0, x1, y1))

  distress_beacon = None

  for y in range(4000001):
    intersection_segment = []
    for sensor, radius in zip(sensors, sensor_beacon_dist):
      intersections = intersect(y, sensor, radius)
      if intersections:
        intersection_segment.append(intersections)

    intersection_segment.sort()
    prev_segment = [0, 0]

    for cur_segment in intersection_segment:
      if cur_segment[1] < 0 or cur_segment[0] > 4000000:
        # Ignore segment out of interested range
        continue

      # Check if current segment intersect with previous segment
      if prev_segment[1] >= cur_segment[0]:
        # Update previous segment with a union of previous and current segment
        prev_segment = (
            min(prev_segment[0], cur_segment[0]),
            max(prev_segment[1], cur_segment[1]),
        )
      else:
        # There's a possible location
        distress_beacon = (prev_segment[1] + 1, y)
        break

    if distress_beacon is not None:
      break
  print("Part 2: ", distress_beacon, distress_beacon[0] * 4000000 + y)


if __name__ == "__main__":
  part_1()
  part_2()

