##############Strings (str)
###1) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#nome_rua = input("Forneça o o nome da rua: ")
#nome_rua = nome_rua.upper()
#print(f"Nome da ruas em maiusculas: {nome_rua}")


###2) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#nome_rua = input("Forneça o o nome da rua: ")
#nome_rua = nome_rua.lower()
#print(f"Nome da ruas em minúsculas: {nome_rua}")

###3) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#frase = input("Forneça uma frase: ")
#frase = frase.strip()
#print(f"Nome da ruas em minúsculas: {frase}")


###4) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#input("Insira uma data no formato dd/mmm/aaaa: ")

data_do_usuario = "20/12/2024"
data_separada = data_do_usuario.split("/")
print(f"Data Informada: {data_separada}")
print(f"Dia: {data_separada[0]}")
print(f"Mes: {data_separada[1]}")
print(f"Ano: {data_separada[2]}")


#5) Escreva um programa que concatene duas strings fornecidas pelo usuário.