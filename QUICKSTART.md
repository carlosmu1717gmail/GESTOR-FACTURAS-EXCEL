# 🚀 Guía Rápida de Instalación

## ⚡ Instalación en 3 Pasos

### 📋 Requisitos Previos
- **Windows** 10/11
- **Python 3.9+** ([Descargar aquí](https://www.python.org/downloads/))
  - ⚠️ Durante la instalación marca: **"Add Python to PATH"**

---

### 🔧 Paso 1: Descargar la Aplicación

#### Opción A: Con Git (Recomendado)
```bash
git clone https://github.com/carlosmu1717gmail/ANTIGRAVITY-GESTOR-FACTURAS.git
cd ANTIGRAVITY-GESTOR-FACTURAS
```

#### Opción B: Descarga Manual
1. Ve a: `https://github.com/carlosmu1717gmail/ANTIGRAVITY-GESTOR-FACTURAS`
2. Clic en **Code** → **Download ZIP**
3. Descomprime el archivo en una carpeta
4. Abre la carpeta descomprimida

---

### ⚙️ Paso 2: Ejecutar Instalación Automática

Haz doble clic en:
```
INSTALAR.bat
```

Este script:
- ✅ Verifica que Python esté instalado
- ✅ Instala todas las dependencias necesarias
- ✅ Crea el archivo de configuración `.env`
- ✅ Prepara la carpeta de facturas

---

### 🔑 Paso 3: Configurar API Key de Gemini

1. **Obtén tu API Key gratuita:**
   - Ve a: [https://ai.google.dev](https://ai.google.dev)
   - Inicia sesión con tu cuenta Google
   - Clic en **Get API Key** → **Create API Key**
   - Copia la clave generada

2. **Configura la aplicación:**
   - Abre el archivo `.env` con Notepad
   - Reemplaza `tu_clave_api_aqui` con tu API Key real:
   ```env
   GEMINI_API_KEY=AIzaSyC1234567890abcdefghijklmnopqrstuvw
   ```
   - Guarda y cierra el archivo

---

## 🎉 ¡Listo! Ahora Puedes Usar la Aplicación

### 💻 Modo Línea de Comandos
```bash
PROCESAR_FACTURAS.bat
```
Coloca tus PDFs en `C:\FACTURAS` y ejecuta el script.

### 🌐 Modo Interfaz Web (Solo en este PC)
```bash
LANZAR_WEB.bat
```
Se abrirá en `http://localhost:8501`

### 🌍 Modo Interfaz Web (Acceso desde otros PCs en la red)
```bash
LANZAR_WEB_REMOTO.bat
```
Otros ordenadores podrán acceder usando tu IP local.

---

## ❓ Problemas Comunes

### "Python no está instalado"
- Descarga Python desde: https://www.python.org/downloads/
- **MUY IMPORTANTE:** Marca la casilla "Add Python to PATH"

### "Error al instalar dependencias"
- Ejecuta manualmente:
```bash
python -m pip install --upgrade pip
python -m pip install -r FICHEROS\requirements.txt
```

### "API Key inválida"
- Verifica que copiaste la clave completa sin espacios
- Asegúrate de haber guardado el archivo `.env`
- La clave debe empezar con `AIza`

---

## 📞 Soporte

¿Problemas? Abre un **issue** en GitHub con:
- Sistema operativo y versión
- Versión de Python (`python --version`)
- Mensaje de error completo
