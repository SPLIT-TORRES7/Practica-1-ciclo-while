cont_corr = "Gustambo university"
while True:
    for i in range(5):
        cont_usu = input(f"Dame la contraseña") 
        if cont_corr == cont_usu: 
            print("Contraseña correcta")
            break
        print(f"Contraseña incorrecta, intento{i+1}")
    else:
        print("Contraseña incorrecta")
    
    break 