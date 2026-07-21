# Python - Python If-Else
# Skills: Python (Basic)
# Difficulty: Easy

def odd_or_even (n):
    if n >=1 and n <=100:
        if n % 2 !=0:
            print("Weird")
        else:
            if n>=2 and n<=5:
                print("Not Weird")
            elif n>=6 and n<=20:
                print ("Weird")
            else:
                print ("Not Weird")
            
    else:
        print("Number is not valid")

if __name__ == '__main__':
    n = int(input().strip())
    odd_or_even(n)
