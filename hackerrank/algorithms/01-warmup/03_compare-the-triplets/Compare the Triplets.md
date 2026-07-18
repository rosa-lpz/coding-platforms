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

# Rust

```rust

use std::io;
use std::cmp::Ordering;

fn get_numbers() -> Vec<u32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).ok().expect("Failed to read line");
    line.split_whitespace().map(|s| s.parse::<u32>().unwrap()).collect()
}

fn main() {
    let a = get_numbers();
    let b = get_numbers();
    
    let mut alice = 0;
    let mut bob = 0;
    
    for idx in 0..3 {
        match a[idx].cmp(&b[idx]) {
            Ordering::Less      => bob += 1,
            Ordering::Greater   => alice += 1,
            Ordering::Equal     => {},
        }
    }
 
    println!("{} {}", alice, bob);
}

```

Reference

* https://martinkysel.com/hackerrank-compare-triplets-solution/

# -----

# C++

```c++
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

// Function to get a vector of numbers from input
vector<int> getNumbers() {
    string line;
    getline(cin, line);  // Read a whole line of input
    stringstream ss(line);
    vector<int> numbers;
    int num;
    while (ss >> num) {
        numbers.push_back(num);
    }
    return numbers;
}

int main() {
    vector<int> a = getNumbers();  // Read the first list of numbers
    vector<int> b = getNumbers();  // Read the second list of numbers
    
    int alice = 0, bob = 0;
    
    for (int i = 0; i < 3; ++i) {
        if (a[i] > b[i]) {
            alice += 1;
        } else if (a[i] < b[i]) {
            bob += 1;
        }
        // If they are equal, do nothing
    }
    
    cout << alice << " " << bob << endl;  // Print the result
    
    return 0;
}

```

* **Libraries**:
  - `#include <iostream>` for input and output.
  - `#include <vector>` for using dynamic arrays (vectors in C++).
  -  `#include <sstream>` for parsing the input string into integers.
* **Function `getNumbers`**:
  * This function reads a line from the input, splits the line into individual numbers using a `stringstream`, and then stores them into a vector of integers.
  * The `getline(cin, line)` function is used to read the entire line of input.
  * We use a `while (ss >> num)` loop to parse integers from the stringstream and store them in a vector.

* **Main Function**:
  - The vectors `a` and `b` are filled by calling `getNumbers()` for each input line.
  - We initialize two variables `alice` and `bob` to keep track of the scores.
  - The loop compares corresponding elements in `a` and `b`. If an element in `a` is greater than the corresponding element in `b`, Alice gets a point; if it's smaller, Bob gets a point. If they are equal, no points are awarded.
  - Finally, we print Alice's and Bob's scores.







# REFERENCES
