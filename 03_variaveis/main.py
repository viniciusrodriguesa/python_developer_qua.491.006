#  declaração de variáveis

texto: str = 'Este é um texto.' # string
numero_inteiro: int = 18 # int
numero_decimal: float = 7.5 # float
programador: bool = True #bool

# saída de dados

print(type(texto))
print(type(numero_inteiro))
print(type(numero_decimal))
print(type(programador))

numero = 10
numero = str(numero)

print(type(numero))

numero = float(numero)

print(type(numero))

numero = int(numero)

print(type(numero))

#variáveis

nome= "Vinícius"
idade = 28
altura = 1.82

# saída de dados

print('Olá, meu nome é ' + nome + ", tenho " + str(idade) + " anos, e tenho " + str(altura) + " metros de altura")

print("Olá, meu nome é", nome, ", tenho ", idade, "anos, e tenho", altura, "metros de altura.")

print('Olá, meu nome é {}, tenho {} anos, e tenho {} metros de altura.'.format(nome, idade, altura))

print(f'Olá, meu nome é {nome}, tenho {idade} anos, e tenho {idade} metros de altura.')

print("Valor da variável:", texto, ". Tipo de dado:", type(texto))

print("Valor da variável:", numero_inteiro, ". Tipo de dado:", type(numero_inteiro))

print("Valor da variável:", numero_decimal, ". Tipo de dado:", type(numero_decimal))

print("Valor da variável:", programador, ". Tipo de dado:", type(programador))



# Alterando vírgula para ponto
valor_decimal = input('Informe um número decimal: ')
valor_decimal = valor_decimal.replace(',', '.')
valor_decimal = float(valor_decimal)

# Exercícios
# 1. Crie um arquivo .py e faça um algoritmo que receba do usuário o nome, idade e profissão, e imprima na tela essas informações.
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
profissao = input("Informe sua profissão: ")

print(f"Meu nome é {nome}, tenho {idade} anos, e minha profissão é {profissao}")


