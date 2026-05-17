flag_cliente = True
while flag_cliente == True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            print("Le dad tiene que se mayor a 0.")
        else:
            flag_cliente = False
    except:
        print("Debe ingresar su edad como numero entero.")
    
flag_tramo = True
while flag_tramo == True:
    try:
        tramo = input("Ingrese el tramo que esta inscrito (A, B, C o D): ").upper()
        if tramo == "A" or tramo == "B" or tramo == "C" or tramo == "D":
            flag_tramo = False
    except:
        print("El tramo debe ser (A,B,C,D)")

valor_medicamento_mensuales = 60000
valor_despacho_domicilio = 8000
        
valor_final_medicamento = 0
valor_final_despacho = 0
descuento_despacho= 0
descuento = 0
total = 0

if edad <= 30 and tramo in ("A", "B"):
    descuento = 0.18
elif edad <= 30 and tramo in ("C", "D"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("A", "B"):
    descuento = 0.12
elif edad >= 31 and edad <= 60 and tramo in ("C", "D"):
    descuento = 0.08
else:
    descuento = 0

if tramo == "A" or tramo == "B":
    if edad <= 55 and edad <= 60:
        descuento_despacho = 0.05
    else:
        descuento_despacho = 0.1

valor_final_medicamento = int(valor_medicamento_mensuales - (valor_medicamento_mensuales*descuento))
valor_final_despacho = int(valor_despacho_domicilio - (valor_despacho_domicilio*descuento_despacho))
total = valor_final_medicamento + valor_final_despacho

print(f"El valor del medicamento es: ${valor_final_medicamento}")
print(f"El valor de su despacho es: ${valor_final_despacho}")
print(f"El valor total del medicamnto y el despacho es: {total}")
