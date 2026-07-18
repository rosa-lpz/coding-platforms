# Simple Array Sum

Given an array of integers, find the sum of its elements.

For example, if the array $ar = [1,2,3]. 1 + 2+ 3 = 6$ so return 6.

**Function Description**

Complete the function with the following parameter(s):

- ar[n]: an array of integers

**Returns**

- int: the sum of the array elements

**Input Format**

The first line contains an integer, n , denoting the size of the array.
The second line contains space-separated integers representing the array's elements.

**Constraints**

$0 >n, ar[i] <=100$

**Sample Input**

```
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]
```

**Sample Output**

```
31
```

**Explanation**

Print the sum of the array's elements: $1+2+3+4+10+11=31$.



# Solutions -------

# Python

## Version 1

```python
import os
import sys

def simpleArraySum(ar):
    sum=0;
    for i in range(len(ar)):
        sum+=ar[i]
    return (sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

```



### **Output**



#### **Test case #0** (Passed)

**Input**

2

3



**Output**

5



### Reference

* https://www.openbookproject.net/thinkcs/python/english2e/ch04.html



## Version 2  

 

```python
import sys

def simpleArraySum(n, ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    # print("array: ", ar)
    result = simpleArraySum(n, ar)
    print(result)
```

 

# -----

# C++

```c++
#include <iostream>
#include <vector>

using namespace std;

// Function to compute the sum of the array
int simpleArraySum(int n, const vector<int>& ar) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        sum += ar[i];
    }
    return sum;
}

int main() {
    int n;
    cin >> n;  // Read the number of elements in the array
    
    vector<int> ar(n);  // Create a vector to store the array elements
    for (int i = 0; i < n; ++i) {
        cin >> ar[i];  // Read each element of the array
    }
    
    int result = simpleArraySum(n, ar);  // Call the function to get the sum
    cout << result << endl;  // Output the result
    
    return 0;
}


```

* **Libraries**:
  - In C++, `#include <iostream>` is used to handle input/output operations.
  - `#include <vector>` is used to declare and work with dynamic arrays (vectors).

* **Function `simpleArraySum`**:

  - The function `simpleArraySum` in C++ takes two arguments: an integer `n` (size of the array) and a `vector<int>` (the array).

  - We initialize `sum` to 0 and iterate over the array to compute the sum of its elements.

* **Main Function**:

  - `cin >> n;` reads the number of elements in the array.
  - We create a `vector<int>` called `ar` to store the array elements. We use a `for` loop to input each element using `cin >> ar[i];`.
  - The sum is calculated by calling `simpleArraySum(n, ar)`.
  - The result is printed using `cout`.



# ---

# Java

## Version 1

```java
import java.util.Scanner;

public class SimpleArraySum {

    // Function to compute the sum of the array
    public static int simpleArraySum(int n, int[] ar) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += ar[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read the number of elements in the array
        int n = sc.nextInt();

        // Create an array to store the array elements
        int[] ar = new int[n];

        // Read the elements of the array
        for (int i = 0; i < n; i++) {
            ar[i] = sc.nextInt();
        }

        // Call the function to get the sum
        int result = simpleArraySum(n, ar);

        // Output the result
        System.out.println(result);

        // Close the scanner to avoid memory leak
        sc.close();
    }
}

```





# REFERENCES
