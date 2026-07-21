# If - Else

## Task 
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird

If n is even and in the inclusive range of 2 to 5, print Not Weird

If n is even and in the inclusive range of 6 to 20, print Weird

If n is even and greater than 20, print Not Weird

**Input Format**

A single line containing a positive integer, n.

**Constraints**

1 <= n <= 100



# Solutions



## Python

### Version 1

```python

import sys


N = int(raw_input().strip())

if N % 2 != 0:
    print "Weird"
else:
    if N >= 2 and N <= 5:
        print "Not Weird"
    elif N >= 6 and N <= 20:
        print "Weird"
    elif N > 20:
        print "Not Weird"


```



### Version 2

```python
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

```



### Version 3

```python

def odd_or_even (n):
    if N % 2 !=0:
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

```





