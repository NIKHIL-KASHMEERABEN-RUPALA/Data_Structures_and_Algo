#include <stdio.h>

// Bubble Sort
// Adjacent elements ne compare kariye.
// Jo left element right karta moto hoy,
// to banne ne swap kariye.
//
// Darek pass pachi largest unsorted element
// array na end ma automatically place thai jay che.

void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int swapped = 0;

        for (int j = 0; j < n - i - 1; j++)
        {
            // Wrong order hoy to swap karo.
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                swapped = 1;
            }
        }

        // Jo koi swap thayu nathi,
        // to array already sorted che.
        if (swapped == 0)
            break;
    }
}

int main()
{
    int arr[] = {5, 1, 4, 2, 8};
    int n = 5;

    bubbleSort(arr, n);

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}