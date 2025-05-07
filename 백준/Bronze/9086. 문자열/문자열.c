#include <stdio.h>

int main() {
  int T;
  char tst[1001];

  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%s", tst);
    printf("%c%c \n", tst[0], tst[strlen(tst) - 1]);
  }
}
