import pandas as pd

# Ruta del CSV generado con los hashes
csv_path = 'output/rainbow_table.csv'

# Leer el archivo CSV
df = pd.read_csv(csv_path)

# Guardar como archivo Excel
excel_path = 'output/rainbow_table_hashes.xlsx'
df.to_excel(excel_path, index=False)

print(f"Archivo Excel exportado correctamente a: {excel_path}")
