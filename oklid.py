import math

def euclidean_distance(point1, point2):
  
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
  # Noktaları tanımlayın
  points = [
    (1, 2),
    (4, 6),
    (3, 1),
    (5, 7)
  ]

  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      distances.append(distance)

  min_distance = min(distances)

  print(f"Minimum mesafe: {min_distance:.2f}")

if __name__ == "__main__":
  main()
