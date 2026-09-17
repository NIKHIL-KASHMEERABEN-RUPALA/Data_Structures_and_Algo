#include <stdio.h>

// Linear Search
// Array na darek element ne ek-ek kari ne check kariye.
// Jo target mali jay to eno index return kariye.
// Jo target na male to -1 return kariye.

int linearSearch(int arr[], int n, int target)
{
    for (int i = 0; i < n; i++)
    {
        // Current element target sathe match thay che?
        if (arr[i] == target)
            return i;
    }

    // Target array ma present nathi.
    return -1;
}

int main()
{
    int arr[] = {10, 20, 30, 40, 50};
    int n = 5;
    int target = 30;

    int result = linearSearch(arr, n, target);

    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");

    return 0;
}