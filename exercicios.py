# Import statistics Library
import statistics
import math

#Inteiros (int)
### 1 #Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#v1 = int(input("Forneça o primeiro numero inteiro: "))
#v2 = int(input("Forneça o primeiro numero inteiro: "))
       
#print(f"A soma dos dois numeros inteiros é {v1 + v2}")       

### 2 #Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#v1 = int(input("Forneça o primeiro numero inteiro: "))

#print(f"O resto da divisao deste numero por 5 é {v1 % 5}")       

### 3 #Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#v1 = int(input("Forneça o primeiro numero inteiro: "))
#v2 = int(input("Forneça o primeiro numero inteiro: "))
       
#print(f"A multiplicacap dos dois numeros inteiros é {v1 * v2}")       


### 4 # Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#v1 = int(input("Forneça o primeiro numero inteiro: "))
#v2 = int(input("Forneça o primeiro numero inteiro: "))
       
#print(f"A divisao dos dois numeros inteiros é {v1 // v2}")       


### 5 # Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#v1 = int(input("Forneça o primeiro numero inteiro: "))
#print(f"O quadrado é {v1 ** 2}")    


#Números de Ponto Flutuante (float)
################################################################
### 1 # Escreva um programa que receba dois números flutuantes e realize sua adição.
#v1 = float(input("Forneça o primeiro numero DECIMAL: "))
#v2 = float(input("Forneça o primeiro numero DECIMAL: "))
       
#print(f"A divisao dos dois numeros inteiros é {v1 + v2}")       

### 2 #Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#v1 = 5
#v2 = 5
#media = statistics.mean([v1,v2])
       
#print(f"A media de {v1} e {v2} é {media}")       


#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
#base = 2.0  # Exemplo de entrada
#expoente = 3.0  # Exemplo de entrada
#potencia = base ** expoente
#print("O resultado da potência é:", potencia)

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em Celsius: "))
#celsius = 30.0  # Exemplo de entrada
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C é igual a {fahrenheit}°F")


#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = math.pi* raio ** 2

print(f"A área do círculo é: {area:.2f}")