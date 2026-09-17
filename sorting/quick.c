#include <stdio.h>

// Partition function:
// Pivot ne eni final correct position par place kare che.
//
// Pivot karta nana/equal elements left side ma
// ane mota elements right side ma aave che.

int partition(int arr[], int low, int high)
{
    // Last element ne pivot choose kariye.
    int pivot = arr[high];

    // i smaller elements ni boundary maintain kare che.
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        // Jo current element pivot karta nano/equal hoy,
        // to ene left side ma move karo.
        if (arr[j] <= pivot)
        {
            i++;

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Pivot ne correct position par muki do.
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

// Quick Sort
// Pivot select kari ne array ne two parts ma divide kariye.
// Pachhi banney parts ne recursively sort kariye.

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        // Pivot ni correct position find karo.
        int pivotIndex = partition(arr, low, high);

        // Pivot ni left side sort karo.
        quickSort(arr, low, pivotIndex - 1);

        // Pivot ni right side sort karo.
        quickSort(arr, pivotIndex + 1, high);
    }
}

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = 6;

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}