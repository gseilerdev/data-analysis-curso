fecha = "2024-11-14"
vendedor = "Carlos Méndez"
ventas = [45000, 32000, 67500, 28000, 91000]
producto_estrella = "Auriculares Bluetooth"

# Tu tarea: construir este reporte
# Reporte de ventas — 2024-11-14
# Vendedor: Carlos Méndez
# Total ventas: $263500
# Promedio por venta: $52700.0
# Producto estrella: Auriculares Bluetooth

total_ventas = sum(ventas)
promedio_ventas = total_ventas / len(ventas)

reporte = f"Reporte de ventas - {fecha}\n Vendedor: {vendedor}\n Total ventas: ${total_ventas}\n Promedio por venta: ${promedio_ventas}\n Producto estrella:{producto_estrella}"

print(reporte)
