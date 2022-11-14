from M_G_1 import M_G_1
from M_D_1 import M_D_1
from M_M_1 import M_M_1
from M_M_S import M_M_S
from M_M_S_K import M_M_S_K
from M_Ek_1 import M_Ek_1
from Color import bcolors


print(bcolors.OKBLUE + "Bienvenido al simulador de Modelo De Colas" + bcolors.ENDC)

ending = False

while (not ending):
    print("")
    print("Selecciona el modelo que desea simular")
    print("1. M/M/1")
    print("2. M/M/S")
    print("3. M/M/S/K")
    print("4. M/G/1")
    print("5. M/D/1")
    print("6. M/Ek/1")
    print("Introduce otro valor para terminar el programa.")
    print("")

    choice = input("Elige el modelo a aplicar: ")
    try:
        choice = int(choice)
    except:
        print("Terminando el programa...")
        ending = True
        continue
    print("")
    if choice == 1:
        local_ending = False
        print(bcolors.OKBLUE + "M/M/1" + bcolors.ENDC)
        while(not local_ending):
            print("")

            avg = input("Introduce la tasa media de llegadas: ")
            try:
                avg = float(avg)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (avg <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue


            miu = input("Introduce el tasa media de servicio: ")
            try:
                miu = float(miu)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (miu <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            n = input("Introduce el número de clientes a analizar: ")
            try:
                n = int(n)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (n <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            if (avg >= (1 * miu)):
                print(bcolors.FAIL + "Error: El sistema no es estable. El promedio de llegadas = " + str(avg) + " debe ser menor que la tasa de servicio = " + str(miu) + "." + bcolors.ENDC)
                continue

            mm1 = M_M_1(avg, miu, n)

            if (mm1.rho < 0 or mm1.rho > 1):
                print(bcolors.FAIL + "Error: El sistema no es estable. Rho = " + str(mm1.rho) + " debe estar entre 0 y 1"  + bcolors.ENDC)
                continue
            else:
                print(bcolors.OKGREEN + "Los Valores introducidos son correctos." + bcolors.ENDC)

            print("")


            print("Probabilidad de que haya " + str(mm1.n) + " clientes en el sistema. (Pn): " + str(mm1.pn))
            print("")
            print("Número esperado de clientes en la cola (excluye los que están en servicio). (Lq): " + str(mm1.lq))
            print("")
            print("Número esperado de clientes en el sistema. (L): " + str(mm1.l))
            print("")
            print("Tiempo esperado de los clientes en la cola (excluye el tiempo de servicio). (Wq): " + str(mm1.wq))
            print("")
            print("Tiempo esperado de estancia de los clientes en el sistema (incluye el tiempo de servicio). (W): " + str(mm1.w))

            print("")
            print("Valores adicionales de calculo:")
            print("Ro: " + str(mm1.rho))
            print("P0: " + str(mm1.p0))

            print("")
            print(bcolors.OKBLUE + "¿Desea realizar otra simulación? (s/n)" + bcolors.ENDC)
            answer = input("")
            if (answer != "s"):
                local_ending = True

    elif choice == 2:
        local_ending = False
        print(bcolors.OKBLUE + "M/M/S" + bcolors.ENDC)
        while(not local_ending):
            print("")

            avg = input("Introduce la tasa media de llegadas: ")
            try:
                avg = float(avg)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (avg <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue


            miu = input("Introduce el tasa media de servicio: ")
            try:
                miu = float(miu)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (miu <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            s = input("Introduce el número de servidores: ")
            try:
                s = int(s)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (s <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            n = input("Introduce el número de clientes a analizar: ")
            try:
                n = int(n)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (n <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            if (avg >= (s * miu)):
                print(bcolors.FAIL + "Error: El sistema no es estable. El promedio de llegadas = " + str(avg) + " debe ser menor que la tasa de servicio = " + str(miu) + "." + bcolors.ENDC)
                continue

            mms = M_M_S(avg, miu, s, n)

            if (mms.rho < 0 or mms.rho > 1):
                print(bcolors.FAIL + "Error: El sistema no es estable. Rho = " + str(mms.rho) + " debe estar entre 0 y 1"  + bcolors.ENDC)
                continue
            else:
                print(bcolors.OKGREEN + "Los Valores introducidos son correctos." + bcolors.ENDC)

            print("")


            print("Probabilidad de que haya " + str(mms.n) + " clientes en el sistema. (Pn): " + str(mms.pn))
            print("")
            print("Número esperado de clientes en la cola (excluye los que están en servicio). (Lq): " + str(mms.lq))
            print("")
            print("Número esperado de clientes en el sistema. (L): " + str(mms.l))
            print("")
            print("Tiempo esperado de los clientes en la cola (excluye el tiempo de servicio). (Wq): " + str(mms.wq))
            print("")
            print("Tiempo esperado de estancia de los clientes en el sistema (incluye el tiempo de servicio). (W): " + str(mms.w))

            print("")
            print("Valores adicionales de calculo:")
            print("Ro: " + str(mms.rho))
            print("P0: " + str(mms.p0))

            print("")
            print(bcolors.OKBLUE + "¿Desea realizar otra simulación? (s/n)" + bcolors.ENDC)
            answer = input("")
            if (answer != "s"):
                local_ending = True
    
    elif choice == 3:
        local_ending = False
        print(bcolors.OKBLUE + "M/M/S/K" + bcolors.ENDC)
        while(not local_ending):
            print("")

            avg = input("Introduce la tasa media de llegadas: ")
            try:
                avg = float(avg)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (avg <= 0 or not avg.is_integer()):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue


            miu = input("Introduce el tasa media de servicio: ")
            try:
                miu = float(miu)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (miu <= 0 or not miu.is_integer()):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            s = input("Introduce el número de servidores: ")
            try:
                s = int(s)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (s < 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            
            k = input("Introduce K: ")
            try:
                k = int(k)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (k <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            n = input("Introduce el número de clientes a analizar: ")
            try:
                n = int(n)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (n <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            if (avg >= (s * miu)):
                print(bcolors.FAIL + "Error: El sistema no es estable. El promedio de llegadas = " + str(avg) + " debe ser menor que la tasa de servicio = " + str(miu) + "." + bcolors.ENDC)
                continue

            mmsk = M_M_S_K(avg, miu, s, k, n)

            if (mmsk.rho < 0 or mmsk.rho > 1):
                print(bcolors.FAIL + "Error: El sistema no es estable. Rho = " + str(mmsk.rho) + " debe estar entre 0 y 1"  + bcolors.ENDC)
                continue
            else:
                print(bcolors.OKGREEN + "Los Valores introducidos son correctos." + bcolors.ENDC)

            print("")


            print("Probabilidad de que haya " + str(mmsk.n) + " clientes en el sistema. (Pn): " + str(mmsk.pn))
            print("")
            print("Número esperado de clientes en la cola (excluye los que están en servicio). (Lq): " + str(mmsk.lq))
            print("")
            print("Número esperado de clientes en el sistema. (L): " + str(mmsk.l))
            print("")
            print("Tiempo esperado de los clientes en la cola (excluye el tiempo de servicio). (Wq): " + str(mmsk.wq))
            print("")
            print("Tiempo esperado de estancia de los clientes en el sistema (incluye el tiempo de servicio). (W): " + str(mmsk.w))

            print("")
            print("Valores adicionales de calculo:")
            print("Ro: " + str(mmsk.rho))
            print("P0: " + str(mmsk.p0))
            print("lambdaE: " + str(mmsk.le))
            print("Pk: " + str(mmsk.pk))

            print("")
            print(bcolors.OKBLUE + "¿Desea realizar otra simulación? (s/n)" + bcolors.ENDC)
            answer = input("")
            if (answer != "s"):
                local_ending = True

    elif choice == 4:
        local_ending = False
        print(bcolors.OKBLUE + "M/G/1" + bcolors.ENDC)
        while(not local_ending):
            print("")

            avg = input("Introduce la tasa media de llegadas: ")
            try:
                avg = float(avg)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (avg <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue


            miu = input("Introduce el tasa media de servicio: ")
            try:
                miu = float(miu)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (miu <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            std_dev = input("Introduce la desviación estándar: ")
            try:
                std_dev = float(std_dev)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un valor entre 0 y 1" + bcolors.ENDC)
                continue
            if (std_dev < 0 or std_dev > 1):
                print(bcolors.FAIL + "Error: Debe introducir un valor entre 0 y 1" + bcolors.ENDC)
                continue

            n = input("Introduce el número de clientes a analizar: ")
            try:
                n = int(n)
            except:
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue
            if (n <= 0):
                print(bcolors.FAIL + "Error: Debe introducir un número entero positivo" + bcolors.ENDC)
                continue

            if (avg >= (1 * miu)):
                print(bcolors.FAIL + "Error: El sistema no es estable. El promedio de llegadas = " + str(avg) + " debe ser menor que la tasa de servicio = " + str(miu) + "." + bcolors.ENDC)
                continue

            mg1 = M_G_1(avg, miu, std_dev, n)

            if (mg1.rho < 0 or mg1.rho > 1):
                print(bcolors.FAIL + "Error: El sistema no es estable. Rho = " + str(mg1.rho) + " debe estar entre 0 y 1"  + bcolors.ENDC)
                continue
            else:
                print(bcolors.OKGREEN + "Los Valores introducidos son correctos." + bcolors.ENDC)

            print("")


            print("Probabilidad de que haya " + str(mg1.n) + " clientes en el sistema. (Pn): " + str(mg1.pn))
            print("")
            print("Número esperado de clientes en la cola (excluye los que están en servicio). (Lq): " + str(mg1.lq))
            print("")
            print("Número esperado de clientes en el sistema. (L): " + str(mg1.l))
            print("")
            print("Tiempo esperado de los clientes en la cola (excluye el tiempo de servicio). (Wq): " + str(mg1.wq))
            print("")
            print("Tiempo esperado de estancia de los clientes en el sistema (incluye el tiempo de servicio). (W): " + str(mg1.w))

            print("")
            print("Valores adicionales de calculo:")
            print("Ro: " + str(mg1.rho))
            print("P0: " + str(mg1.p0))

            print("")
            print(bcolors.OKBLUE + "¿Desea realizar otra simulación? (s/n)" + bcolors.ENDC)
            answer = input("")
            if (answer != "s"):
                local_ending = True
            



    elif (choice == 2):
        print("M/D/1")
        print("")

        avg = float(input("Enter the average number of customers: "))
        miu = float(input("Enter the average service time: "))
        n = int(input("Enter the number of customers"))
    