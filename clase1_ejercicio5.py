usuarios_activos = "1523"
ingresos_totales = 847320.50
tasa_conversion = "3.7"
nombre_campania = "BlackFriday2024"

# Estas operaciones fallan — ¿por qué? ¿cómo las corriges?
ingreso_por_usuario = ingresos_totales / int(usuarios_activos)
tasa_decimal = float(tasa_conversion) / 100
resumen = "Campaña " + nombre_campania + " | Conversión: " + str(tasa_conversion) + "% | Ingreso/usuario: $" + str(ingreso_por_usuario)
print(resumen)
