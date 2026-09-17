#include <stdio.h>

// Binary Search
// Sorted array ma search space ne darek step par half kariye.
// Aa reason thi Binary Search ni time complexity O(log n) che.

int binarySearch(int arr[], int n, int target)
{
    int left = 0;
    int right = n - 1;

    while (left <= right)
    {
        // Aa formula overflow avoid karva mate safe che.
        int mid = left + (right - left) / 2;

        // Target mali gayo.
        if (arr[mid] == target)
            return mid;

        // Target middle karta moto che,
        // etle right half ma search karishu.
        if (arr[mid] < target)
            left = mid + 1;

        // Target middle karta nano che,
        // etle left half ma search karishu.
        else
            right = mid - 1;
    }

    // Target array ma present nathi.
    return -1;
}

int main()
{
    int arr[] = {10, 20, 30, 40, 50, 60, 70};
    int n = 7;
    int target = 50;

    int result = binarySearch(arr, n, target);

    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");

    return 0;
}