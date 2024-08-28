
Aula 6 - Travis-CI
Ezequiel Manuel Muxito
•
17:32

Aula_6_DevOps.pdf
PDF

testes.py
Texto

code.py
Texto

jogos.py
Texto

Microsoft Teams
https://teams.live.com/meet/9326961028076?p=k0EXE7QB6VLkgI8GnS
Comentários da turma

Adicionar comentário para a turma...

def inicializar():
	tab = []
	for i in range(3):
		linha = []
		for j in range(3):
			linha.append(".")
		tab.append(linha)
	return tab

def main():
	jogo = inicializar()
	print(jogo)

if __name__ == "__main__":
	main()