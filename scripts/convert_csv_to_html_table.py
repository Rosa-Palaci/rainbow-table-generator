import csv

# Leer el CSV generado
with open('output/rainbow_table.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Saltar encabezado

    # Crear filas HTML
    rows = ""
    for row in reader:
        rows += "      <tr>\n"
        for cell in row:
            rows += f"        <td>{cell}</td>\n"
        rows += "      </tr>\n"

# Insertar en el archivo HTML
with open('dashboard/rainbow_table.html', 'r') as f:
    html = f.read()

# Reemplazar el contenido del <tbody>
new_html = html.replace("<tbody>\n\n    </tbody>", f"<tbody>\n{rows}    </tbody>")

# Guardar
with open('dashboard/rainbow_table.html', 'w') as f:
    f.write(new_html)

print("Tabla HTML actualizada con los datos del CSV.")
