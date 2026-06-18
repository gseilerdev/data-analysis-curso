anio = 2024
pais = "AR"
tipo_transaccion = "compra"
numero = 847

# Resultado esperado: "2024-AR-COMPRA-000847"
# Pista: investigá el método .zfill() o el formateo con f-strings {numero:06d}

transaction_id = f"{anio}-{pais}-{tipo_transaccion.upper()}-{numero:06d}"
print(transaction_id)
     