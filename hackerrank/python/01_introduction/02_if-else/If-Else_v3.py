# Python - Python If-Else (Version 3)
# Skills: Python (Basic)
# Difficulty: Easy

def odd_or_even (n):
    if n % 2 !=0:
         print("Weird")
    elif n%2==0 and 2<=n<=5:
         print("Not Weird")
    elif n%2==0 and 6<=n<=20:
         print ("Weird")
    else:
        print ("Not Weird")
    
    
if __name__ == '__main__':
    n = int(input().strip())
    odd_or_even(n)