# Datos tal como llegan del sistema externo (todo string)
precio_str = "15990"
descuento_str = "0.15"
cantidad_str = "4"
tiene_iva_str = "True"

# Tu tarea:
# 1. Convierte cada variable al tipo correcto (int, float, bool)
# 2. Calcula el precio final con descuento
# 3. Si tiene IVA, suma un 21% adicional
# 4. Imprime el total para la cantidad indicada

precio = int(precio_str)
descuento = float(descuento_str)
cantidad = int(cantidad_str)
tiene_iva = tiene_iva_str == "True"

importe_descuento = precio * descuento

precio_final = precio - importe_descuento
if tiene_iva == True:
    precio_final_con_iva = precio_final * 1.21
else:
    precio_final_con_iva = precio_final


print(f"Precio total para {cantidad} unidades: {precio_final_con_iva * cantidad}")

