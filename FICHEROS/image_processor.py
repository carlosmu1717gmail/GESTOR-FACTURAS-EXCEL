from PIL import Image, ImageEnhance, ImageFilter
import os

def preprocesar_imagen(input_path, output_path=None):
    """
    Mejora la calidad de una imagen antes de enviarla a Gemini.
    
    Optimizaciones:
    - Mejora de contraste
    - Aumento de nitidez
    - Reducción de ruido
    - Conversión a escala de grises si es necesario
    
    Args:
        input_path: Ruta de la imagen original
        output_path: Ruta donde guardar la imagen mejorada (opcional)
    
    Returns:
        Ruta de la imagen mejorada
    """
    try:
        # Solo procesar imágenes, no PDFs
        if input_path.lower().endswith('.pdf'):
            return input_path
        
        # Abrir imagen
        img = Image.open(input_path)
        
        # Convertir a RGB si es necesario
        if img.mode not in ('RGB', 'L'):
            img = img.convert('RGB')
        
        # 1. Mejorar contraste (1.3x - moderado para no perder información)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.3)
        
        # 2. Mejorar nitidez (1.5x - hace el texto más legible)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.5)
        
        # 3. Reducir ruido (suavizado ligero)
        # img = img.filter(ImageFilter.MedianFilter(size=3))  # Desactivado: puede difuminar texto pequeño
        
        # 4. Ajustar brillo si la imagen está muy oscura o clara
        enhancer = ImageEnhance.Brightness(img)
        # Analizar brillo promedio
        grayscale = img.convert('L')
        stat = grayscale.getextrema()
        avg_brightness = sum(stat) / 2
        
        # Si está muy oscura, aclarar un poco
        if avg_brightness < 80:
            img = enhancer.enhance(1.2)
        # Si está muy clara, oscurecer un poco
        elif avg_brightness > 200:
            img = enhancer.enhance(0.9)
        
        # Guardar imagen mejorada
        if output_path is None:
            # Crear archivo temporal en el mismo directorio
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_optimized{ext}"
        
        # Guardar con calidad alta
        img.save(output_path, quality=95, optimize=True)
        
        return output_path
        
    except Exception as e:
        # Si falla el preprocesamiento, devolver original
        print(f"⚠️ Preprocesamiento falló para {input_path}: {e}")
        return input_path

def limpiar_imagenes_temporales(directorio="."):
    """Elimina imágenes optimizadas temporales"""
    try:
        for archivo in os.listdir(directorio):
            if '_optimized' in archivo:
                try:
                    os.remove(os.path.join(directorio, archivo))
                except:
                    pass
    except:
        pass
