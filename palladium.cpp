#include <limits.h>
#include <stdio.h>

int main () {
  int h[] = {3,1,4};
  int n   = 3;

  int hist_esquerda[5];
  int hist_direita[5];

  // Primeira passada: historicos de maximo da esquerda pra direita
  for (int i = 0, max = INT_MIN; i < n; i++) {
    if (h[i] > max) {
      max = h[i];
    }
    hist_esquerda[i] = max;
  }

  // Segunda passada: historicos de maximo da direita pra esquerda
  for (int i = 1, max = INT_MIN; i <= n; i++) {
    if (h[n - i] > max) {
      max = h[n - i];
    }
    hist_direita[n - i] = max;
  }

  int solucao = INT_MAX;
  // Terceira passada: calcular a solucao
  for (int i = 0; i <= n; i++) {
    // Corner case 1: apenas uma lona, a da direita
    if (i == 0) {
      int lona_direita = n * hist_direita[i];
      if (lona_direita < solucao) {
        solucao = lona_direita;
      }
      printf("Partindo em %d, achei %d\n", i, lona_direita);
    }
    // Corner case 2: apenas uma lona, a da esquerda
    else if (i == n) {
      int lona_esquerda = n * hist_esquerda[i-1];
      if (lona_esquerda < solucao) {
        solucao = lona_esquerda;
      }
      printf("Partindo em %d, achei %d\n", i, lona_esquerda);
    }
    // Caso comum: partir em algum lugar no meio, usando duas lonas
    else {
      int lona_esquerda = i * hist_esquerda[i-1];
      int lona_direita = (n - i) * hist_direita[i];
      int duas_lonas = lona_esquerda + lona_direita;
      if (duas_lonas < solucao) {
        solucao = duas_lonas;
      }
      printf("Partindo em %d, achei %d + %d\n", i, lona_esquerda, lona_direita);
    }

  }

  printf("%d\n", solucao);
}