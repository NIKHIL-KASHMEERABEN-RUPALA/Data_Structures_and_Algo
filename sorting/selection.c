#include <stdio.h>

// Selection Sort
// Darek position mate smallest element find kariye.
// Pachhi smallest element ne current position sathe swap kariye.

void selectionSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        // Initially assume kariye ke arr[i] minimum che.
        int minIndex = i;

        // Remaining unsorted portion ma minimum find karo.
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }

        // Minimum element ne correct position par muki do.
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = 5;

    selectionSort(arr, n);

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}