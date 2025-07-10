print('--- Seja Bem Vindo(a) ---')
nome = input('Digite o seu nome: ')

def calcularMedia():
    n1 = int(input('Digite a sua primeira nota: '))
    n2 = int(input('Digite a sua segunda nota: '))
    n3 = int(input('Digite a sua terceira nota: '))
    media = (n1 + n2 + n3) / 3
    print ('\nSua média é: ', media)
    if media >= 15:
        print(nome, 'parabéns, você está aprovado(a)\n')
    elif media >= 7:
        print(nome, 'você está de recuperação\n')
    else:
        print(nome, 'você está reprovado(a)\n')

    repeticao = int(input("Você deseja calcular outra média? Digite: \n 1-Sim, 2-Não: "))
    if repeticao == 1:
        calcularMedia()
    else:
        print("\nObrigado por usar o nosso sistema!")

calcularMedia()