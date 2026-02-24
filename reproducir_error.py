import openpyxl
from openpyxl import Workbook
from FICHEROS.finalizar_excel import finalizar_excel
import os

# Crear un Excel de prueba simulando el output de save_to_excel
filename = "test_repro.xlsx"
wb = Workbook()
ws = wb.active
ws.title = "FACTURAS"

# Encabezados (16 columnas ahora)
columns = [
    "#", "Nombre Archivo", "Fecha Expedición",
    "Número Factura", "Nombre", "NIF", "COD POSTAL",
    "Base Imponible", "% IVA", "Cuota IVA", "Total Factura",
    "%Retención", "Retenciones", "Forma de Pago",
    "Observaciones", "Confianza"
]
ws.append(columns)
ws.append([""] * len(columns))
ws.append([""] * len(columns))

# Datos de prueba
# Fila 4
row_data = [
    1, "factura1.pdf", "01/01/2026",
    "F001", "Proveedor A", "B12345678", "33000",
    100.0, 21.0, 21.0, 121.0,
    0.0, 0.0, "Transferencia",
    "", 0.99
]
ws.append(row_data)

wb.save(filename)
print(f"Creado {filename} con {len(columns)} columnas")

# Ejecutar finalizar_excel
print("Ejecutando finalizar_excel...")
finalizar_excel(filename)
print("Finalizado sin errores?")
