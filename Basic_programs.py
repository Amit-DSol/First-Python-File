#area and perimeter calculator 
shape = input("Write the shape you want to calculate area or perimeter of (square,rectangle,circle,triangle) : ")
determinant = input("Write want you want (area or perimeter) : ")
if shape == ("square" or "Square"):
    side = int(input("Write the side of square : "))
    if determinant == ("area" or "Area"):
        print(f"The area of square with side {side} cm is {side*side}")
    elif determinant == ("perimeter" or "Perimeter") : 
        print(f"The perimeter of square with side {side} cm is {side*4}")
    else :
        print("Operation or operands not specified")        
elif shape == ("rectangle" or "Rectangle"):
    length = int(input("Write the length of rectangle : "))
    breadth = int(input("Write the breadth of rectangle : "))
    if determinant == ("area" or "Area"):
        print(f"The area of rectangle is {length*breadth}")
    elif determinant == ("perimeter" or "Perimeter") : 
        print(f"The perimeter of rectangle is {2*(length + breadth)}")
    else :
        print("Operation or operands not specified")        
elif shape == ("circle" or "Circle"):
    radius = int(input("Write the radius of circle : "))
    if determinant == ("area" or "Area") :
        print(f"The area of circle is {3.14 * radius*radius}")
    elif determinant == ("perimeter" or "Perimeter") : 
        print(f"The perimeter of circle is {radius*4*3.14}")
    else :
        print("Operation or operands not specified")       
elif shape == ("triangle" or "Triangle"):
    if determinant == ("area" or "Area") :
        height = int(input("Write the height of triangle : "))
        base = int(input("Write the base of triangle : "))
        print(f"The area of triangle is {0.5*base*height}")
    elif determinant == ("perimeter" or "Perimeter") :
        side1 = int(input("Write the side1 of triangle : "))
        side2 = int(input("Write the side2 of triangle : "))
        side3 = int(input("Write the side3 of triangle : ")) 
        print(f"The perimeter of triangle is {side1+side2+side3}")
    else :
        print("Operation or operands not specified")        

                  