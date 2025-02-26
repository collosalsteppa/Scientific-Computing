import math

def calculate_area(shape, dimension1,dimension2=0):
 if shape =="circle":
    area =math.pi*(dimension1)
 elif shape =="rectangle":
    area = dimension1 * dimension2
 elif shape == "triangle":
    area = 0.5 * dimension1 * dimension2
 else:
      raise ValueError("invalid shape .Choose circle, rectangle or triangle.")

 return area


 #testing the function with different shapes
try:
     circle_area=calculate_area("circle", 5)
     print(f"area of the circle with radius of 5 is : {circle_area:.2f}")
     
     rectangle_area=calculate_area("rectangle",34,56)
     print(f"the area of a rectangle with length 34 and width 56 is :{rectangle_area:.2f}")

     triangle_area= calculate_area("triangle",3,4)
     print(f"the area of the triangle with base 3 and height 4 is:{triangle_area:.2f}")

except ValueError as e:
     print(e)
