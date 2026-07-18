
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
