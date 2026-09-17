#include <stdio.h>

// Merge function:
// Be sorted portions ne merge kari ne ek sorted portion banave che.
void merge(int arr[], int left, int mid, int right)
{
    int i = left;
    int j = mid + 1;
    int k = 0;

    // Temporary array maximum required size jetlu banaviye.
    int temp[right - left + 1];

    // Banney sorted portions mathi smallest element
    // temporary array ma add kariye.
    while (i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    // Left portion ma remaining elements hoy
    // to temporary array ma copy karo.
    while (i <= mid)
        temp[k++] = arr[i++];

    // Right portion ma remaining elements hoy
    // to temporary array ma copy karo.
    while (j <= right)
        temp[k++] = arr[j++];

    // Temporary array ne original array ma copy back karo.
    for (i = left, k = 0; i <= right; i++, k++)
        arr[i] = temp[k];
}

// Merge Sort
// Array ne repeatedly half ma divide kariye.
// Pachhi sorted halves ne merge kariye.

void mergeSort(int arr[], int left, int right)
{
    // Single element already sorted hoy che.
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;

    // Left half sort karo.
    mergeSort(arr, left, mid);

    // Right half sort karo.
    mergeSort(arr, mid + 1, right);

    // Banney sorted halves merge karo.
    merge(arr, left, mid, right);
}

int main()
{
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = 7;

    mergeSort(arr, 0, n - 1);

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}