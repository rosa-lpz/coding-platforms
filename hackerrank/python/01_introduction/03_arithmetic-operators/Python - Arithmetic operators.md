# Python - Arithmetic operators

* Skills: Python (Basic)
* Difficulty: Easy
* Subdomain: Introduction

## Task 
The provided code stub reads two integers from STDIN, and . Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.



**Example**

a = 3

b = 5

Print the following:

```cmd
8
-12
15
```



**Input Format**

The first line contains the first integer, $a$.
The second line contains the second integer, $b$ .

**Constraints**

1<= a <=10^10

1<= b <=10^10



**Output Format**

Print the three lines as explained above.

**Sample Input 0**

```
3
2
```

**Sample Output 0**

```
5
1
6
```

**Explanation 0**

$3 + 2 ==> 5$

$3 - 2 ==> 1$

$3 * 2 ==> 6$



# Solutions



## Python



### Solution 1 - Python 3

```python
a = int(input().strip())
if a<1 and a< (10**10):
  a = int(input())

b = int(input().strip())
if b<1 and b< (10**10):
  b = int(input())



print (a + b)
print (a - b)
print (a * b)
```



### Solution 2 - Python 3

```python
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
```







