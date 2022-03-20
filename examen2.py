import os
os.system("cls")

#ESCRIBIR VARIABLES NECESARIAS PARA EL CAJERO
saldo=int(0)
usuario=str.lower("admin")
contraseña=int("12345")
total=saldo
contador=0



#comenzar ingreso de u/c
#fbloqueo a 3 intentos listo 

while contador<3:
      usuario=input("Digite el usuario: ")
      contador=contador+1
      if str(usuario)== "admin":
            print("Usuario correcto")
            contraseña=input("ingrese su contraseña : ")
            if (contraseña)== "12345":
                  print("Bienvenido")
                  break      
            else:
                  print("Contraseña incorrecta")
                  if    contador==3:
                        quit(print("Sistema bloqueado"))
                        
      else:
            print("Usuario incorrecto")
            if    contador==3:
                  quit(print("sistema bloqueado"))
                  
            
      
#Menu de opciones 
#Bucle del menu listo 
while True:
      print(f"Seleccione la opcion\n\
1-Ingresar dinero:\n\
2-Retirar dinero:\n\
3-Ver saldo:\n\
4-Salir:")

      opcion=input()    
      
      if opcion=="1":
            ingreso=float(input(f"Digite el monto:"))
            saldo+=ingreso 
            print(f"Su saldo es de {saldo}:\n\
Monto depositado es:{total+saldo}")
                     
      if opcion=="2":
            egreso=float(input(f"Cuanto dinero desea retirar:"))
            
            print(f'Su retiro es de:{egreso}')

            if egreso>saldo:
                  print(f"Su saldo es insuficiente")
                  
            else:
                  saldo-=egreso
                  print(f"Su saldo es de: {saldo}")
                  

      if opcion=="3":
            print(f"Su saldo es de:{saldo}")

      if opcion=="4":
            quit(print("Gracias por preferirnos"))
      
            

    


