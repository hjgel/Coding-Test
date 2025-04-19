#include <stdio.h>

int main() {
  int i, j;
  int n = 0; // 출력할 줄 수

  scanf("%d", &n);

  for (i = 1; i <= n; i++) {
    // 공백 출력
    for (j = 1; j <= n - i; j++) {
      printf(" ");
    }

    // 별 출력
    for (j = 1; j <= i; j++) {
      printf("*");
    }

    printf("\n"); // 줄 바꿈
  }

  return 0;
}