import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getPoint(self):
        return self.x, self.y
    
    def showPoint(self):
        print(f"Point: ({self.x}, {self.y})")

class Shape(Point):
    def __init__(self, x, y, vertices):
        super().__init__(x, y)
        self.vertices = vertices
    
    def identifyShape(self):
        num_vertices = len(self.vertices)
        if num_vertices == 3:
            return "Triangle"
        elif num_vertices == 4:
            side_lengths = []
            for i in range(4):
                x1, y1 = self.vertices[i]
                x2, y2 = self.vertices[(i + 1) % 4]
                side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                side_lengths.append(side_length)
            # Assuming a square has equal sides
            if all(side == side_lengths[0] for side in side_lengths):
                return "Square"
            # Assuming a rectangle has opposite sides of equal length
            elif side_lengths[0] == side_lengths[2] and side_lengths[1] == side_lengths[3]:
                return "Rectangle"
        return "Unknown Shape"

class Outlier(Shape):
    def checkIfPointInShape(self, x_point, y_point):
        # Assuming the shape is a square with vertices at (self.x, self.y), (self.x + side_length, self.y), 
        # (self.x, self.y + side_length), and (self.x + side_length, self.y + side_length)
        side_length = math.sqrt((self.vertices[1][0] - self.vertices[0][0]) ** 2 + (self.vertices[1][1] - self.vertices[0][1]) ** 2)
        
        if self.x <= x_point <= self.x + side_length and self.y <= y_point <= self.y + side_length:
            print("Point falls within the area.")
        else:
            print("Point is an outlier.")

# Main method to demonstrate the classes
if __name__ == "__main__":
    # Create a Point
    point = Point(2, 3)
    point.showPoint()

    # Create a Shape (Assuming a square with vertices)
    vertices = [(2, 3), (4, 3), (2, 5), (4, 5)]
    shape = Shape(7, 9, vertices)
    print("Identified Shape:", shape.identifyShape())

    # Create an Outlier and check if a point falls within the shape
    outlier_point = Outlier(3, 4, vertices)
    x_point, y_point = 3.5,4.5
    print(f"Checking point ({x_point}, {y_point})")
    outlier_point.checkIfPointInShape(x_point, y_point)
