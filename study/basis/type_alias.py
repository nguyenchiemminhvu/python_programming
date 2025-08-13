from typing import Tuple, List

Point = Tuple[float, float]
def distance(p1: Point, p2: Point) -> float:
    """Calculate the Euclidean distance between two points."""
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Example usage
p1: Point = (1.0, 2.0)
p2: Point = (4.0, 6.0)
dist = distance(p1, p2)
print(f"The distance between {p1} and {p2} is {dist:.2f}")

Path = List[Point]
def total_distance(points: Path) -> float:
    """Calculate the total distance for a path defined by a list of points."""
    return sum(distance(points[i], points[i + 1]) for i in range(len(points) - 1))

# Example usage
path: Path = [(1.0, 2.0), (4.0, 6.0), (7.0, 8.0)]
total_dist = total_distance(path)
print(f"The total distance for the path {path} is {total_dist:.2f}")