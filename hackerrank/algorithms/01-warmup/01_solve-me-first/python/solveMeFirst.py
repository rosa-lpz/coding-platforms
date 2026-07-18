def solveMeFirst(a, b):
    # Check if a and b are within the valid range
    if 1 <= a <= 1000 and 1 <= b <= 1000:
        return a + b
    else:
        print("The numbers are not valid")
        return None
    
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)