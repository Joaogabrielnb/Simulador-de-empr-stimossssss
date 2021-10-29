while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("    SIMULADOR DE EMPRÉSTIMO    ")
    print("-------------------------------")

    cliente = str(input("Olá. Qual opção você gostaria de realizar ? [1º] Tesouro pré fixado 2024/[2º] Tesouro pré fixado 2026.:  "))

    if cliente == '1':
     valor = int(input("Qual o valor você quer investir?:  "))
     valorm =int(input("Se você for investir todo o mês (aporte mensal), qual será o valor?:  "))
     
     
     valorp = (valorm*32) + valor
     ir = (valorp*7.5)/100
     IR = valorp - ir
     b3 = (valorp*7.5)/100
     valorTotal = valorp 
     
     
     print("-------------------------------")
     print("   RESULTADO DA SIMULAÇÃO      ")
     print("-------------------------------")    
     print("Valor do ínicio da simulação: R$ ", valor)
     print("Valor investido por mês de: R$", valorm,"em 32 meses")
     print("Valor total investido: R$ ",valorp)
     print("-------------------------------")
     print("Valor bruto: R$ ", IR)
     print("-------------------------------")
     resetar = str(input("Deseja realizar outra simulação? s/n: "))


    else :
     valor = int(input("Qual o valor você quer investir?:  "))
     valorm =int(input("Se você for investir todo o mês (aporte mensal), qual será o valor?:  "))
     
     
     valorp = (valorm*50) + valor
     ir = (valorp*7.5)/100
     IR = valorp - ir
     b3 = (valorp*7.5)/100
     valorTotal = valorp + lucro
     
     
     print("-------------------------------")
     print("   RESULTADO DA SIMULAÇÃO      ")
     print("-------------------------------")    
     print("Valor do ínicio da simulação: R$ ", valor)
     print("Valor investido por mês: R$", valorm,"em 50 meses")
     print("Valor total investido: R$ ",valorp)
     print("-------------------------------")
     print("Valor bruto: R$ ", IR)
     print("-------------------------------")
     resetar = str(input("Deseja realizar outra simulação? s/n: "))

     if resetar == 'n':
         break
     print ("Programa encerrado !")
