#include <iostream>
using namespace std;

int solveMeFirst(int a, int b) {
    // Check if a and b are within the valid range
    if (a >= 1 && a <= 1000 && b >= 1 && b <= 1000) {
        return a + b;
    } else {
        cout << "The numbers are not valid" << endl;
        return -1; // Return -1 to indicate invalid input
    }
}

int main() {
    int num1, num2;
    cin >> num1 >> num2;  // Input numbers
    int res = solveMeFirst(num1, num2);
    
    if (res != -1) { // Only print the result if it's valid
        cout << res << endl;
    }
    
    return 0;
}
