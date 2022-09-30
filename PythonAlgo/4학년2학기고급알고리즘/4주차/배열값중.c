#include <stdio.h>
int main(void) {
    int arr1[] = {6,0,8,2,3,0,4,0,1};
    int n = sizeof(arr1) / sizeof(arr1[0]);
    int j = 0;
    for (int i = 0; i<n; i++)
    {
        if (arr1[i] != 0)
            arr1[j] = arr1[i];
            j += 1;
    }
    for (int i=j; i<n; i++)
        arr1[j] = 0;
    for (int i = 0; i<n; i++)
        printf("%d",arr1[i]);
    return 0;
}