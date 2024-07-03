# Exercícios
# Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check), o uso de try-except para tratamento de exceções e a 
# utilização da estrutura condicional if. Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, 
# utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada 
# não for válida.

# try:
#     C = float(input("Digite a temperatura em graus Celsius "))
#     F = (C*9/5) + 32
#     print(f"{C} celsius equivale a {F} Fahrenheit")
# except ValueError as error:
#     print("Valor informado nao permitido")

    



# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# def inverter(txt):
#     return txt[::-1]


# entrada = input("Digite uma palavra ou uma frase: ")
# if isinstance(entrada,str):
#     palavra = entrada.replace(" ","").upper()
#     palavra_invertida = inverter(palavra)
#     print(f"{palavra}  e inverso {palavra_invertida}")
#     if palavra == palavra_invertida:
#         print(f"A {palavra_invertida} é um palíndromo")
#     else:
#         print(f"A {palavra_invertida} NAO é um palíndromo")
# else:
#     print("Valor informado nao permitido")



# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões 
# por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma
#  mensagem de erro apropriada.

# try:
#     numero1 = int(input("Digite um numero inteiro: "))
#     numero2 = int(input("Digite um numero inteiro: "))
#     if (numero1 % 2):
#        print(f"Primeiro numero é PAR")
#     else:
#        print(f"Primeiro numero é IMPAR")
#     if (numero1 < 0 or numero2 < 0): 
#        print("Numeros NEGATIVOS nao permitidos")
#     else:
#         oper = input("Digite a operacao desejada SOMA SUBTRACAO DIVISAO MULTIPLICACAO, utilize os operadores (+, -, *, /) para indica: ")
#         if oper == "+":
#            print(f"Resultado da soma de {numero1} pelo {numero2} é {numero1 + numero2}")
#         elif oper == "-":
#            print(f"Resultado da soma de {numero1} pelo {numero2} é {numero1 - numero2}")
#         elif oper == "*":
#            print(f"Resultado da soma de {numero1} pelo {numero2} é {numero1 * numero2}")
#         elif oper == "/" and numero2 != 0:
#            print(f"Resultado da soma de {numero1} pelo {numero2} é {numero1 / numero2}")
#         else:
#            print("Operacao Desconhecida ou Divisao por ZERO")   

# except ValueError:
#     print("Somente numero serão aceitos")   


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else
#  para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um
#  inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
print(f"entrada { entrada_lista}")
print(f"depois do split { numeros_str}")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")    

##############################################################################################
## Exercicio Extra de tratamento de erros

# nome = input("Digite seu nome: ")

# if nome.isdigit():
#    print("Voce digitou seu nome errado")
#    exit()
# elif len(nome) == 0:
#    print("Voce NAo digitou nada")   
#    exit()
# elif nome.isspace():   
#    print("Voce digitou somente espacos")   
#    exit()
# else:
#    print(f"Seu nome {nome}")  
