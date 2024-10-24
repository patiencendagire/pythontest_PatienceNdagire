# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
def distance_between_two_coordinates():
    x1=int(input("Enter the distance x1 :"))
    x2=int(input("Enter the distance x2:"))
    y1=int(input("Enter the distance y1:"))
    y2=int(input("Enter the distance y2:"))
    import math
    squareroot=math.sqrt
    distance=squareroot((x2-x1)**2 +(y2-y1)**2)
    print(f'The distance between two points (x1-y1) and (x2-y2) is distance {distance}')
distance_between_two_coordinates()

# Question 1(ii)
# Write a Python program to find maximum between three numbers
number=int(input("enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
maximum=(number+num2+num3)
print(f'The maximum between three numbers is {maximum}')





