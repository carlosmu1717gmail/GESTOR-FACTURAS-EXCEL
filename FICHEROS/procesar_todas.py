# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
from extractor import extract_invoice_data
from excel_writer import inicializar_excel, save_to_excel, finalizar_y_guardar_excel
from finalizar_excel import finalizar_excel
from cache_manager import CacheManager
from image_processor import preprocesar_imagen, limpiar_imagenes_temporales

# Asegurar que stdout use UTF-8
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
import json

def generar_nombre_archivo():
    """
    Genera un nombre de archivo numerado (facturas01.xlsx, facturas02.xlsx, etc.)
    """
    contador = 1
    while True:
        nombre = f"facturas{contador:02d}.xlsx"
        if not os.path.exists(nombre):
            return nombre
        contador += 1

def procesar_todas_facturas(directorio_facturas):
    """
    Procesa todas las facturas (PDF/JPG/PNG) de un directorio.
    OPTIMIZADO con caché y pre-procesamiento de imágenes.
    """
    # Inicializar gestor de caché
    cache = CacheManager()
    
    # Usar Path para mejor manejo de rutas Unicode
    directorio = Path(directorio_facturas)
    
    # Buscar todos los archivos con extensiones válidas
    extensiones_validas = ['.pdf', '.jpg', '.jpeg', '.png']
    archivos = []
    
    try:
        # Path.glob maneja UTF-8 automáticamente
        for ext in extensiones_validas:
            # Buscar tanto minúsculas como mayúsculas
            archivos.extend(directorio.glob(f'*{ext}'))
            archivos.extend(directorio.glob(f'*{ext.upper()}'))
        
        # Eliminar duplicados y convertir a strings
        archivos = sorted(list(set(str(f) for f in archivos)))
    
    except Exception as e:
        print(f"Error al listar archivos: {e}")
        return
    
    if not archivos:
        print(f"No se encontraron facturas en: {directorio_facturas}")
        return
    
    print(f"===================================================")
    print(f"  MODO OPTIMIZADO: Caché + Pre-procesamiento")
    print(f"  Procesando {len(archivos)} factura(s)")
    print(f"  Modelo: gemini-3-pro-preview (máxima precisión)")
    print(f"===================================================")
    
    # Generar nombre de archivo numerado
    nombre_excel = generar_nombre_archivo()
    print(f"\n   Archivo de salida: {nombre_excel}\n")
    
    # Inicializar Excel
    inicializar_excel(nombre_excel)
    
    procesadas = 0
    errores = 0
    desde_cache = 0
    
    # Diccionario para detectar duplicados
    facturas_vistas = {}
    datos_facturas = []
    
    # FASE 1: Extraer todas las facturas (con caché y pre-procesamiento)
    print("   Fase 1: Extrayendo datos (con optimizaciones)...")
    for archivo in archivos:
        try:
            nombre_archivo = Path(archivo).name
            print(f"[{len(datos_facturas) + 1}/{len(archivos)}] {nombre_archivo}", end="")
        except Exception:
            print(f"[{len(datos_facturas) + 1}/{len(archivos)}] <error en nombre>", end="")
        
        try:
            # OPTIMIZACIÓN 1: Verificar si está en caché
            cached_data = cache.get_cached_data(archivo)
            
            if cached_data:
                # Recuperar desde caché (velocidad x10)
                print(" ⚡ CACHE")
                data = cached_data
                desde_cache += 1
            else:
                # No está en caché: procesar normalmente
                # OPTIMIZACIÓN 2: Pre-procesar imagen antes de enviar a Gemini
                archivo_procesado = preprocesar_imagen(archivo)
                
                # Extraer datos con Gemini 3 Pro Preview
                data = extract_invoice_data(archivo_procesado, model_name="gemini-3-pro-preview")
                
                # Limpiar imagen temporal si se creó
                if archivo_procesado != archivo:
                    try:
                        os.remove(archivo_procesado)
                    except:
                        pass
                
                # Guardar en caché para próximas ejecuciones
                cache.save_to_cache(archivo, data)
                print(" ✅ PROCESADO")
            
            # Añadir nombre de archivo
            data["file_name"] = Path(archivo).name
            datos_facturas.append(data)
            
        except Exception as e:
            print(f" ❌ ERROR: {e}\n")
            errores += 1
    
    # Limpiar imágenes temporales que puedan haber quedado
    limpiar_imagenes_temporales(directorio_facturas)
    
    # FASE 2: Detectar duplicados
    print("\n   Fase 2: Detectando duplicados...")
    for data in datos_facturas:
        nif = data.get("contraparte_nif")
        fecha = data.get("fecha_expedicion")
        numero = data.get("numero_factura")
        total = data.get("total_factura")
        
        clave = (nif, fecha, numero, total)
        
        if clave in facturas_vistas:
            issues = data.get("issues", [])
            if isinstance(issues, list):
                issues.append("FACTURA_DUPLICADA")
            else:
                issues = ["FACTURA_DUPLICADA"]
            data["issues"] = "FACTURA_DUPLICADA"
        else:
            facturas_vistas[clave] = True
    
    # FASE 3: Guardar en Excel
    print("\n   Fase 3: Guardando en Excel...")
    for data in datos_facturas:
        try:
            save_to_excel(data, nombre_excel)
            procesadas += 1
        except Exception as e:
            print(f"   ERROR al guardar: {e}")
            errores += 1
    
    # Finalizar y guardar Excel
    finalizar_y_guardar_excel(nombre_excel)
    
    print(f"===================================================")
    print(f"  RESUMEN:")
    print(f"  Procesadas correctamente: {procesadas}")
    print(f"  Desde caché (instantáneas): {desde_cache}")
    print(f"  Nuevas (Gemini): {procesadas - desde_cache}")
    print(f"  Errores: {errores}")
    print(f"===================================================")
    
    # Finalizar Excel: añadir totales y crear hoja de proveedores
    if procesadas > 0:
        finalizar_excel(nombre_excel)

if __name__ == "__main__":
    directorio = r"c:\FACTURAS"
    procesar_todas_facturas(directorio)
