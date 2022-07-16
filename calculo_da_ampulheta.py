# Bibliotecas importadas
from time import sleep
from os import system
from math import ceil, sqrt
import os

# Limpando o terminal
os.system('cls')

# Começo do programa
x = True
while x == True:
	seconds = int(input('Tempo em segundos: '))
	if seconds >= 20:
		def print_glass(size, tot, seconds_up, seconds_down):
			width = 2 * size
			count_up = count_down = 0
			print('_' * width)
			for i in range(1, 2 * size + 1):
				diag1 = diag2 = 2 * size + 1
				for j in range(1, 2 * size + 1):
					symbol = ' '
					
					# Diagonal esquerda
					if i == j:
						symbol, diag1 = '\\', j
					
					# Diagonal direita
					elif i + j == 2 * size + 1:
						symbol, diag2 = '/', j
						
					# Areia da ampulheta
					elif diag1 < j < diag2:
						count_up += 1
						if count_up > (tot-seconds_up):
							symbol = '*'
					elif diag2 < j < diag1:
						count_down += 1
						if count_down > (tot-seconds_down):
							symbol = '*'
							
					print(symbol, end = '')
				print()
			print('_' * width)
			return count_up

		# Calculando o tamanho e o espaço total
		size = ceil(sqrt(seconds)) + 1
		total = print_glass(size, 3 * size, seconds, 8)
		system('cls')

		# Movimento da areia na ampulheta
		for sec in range(seconds):
			print_glass(size, total, seconds-sec, sec)
			sleep(1)
			system('cls')
		print_glass(size, total, 0, seconds)
		x = False
	else:
		print("\nO TEMPO DEVE SER MAIOR OU IGUAL A 20 SEGUNDOS! TENTE NOVAMENTE!\n")