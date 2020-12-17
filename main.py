import os

def imprimir_tabuleiro(board):
	
	
	print('   |   |   ')
	print(' '+ board[6]+' | '+ board[7]+' | '+board[8])
	print('   |   |   ')
	print('--------------')
	print('   |   |   ')
	print(' '+ board[3]+' | '+ board[4]+' | '+board[5])
	print('   |   |   ')
	print('--------------')
	print('   |   |   ')
	print(' '+ board[0]+' | '+ board[1]+' | '+board[2])
	print('   |   |   ')
	

def player_input(marker):

    while marker != 'X' and marker != 'O':
        marker = input('Jogador 1, você deseja ser X ou O?\n').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):

	board[position] = marker

def win_check(board,marker):

    return ((board[6] == marker and board[7] == marker and board[8] == marker)or
    (board[3] == marker and board[4] == marker and board[5] == marker) or
    (board[0] == marker and board[1] == marker and board[2] == marker) or
    (board[6] == marker and board[3] == marker and board[0] == marker) or
    (board[8] == marker and board[5] == marker and board[2] == marker) or
    (board[6] == marker and board[4] == marker and board[2] == marker) or
    (board[0] == marker and board[4] == marker and board[8] == marker) or
    (board[7] == marker and board[4] == marker and board[1] == marker))

def space_check(board,position):

	if board[position] == ' ':
		return True
	else:
		return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
	proxima = -1
	while proxima not in range(0,9):
		proxima = int(input("Digite a posição que deseja (0 - 8)\n"))
		while proxima in range(0,9):
			if space_check(board,proxima):
				return proxima
			else:
				print("Posição ja ocupada, tente outra!\n")
				proxima = int(input("Digite a posição que deseja (0 - 8)\n"))
		else:
			print("Posição inexistente, tente outra!\n")
			

def replay():
	decisao = ' '
	while decisao != 1 and decisao != 2:
		decisao = int(input("Desejam jogar novamente? \n1-SIM\n2-NAO\n"))
		if decisao == 1:
			return True
		elif decisao == 2:
			return False

print('BEM VINDO AO JOGO DA VELHA!')

while True:
	clear = lambda: os.system('cls')
	board = [' '] * 9
	marker = '.'
	player1 = 0
	player2 = 0
	print("ESTE É UM JOGO DA VELHA FEITO EM PYTHON 3. DIVIRTA-SE :)")
 
	players = player_input(' ')
    
	while not win_check(board,marker) and not full_board_check(board):
        
		while player1 == 0:
			clear()
			marker = players[0]
			print("Vez do jogador 1")
			imprimir_tabuleiro(board)
			escolha = player_choice(board)
			place_marker(board,players[0],escolha)
			player1 = 1
		if win_check(board,marker):
			break;
		player1 = 0
		while player2 == 0:
			clear()
			marker = players[1]
			print("Vez do jogador 2")
			imprimir_tabuleiro(board)
			escolha = player_choice(board)
			place_marker(board,players[1],escolha)
			player2 = 1
		if win_check(board,marker):
			break;
		player2 = 0

	else:
		print("Empate!")

	if marker == players[0]:
		clear()
		print("Jogador 1 ganhou!")
		imprimir_tabuleiro(board)

	elif marker == players[1]:
		clear()
		print("Jogador 2 ganhou!")
		imprimir_tabuleiro(board)
			    
	if not replay():
		print("Obrigado por jogar :)")
		break



