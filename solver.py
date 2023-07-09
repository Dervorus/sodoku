
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(bo):
    for i in range(len(bo)): #para cada numero no eixo X
        if i % 3 == 0 and i != 0: #se for uma linha divisivel por 3 e não for a linha zero
            print("---------------------") #imprime o separador
        for j in range(len(bo[0])): 
            if j % 3 == 0  and j != 0: #se for uma coluna divisivel por 3 e nao for a primeira
                print("| ", end="") #imprime o pipe e nao quebra a linha
            if j == 8: #se for a ultima posicao
                print(bo[i][j]) #imprime o caracter e QUEBRA a linha
            else: # qualquer outra posicao
                print(str(bo[i][j])+ " ", end="") #imprime o caracter e nao quebra a linha

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): #loop por todos os valores
            if bo[i][j] == 0: # se o valor for zero
                return (i, j) # retorna linha coluna com campo em zero

def main():
    print_board(board)
    
if __name__ == "__main__":
    main()