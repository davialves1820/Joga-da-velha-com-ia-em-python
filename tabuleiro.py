
class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    # Inicializa o tabuleiro com todas as posições vazias
    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]

    # Verifica se à vencedor nas linhas
    def campeao_linha(self):
        
        for l in range(0,3):
            if (self.matriz[l][0] != Tabuleiro.DESCONHECIDO and self.matriz[l][0] == self.matriz[l][1] == self.matriz[l][2]):
                return self.matriz[l][0]
        else:
            return Tabuleiro.DESCONHECIDO
    
    # Verifica se à vencedor nas colunas
    def campeao_coluna(self):
        
        for c in range(0,3):
            if (self.matriz[0][c] != Tabuleiro.DESCONHECIDO and self.matriz[1][c] == self.matriz[2][c] == self.matriz[0][c]):
                return self.matriz[0][c]
        else:
            return Tabuleiro.DESCONHECIDO
    
    # Verifica se à vencedor nas diagonais
    def campeao_diagonal(self):
        if (self.matriz[0][0] != Tabuleiro.DESCONHECIDO and self.matriz[1][1] == self.matriz[2][2] == self.matriz[0][0]):
                return self.matriz[0][0]
        elif (self.matriz[0][2] != Tabuleiro.DESCONHECIDO and self.matriz[1][1] == self.matriz[2][0] == self.matriz[0][2]):
                return self.matriz[0][2]
        else:
                return Tabuleiro.DESCONHECIDO
    
    # Verifica se à campeão
    def tem_campeao(self):
        soma = self.campeao_coluna() + self.campeao_diagonal() + self.campeao_linha()
        
        if soma == 0:
            return Tabuleiro.DESCONHECIDO
        elif soma % 4 == 0:
            return Tabuleiro.JOGADOR_X
        else:
            return Tabuleiro.JOGADOR_0