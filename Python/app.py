def main():
    print('-=='*12)
    print('CALCULADORA DO JAPA')
    print('-=='*12)
    def soma():
        return num_1 + num_2
    def sub():
        return num_1 - num_2
    def mult():
        return num_1 * num_2
    def div():
        return num_1 / num_2
    def power():
        return num_1 ** num_2
    def raiz():
        return num_1 ** (1/num_2)


    while True:
        num_1 = float(input("Digite o primeiro valor: "))
        num_2 = float(input("Digite o segundo valor: "))
        print('-=='*12)
        print('1. Somar')
        print('2. Subtrair')
        print('3. Multiplicar')
        print('4. Potenciar')
        print('5. Enraizar')
        print('6. Voltar')
        print('7. Sair')
        print('-=='*12)
        operaçao = int(input('Que operação deseja atribuir com {} e {}? '.format(num_1,num_2)))
        if operaçao == 1:
            print('O resultado da soma é {}'.format(soma()))
        elif operaçao == 2:
            print('O resultado da subtração é {}'.format(sub()))
        elif operaçao == 3:
            print('O resultado da multiplicação é {}'.format(mult()))
        elif operaçao == 4:
            print('O resultado da potencição é {}'.format(div()))
        elif operaçao == 5:
            print('O resultado da raiz é {}'.format(raiz()))
        elif operaçao == 6:
            return main()
        elif operaçao == 7:
            print('-=='*12)
            print('Até mais!')
            break
        else:
            print('Insira uma opção válida.')
            
     

if __name__== "__main__":
    main()