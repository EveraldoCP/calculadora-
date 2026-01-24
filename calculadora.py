import os

def mensagem_boas_vindas():
    print('----Bem vindos a calculadora em Python----')


def soma (num1, num2):
        return num1 + num2

def subtracao (num1, num2):
        return num1- num2

def multiplicacao (num1,num2):
        return num1 * num2
def divisao (num1,num2):
        if num2 ==0:
            return 'Erro,não é possível dividir por 0'
        else:
            return num1/num2


def exibir_opcoes():
    print('O que vamos fazer hoje?')
    print('1 somar')
    print('2 subtrair')
    print('3 multiplicar')
    print('4 dividir')


def escolha_operacao():
    opcao_escolhida = int(input('Escolha a operação: '))

    if opcao_escolhida == 1:    
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print(f'O resultado da soma é: {soma(num1,num2)}')
    else:
        os.system('clear')    

def main():
    mensagem_boas_vindas()
    exibir_opcoes()
    escolha_operacao()

if __name__ == '__main__':
    main()


