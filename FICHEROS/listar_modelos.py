# -*- coding: utf-8 -*-
"""
Listar modelos Gemini disponibles
"""
import sys
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Configurar salida UTF-8
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

# Cargar variables de entorno
load_dotenv()

# Configurar API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("ERROR: No se encontró GEMINI_API_KEY")
    sys.exit(1)

genai.configure(api_key=API_KEY)

print("=" * 80)
print("MODELOS GEMINI DISPONIBLES")
print("=" * 80)
print()

try:
    modelos = genai.list_models()
    
    # Filtrar solo modelos que soporten generateContent
    modelos_generativos = [m for m in modelos if 'generateContent' in m.supported_generation_methods]
    
    print(f"Total de modelos con generateContent: {len(modelos_generativos)}\n")
    
    for i, model in enumerate(modelos_generativos, 1):
        print(f"{i}. {model.name}")
        print(f"   Nombre corto: {model.name.replace('models/', '')}")
        if hasattr(model, 'display_name'):
            print(f"   Display: {model.display_name}")
        if hasattr(model, 'description'):
            desc = model.description[:80] if len(model.description) > 80 else model.description
            print(f"   Descripcion: {desc}")
        print()
    
    # Recomendar modelos
    print("=" * 80)
    print("MODELOS RECOMENDADOS PARA EXTRACCION DE FACTURAS:")
    print("=" * 80)
    
    nombres = [m.name.replace('models/', '') for m in modelos_generativos]
    
    # Buscar el mejor modelo
    if any('gemini-2.0-flash-exp' in n for n in nombres):
        print("\n[RECOMENDADO] gemini-2.0-flash-exp  - Experimental, más potente")
    elif any('gemini-2.0-flash' in n for n in nombres):
        print("\n[RECOMENDADO] gemini-2.0-flash  - Rapido y eficiente")
    
    if any('gemini-1.5-pro' in n for n in nombres):
        print("[ALTERNATIVA] gemini-1.5-pro  - Mas preciso pero mas lento")
    
    if any('gemini-exp' in n for n in nombres):
        print("\nModelos experimentales disponibles:")
        for nombre in nombres:
            if 'exp' in nombre.lower():
                print(f"  - {nombre}")
    
    print("\n" + "=" * 80)
    
except Exception as e:
    print(f"Error al listar modelos: {e}")
    import traceback
    traceback.print_exc()
