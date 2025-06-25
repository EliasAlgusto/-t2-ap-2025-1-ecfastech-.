nome=input("Digite seu nome(maior que 3 caracteres):")
if len(nome)>3:
    print("Nome valido,pode ir para o procimo")
else:
    print("Nome curto, precisa de mais 3 letras.")
idade=int(input("Digite sua idade(entre 0 e 150):"))
if 0<=idade<=150:
    print("idade valida")
else:
    print("idade invalida, tem que ser entre 0 e 150")
salario=float(input("Digite o salario(maior que zero):"))
if salario> 0:
   print("Salario valido")
else:
   print("Salario invalido, tem que ser maior que zero")


sexo=input("Digite o sexo(F para feminino e M para masculino):")
if sexo in('f' , 'm'):
   print("sexo valido")
else:
   print("sexo invalido! Digite apenas F ou M")
estado_civil=input("Digite seu estado civil(S, C, V, ou D):")
if estado_civil in ('s', 'c', 'v', 'd'):
   print("estado civil valido")
else:
   print("estado civil invalido! Digite apenas 'S', 'C', 'V', ou 'D'.")
