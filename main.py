"CALCULADORA SIMPLES EM PYTHON (v1.0)"

def calcular(escolha, valor1, valor2):
    resultado = 0
    
    match escolha:
        
        case 1:
            resultado = valor1 + valor2
            print(f"Valor somado: {valor1} + {valor2}\n\
                         Resultado: {resultado}")
        case 2:
            resultado = valor1 - valor2
            print(f"Valor subtraído: {valor1} - {valor2}\n\
                        Resultado: {resultado}")
        case 3:
            try:
                resultado = valor1 / valor2
                print(f"Valor dividido: {valor1} / {valor2}\n\
                            Resultado: {resultado}")
            except ZeroDivisionError:
                print("Não é possível dividir por ZERO!")

        case 4:
            resultado = valor1 * valor2
            print(f"Valor multiplicado: {valor1} * {valor2}\n\
                         Resultado: {resultado}")
        case _:
            print(f"{escolha} - Escolha um número da lista")
            calculadora()

def calculadora():
    
    while True:
        try:
            print("CALCULADORA PYTHON")
            categoria_escolhida = int(input("Escolha o que deseja fazer:\n"\
            "1-Somar\n"\
            "2-Subtrair\n"\
            "3-Dividir\n"\
            "4-Multiplicar\n"\
            "0-Sair\n"\
            "Digite um número da listagem acima: "))
            print("==================")
            
            if categoria_escolhida == 0:
                print("Saindo da calculadora... ")
                break

            if categoria_escolhida > 0 and categoria_escolhida < 5:

                primeiro_numero = float(input("Digite o primeiro número:"))
                print(f"Você escolheu o primeiro valor de número: {primeiro_numero}")

                segundo_numero = float(input("Digite o segundo número:"))
                print(f"Você escolheu o segundo valor de número: {segundo_numero}")

                calcular(categoria_escolhida, primeiro_numero, segundo_numero)
            else:
                print("Digite um número de acordo com a listagem anterior.")

        except ValueError:
            print("Entrada inválida.")

calculadora()