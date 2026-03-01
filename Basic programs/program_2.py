# Basic calculator on two values (+,-,*,/)
operation = input("What operation do you want to perform (+,-,*,/) : ")
operator1 = int(input("Write the first value for performing the calculation : "))
operator2 = int(input("Write the second value for performing the calculation : "))
if operation == "+" :
    print(f"The output is {operator1+operator2}")
elif operation == "-" :
    print(f"The output is {operator1-operator2}")
elif operation == "*" :
    print(f"The output is {operator1*operator2}")
elif operation == "/" :
    print(f"The output is {operator1/operator2}")    
else : 
    print("Operation not available")