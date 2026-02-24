# -*- coding: utf-8 -*-
"""
Script de prueba para verificar que Gemini 3.0 Pro funciona correctamente
"""
import sys
sys.path.insert(0, '.')

import os
from pathlib import Path
from extractor import extract_invoice_data

# Configurar salida UTF-8
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

def probar_modelo():
    """Prueba rápida del modelo Gemini 3.0 Pro"""
    directorio = Path(r"c:\FACTURAS")
    
    # Buscar el primer archivo PDF o imagen
    archivos = []
    for ext in ['.pdf', '.jpg', '.jpeg', '.png']:
        archivos.extend(directorio.glob(f'*{ext}'))
        archivos.extend(directorio.glob(f'*{ext.upper()}'))
    
    if not archivos:
        print("No se encontraron archivos de prueba")
        return
    
    archivo_prueba = str(archivos[0])
    nombre = Path(archivo_prueba).name
    
    print("=" * 70)
    print("PRUEBA DE GEMINI 3.0 PRO")
    print("=" * 70)
    print(f"\nArchivo de prueba: {nombre}")
    print(f"Extrayendo datos con Gemini 3.0 Pro de '{nombre}' (Modo RECIBIDA)...\n")
    
    try:
        # Extraer con el modelo 3 Pro Preview
        data = extract_invoice_data(archivo_prueba, model_name="gemini-3-pro-preview", tipo_factura="recibida")
        
        print("=" * 70)
        print("RESULTADO:")
        print("=" * 70)
        
        if 'error' in data:
            print(f"\n[ERROR] {data['error']}\n")
            print("NOTA: Si el error indica que el modelo no existe,")
            print("      puede ser que aun no este disponible en tu region")
            print("      o que el nombre correcto sea diferente.")
        else:
            print(f"\n[OK] Modelo funcionando correctamente!")
            print(f"\nDatos extraidos:")
            print(f"  - Numero factura: {data.get('numero_factura')}")
            print(f"  - Fecha: {data.get('fecha_expedicion')}")
            print(f"  - NIF: {data.get('contraparte_nif')}")
            print(f"  - CP: {data.get('contraparte_cod_postal')}")
            print(f"  - Total: {data.get('total_factura')}")
            print(f"  - Confianza: {data.get('confidence_score')}")
        
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"\n[ERROR] {str(e)}\n")
        print("Si el error indica que el modelo no existe, es posible que:")
        print("  1. El nombre sea 'gemini-exp-3.0' o similar")
        print("  2. El modelo aun no este disponible en tu region")
        print("  3. Necesites actualizacion de la libreria")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    probar_modelo()
