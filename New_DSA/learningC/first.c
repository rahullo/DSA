#include <stdio.h>
#include <stdlib.h>

int main() {
  int *array;
  int size = 5000;

  array = (int *)malloc(size * sizeof(int));
  if (array == NULL) {
    printf("Error allocating memory!\n");
    return 1;
  }

  for (int i = 0; i < size; i++) {
    array[i] = i;
  }

  for (int i = 0; i < size; i++) {
    printf("%d ", array[i]);
  }

  free(array);

  return 0;
}