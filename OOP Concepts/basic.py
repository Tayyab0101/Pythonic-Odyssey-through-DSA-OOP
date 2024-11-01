class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"

class Shape:
    def __init__(self, points):
        self.points = points
        
    def __str__(self):
        result = ""
        for point in self.points:
            result += str(point) + "-"
        return result[:-1]

# Create Point objects
p1 = Point(5, 5)
p2 = Point(10, 5)
p3 = Point(5, 10)

# Create a list of points
points = [p1, p2, p3]

# Create a Shape object with the list of points
shape1 = Shape(points)

# Print the Shape object
print(shape1)


