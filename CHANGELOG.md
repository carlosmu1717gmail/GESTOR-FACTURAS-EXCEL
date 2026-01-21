# 📋 Historial de Cambios

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [1.0.0] - 2026-01-21

### ✨ Añadido
- Sistema de extracción automática con Google Gemini 3 Pro
- Interfaz web con Streamlit para arrastrar y soltar facturas
- Modo línea de comandos para procesamiento batch
- Sistema de caché inteligente para evitar reprocesar facturas
- Pre-procesamiento automático de imágenes (contraste y nitidez)
- Exportación a Excel con dos hojas:
  - **FACTURAS**: Todas las facturas procesadas
  - **PROVEEDORES**: Agrupadas por NIF con desglose de IVA
- Soporte multi-IVA (facturas con varios tipos de IVA)
- Detección automática de duplicados
- Scripts de instalación automática (`INSTALAR.bat`)
- Script de actualización desde GitHub (`ACTUALIZAR.bat`)
- Modo interfaz web con acceso remoto (`LANZAR_WEB_REMOTO.bat`)
- Documentación completa:
  - `README.md` - Guía completa
  - `QUICKSTART.md` - Instalación rápida
  - `DESCARGA.md` - Descarga sin Git
  - `CHANGELOG.md` - Historial de versiones

### 🎨 Mejorado
- Formato Excel con:
  - Colores diferenciados por proveedor
  - Desglose detallado de IVA por tipo
  - Totales automáticos
  - Estilos profesionales

### 🔒 Seguridad
- Archivo `.env.example` como plantilla
- `.gitignore` configurado para proteger datos sensibles
- API Keys nunca se suben al repositorio

---

## 🔮 Próximas Características

### En Desarrollo
- [ ] Soporte para más formatos de factura
- [ ] Exportación a otros formatos (CSV, JSON)
- [ ] Base de datos SQLite para historial
- [ ] Dashboard de estadísticas
- [ ] Soporte multi-idioma

### Considerando
- [ ] OCR mejorado con Tesseract
- [ ] Integración con sistemas contables
- [ ] API REST para integraciones
- [ ] Aplicación de escritorio con GUI nativa

---

## 📝 Notas de Versión

### Compatibilidad
- **Python**: 3.9+
- **Sistema Operativo**: Windows 10/11
- **API**: Google Gemini 3 Pro Preview

### Dependencias Principales
- `google-generativeai` - IA de Google
- `streamlit` - Interfaz web
- `openpyxl` - Generación Excel
- `Pillow` - Procesamiento de imágenes
- `pydantic` - Validación de datos
