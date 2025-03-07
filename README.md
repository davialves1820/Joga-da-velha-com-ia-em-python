# Jogo da Velha com IA
O programa implementa um jogo da velha onde o adversário é uma Inteligência Artificial (IA) que nunca perde. O objetivo é desafiar a IA, que sempre joga de forma ideal para vencer ou empatar.

## 🧠 Lógica da Inteligência Artificial
1. **Bloqueio ou Vitória imediata**:  
   - Se você ou a IA tiver duas marcações em sequência, a IA preenche o terceiro quadrado.  
2. **Criação de vantagens**:  
   - A IA prioriza jogadas que criem duas sequências de vitória possíveis.  
3. **Controle do centro**:  
   - A IA joga no quadrado central, se disponível.  
4. **Marcação oposta**:  
   - Se o jogador marcar um canto, a IA marca o canto oposto.  
5. **Uso de cantos vazios**:  
   - A IA preenche um canto livre antes de outras áreas.  
6. **Marcação arbitrária**:  
   - Em último caso, a IA marca qualquer quadrado vazio.

## 📂 Organização
- pycache: Pasta com o arquivo de execução.

- buttons.py: Gerenciamento de botões na interface.

- tabuleiro_screen.py: Tela do tabuleiro.

- tabuleiro.py: Representação lógica do tabuleiro.

- jogador.py: Classe base para jogadores.

- jogador_humano.py: Classe do jogador humano.

- jogador_ia.py: Classe da IA.

- jogo_velha.py: Regras do jogo da velha.

- main.py: Arquivo principal para iniciar o jogo.

## 🖥️ Execução

### Executar o jogo
```
python main.py
```
