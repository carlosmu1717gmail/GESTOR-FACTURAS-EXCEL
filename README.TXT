===================================================
   GUIA DE INSTALACION - GESTOR DE FACTURAS IA
===================================================

Este paquete contiene un sistema inteligente para extraer datos de facturas
utilizando la IA de Google Gemini.

Sigue estos pasos en orden para ponerlo en marcha en tu ordenador:

PASO 1: REQUISITOS PREVIOS
--------------------------
1. Debes tener instalado Python (version 3.10 o superior).
2. Si no lo tienes, descargalo aqui: https://www.python.org/downloads/
3. IMPORTANTE: Durante la instalacion de Python, marca la casilla 
   "Add Python to PATH".

PASO 2: INSTALACION AUTOMATICA
------------------------------
1. Descomprime este archivo en una carpeta de tu ordenador.
2. Haz doble clic en el archivo: INSTALAR.bat
3. Espera a que termine. Este script instalara las librerias necesarias
   y preparara la carpeta "C:\FACTURAS" donde se guardaran los resultados.

PASO 3: CONFIGURACION DE LA IA (API KEY)
----------------------------------------
La aplicacion necesita una "llave" para hablar con la IA de Google.
1. Consigue tu API Key gratuita en: https://ai.google.dev
2. Busca en esta carpeta el archivo llamado ".env" y abrelo con el Bloc de notas.
3. Veras una linea que dice: GEMINI_API_KEY=tu_llave_aqui
4. Sustituye "tu_llave_aqui" por la clave que has copiado de Google.
5. Guarda el archivo y cierralo.

PASO 4: ¡A FUNCIONAR!
---------------------
Tienes varias formas de usar la aplicacion:

- INTERFAZ WEB (Recomendado): Ejecuta "LANZAR_WEB.bat". 
  Se abrira tu navegador en una direccion tipo http://localhost:5000 
  donde podras subir facturas y ver los resultados.

- MODO RAPIDO (Consola): Ejecuta "PROCESAR_FACTURAS.bat".

LISTO PARA USAR
---------------
Cualquier duda, consulta la documentacion detallada en la carpeta FICHEROS.
===================================================
