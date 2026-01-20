# 📄 AutoGestor Facturas

Sistema inteligente de extracción y gestión de datos de facturas usando IA (Google Gemini 3 Pro).

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Características

- ✅ **Extracción automática con IA**: Utiliza Gemini 3 Pro para extraer datos de facturas (PDF, JPG, PNG)
- ✅ **Sistema de caché inteligente**: Evita reprocesar facturas ya analizadas
- ✅ **Pre-procesamiento de imágenes**: Mejora automática de contraste y nitidez
- ✅ **Exportación a Excel**: Genera hojas "FACTURAS" y "PROVEEDORES" con totales y desglose por IVA
- ✅ **Interfaz web opcional**: Streamlit UI para arrastrar y soltar facturas
- ✅ **Multi-IVA**: Maneja facturas con múltiples tipos de IVA
- ✅ **Detección de duplicados**: Identifica facturas repetidas automáticamente

## 📋 Requisitos

- Python 3.9+
- API Key de Google Gemini (gratuita en [ai.google.dev](https://ai.google.dev))

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/AutoGestorFacturas.git
cd AutoGestorFacturas
```

### 2. Instalar dependencias
```bash
pip install -r FICHEROS/requirements.txt
```

### 3. Configurar API Key
Crea un archivo `.env` en la raíz del proyecto:
```env
GEMINI_API_KEY=tu_clave_api_aqui
```

## 💻 Uso

### Modo Línea de Comandos

1. Coloca tus facturas (PDF/JPG/PNG) en `c:\FACTURAS`
2. Ejecuta el batch:
```bash
PROCESAR_FACTURAS.bat
```
3. El archivo Excel se generará como `facturasXX.xlsx`

### Modo Interfaz Web

1. Lanza la aplicación web:
```bash
LANZAR_WEB.bat
```
2. Abre tu navegador en `http://localhost:8501`
3. Arrastra y suelta tus facturas
4. Descarga el Excel generado

## 📊 Formato de Salida Excel

### Hoja "FACTURAS"
Todas las facturas procesadas con:
- Datos fiscales completos
- Desglose de IVA por tipo
- Retenciones
- Totales generales

### Hoja "PROVEEDORES"
Facturas agrupadas por NIF con:
- Color único por proveedor
- Desglose por tipo de IVA (solo si >1 tipo)
- Subtotales por proveedor
- Total general

## 🎨 Estructura del Proyecto

```
APP FACTURACION/
├── FICHEROS/
│   ├── app.py                    # Interfaz web Streamlit
│   ├── extractor.py              # Extracción con Gemini
│   ├── procesar_todas.py         # Script principal
│   ├── excel_writer.py           # Generación Excel
│   ├── finalizar_excel.py        # Totales y hoja PROVEEDORES
│   ├── cache_manager.py          # Sistema de caché
│   ├── image_processor.py        # Pre-procesamiento imágenes
│   ├── requirements.txt          # Dependencias Python
│   └── logo_muniz_nuno.png       # Logo corporativo
├── PROCESAR_FACTURAS.bat         # Launcher CLI
├── LANZAR_WEB.bat                # Launcher Web UI
└── .env                          # Configuración (no incluido)
```

## ⚙️ Configuración Avanzada

### Cambiar modelo de IA
Edita `FICHEROS/procesar_todas.py` o `FICHEROS/app.py`:
```python
model_name="gemini-3-pro-preview"  # Máxima precisión (actual)
# model_name="gemini-2.0-flash"    # Más rápido
```

### Ajustar workers paralelos
Edita `FICHEROS/procesar_todas.py`:
```python
max_workers=5  # Número de facturas procesadas simultáneamente
```

## 🛡️ Seguridad

- ⚠️ **NUNCA** subas tu archivo `.env` al repositorio
- ⚠️ La API Key es confidencial
- ✅ El `.gitignore` ya está configurado para proteger archivos sensibles

## 📝 Licencia

MIT License - Libre para uso personal y comercial

## 👨‍💼 Créditos

Desarrollado para **Muñiz & Nuño Asesores**

---

**¿Necesitas ayuda?** Abre un issue en GitHub
