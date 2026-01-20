import sys
import json
import os
from extractor import extract_invoice_data

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_a_la_factura>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"❌ El archivo no existe: {file_path}")
        sys.exit(1)
        
    print(f"Analizando factura: {file_path} ...")
    
    # Extraer datos (Se puede cambiar el modelo aquí si Google lanza 'gemini-3-pro' oficialmente)
    data = extract_invoice_data(file_path, model_name="gemini-3-pro-preview")
    
    # Imprimir resultado JSON indentado
    print(json.dumps(data, indent=2, ensure_ascii=False))
    
    # Guardar en Excel
    from excel_writer import save_to_excel
    # Añadir nombre de archivo a los datos para que salga en el excel
    data["file_name"] = os.path.basename(file_path)
    save_to_excel(data)

if __name__ == "__main__":
    main()
