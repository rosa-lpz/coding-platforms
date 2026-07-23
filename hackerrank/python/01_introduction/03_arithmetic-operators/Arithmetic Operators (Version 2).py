# Python - Arithmetic Operators (Version 2)
# Skills: Python (Basic)
# Difficulty: Easy

if __name__ == '__main__':
    a = int(input("a: ").strip())
    b = int(input("b: ").strip())
   
     # 1 <= value <=10000000000
    while (1<= a <=10**10) and (1<= b <=10**10):
        continue        
    else:
        print("Please, give integer values between 1 and 10^10")
        a = int(input("a: ").strip())
        b = int(input("b: ").strip())
   
    print ("a + b: ", a + b)
    print ("a - b: ", a - b)
    print ("a * b: ", a * b)