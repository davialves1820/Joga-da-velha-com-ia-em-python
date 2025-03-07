# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        # 1. Verificar vitória ou bloqueio
        jogada = self.verificar_vitoria_ou_bloqueio(self.tipo)
        if jogada:
            return jogada  # Se houver vitória ou bloqueio, faz a jogada

        # 2. Criar vantagem
        jogada = self.criar_vantagem(self.tipo)
        if jogada:
            return jogada  # Se puder criar uma vantagem, faz a jogada

        # 3. Controle do centro
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)  # Joga no centro se disponível

        # 4. Marcação oposta
        jogada = self.marcar_oposto()
        if jogada:
            return jogada  # Se houver uma marcação oposta, faz a jogada

        # 5. Usar cantos vazios
        jogada = self.usar_cantos_vazios()
        if jogada:
            return jogada  # Se houver um canto vazio, joga nele

        # 6. Marcação arbitrária
        return self.jogada_aleatoria()

    def verificar_vitoria_ou_bloqueio(self, jogador: int) -> (int, int):
        # Verificar se o jogador pode ganhar ou bloquear a vitória
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = jogador
                    if self.tabuleiro.tem_campeao() == jogador:
                        
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)  # Vitória
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

                    # Verificar se o oponente pode ganhar e bloquear
                    
                    self.matriz[l][c] = Tabuleiro.JOGADOR_X
                    
                    if self.tabuleiro.tem_campeao() == Tabuleiro.JOGADOR_X:
                        print("bloqueia")
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)  # Bloqueio
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
        return None

    # Tentar criar uma jogada que crie duas possíveis vitórias
    def criar_vantagem(self, jogador: int) -> (int, int):
        # Procura por uma linha e uma coluna que tem somente o símbolo O
        linha = -1
        coluna = -1
        pontos_linha = 0
        pontos_coluna = 0

        for l in range(3):
            for c in range(3):
                if (self.matriz[l][c] == Tabuleiro.JOGADOR_0):
                    pontos_linha += 1
                elif (self.matriz[l][c] == Tabuleiro.JOGADOR_X):
                    pontos_linha += 4

                if (self.matriz[c][l] == Tabuleiro.JOGADOR_0):
                    pontos_coluna += 1
                elif (self.matriz[c][l] == Tabuleiro.JOGADOR_X):
                    pontos_linha += 4
            if (pontos_linha == 1):
                linha = l

            if (pontos_coluna == 1):
                coluna = l
            
            pontos_linha = 0
            pontos_coluna = 0

        # Caso encontrado as linhas e colunas e sendo uma posição vazia efetua a jogada
        if (linha >= 0 and coluna >= 0 and self.matriz[linha][coluna] == Tabuleiro.DESCONHECIDO):
            return (linha, coluna)
        
        return None

    # Se o jogador marcar um canto, a IA marca o canto oposto
    def marcar_oposto(self) -> (int, int):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (l, c) in cantos:
            if self.matriz[l][c] == Tabuleiro.JOGADOR_X:  # Oponente marcou um canto
                oposto = (2 - l, 2 - c)
                if self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                    return oposto  # Marca o canto oposto
        return None

    # Se houver cantos vazios, prioriza jogá-los
    def usar_cantos_vazios(self) -> (int, int):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for (l, c) in cantos:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)  # Joga em um canto vazio
        return None

    # Caso não haja jogadas estratégicas, joga aleatoriamente
    def jogada_aleatoria(self) -> (int, int):
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
        return lista[randint(0, len(lista) - 1)] if lista else None
