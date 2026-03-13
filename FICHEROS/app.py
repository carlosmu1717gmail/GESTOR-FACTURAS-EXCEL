import streamlit as st
import pandas as pd
from pathlib import Path
import tempfile
import os
from datetime import datetime
from extractor import extract_invoice_data
from excel_writer import inicializar_excel, save_to_excel, finalizar_y_guardar_excel
from finalizar_excel import finalizar_excel
import base64

# Configuración de la página
st.set_page_config(
    page_title="AutoGestor Facturas - Muñiz & Nuño",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función para cargar logo como base64
def get_logo_base64():
    """Convierte el logo a base64 para incrustar en HTML. 
       Busca en varios directorios por si la ejecución varía entre Windows y la nube."""
    import os
    
    # Pruebas de posibles rutas donde esté la imagen
    posibles_rutas = [
        "logo_muniz_nuno.png", # Si lo levanta desde la raíz (Streamlit Cloud a veces)
        os.path.join(os.path.dirname(__file__), "logo_muniz_nuno.png"), # Si lo levanta desde FICHEROS/
        os.path.join(os.getcwd(), "FICHEROS", "logo_muniz_nuno.png") # Si el current working directory es la raíz
    ]
    
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            with open(ruta, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    
    # Si llega aquí, es que no encontró la imagen en ninguna ruta
    return None


# CSS personalizado
st.markdown("""
<style>
    .main-header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
    }
    .logo-header {
        max-height: 80px;
        width: auto;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f4e78;
        margin: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f4e78;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2d6ba8;
    }
    .sidebar-logo {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f4e78;
    }
    .sidebar-logo img {
        max-width: 180px;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session_state
if 'datos_facturas' not in st.session_state:
    st.session_state.datos_facturas = []
if 'procesamiento_completo' not in st.session_state:
    st.session_state.procesamiento_completo = False

# Header con logo
logo_b64 = get_logo_base64()
if logo_b64:
    st.markdown(f"""
    <div class="main-header-container">
        <img src="data:image/png;base64,{logo_b64}" class="logo-header" alt="Muñiz & Nuño Asesores">
        <div>
            <h1 class="main-header">AutoGestor Facturas</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="main-header">📄 AutoGestor Facturas</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-header">Extracción inteligente con Gemini 3 Pro AI · Interfaz Visual</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo en sidebar
    if logo_b64:
        st.markdown(f"""
        <div class="sidebar-logo">
            <img src="data:image/png;base64,{logo_b64}" alt="Muñiz & Nuño">
        </div>
        """, unsafe_allow_html=True)
    
    st.title("⚙️ Configuración")
    
    st.markdown("---")
    
    # NOTA: SIEMPRE gemini-3-pro-preview (el más avanzado)
    modelo_seleccionado = "gemini-3-pro-preview"
    st.info(f"🤖 Modelo: **{modelo_seleccionado}**\n\n(Gemini 3 Pro - Máxima precisión)")
    
    st.markdown("---")
    
    # Selector de tipo de factura
    tipo_factura_ui = st.radio(
        "Tipo de Facturas",
        ("RECIBIDAS (Gastos)", "EMITIDAS (Ventas)"),
        index=0,
        help="Selecciona si vas a procesar facturas de proveedores (Gastos) o a clientes (Ventas)"
    )
    
    # Mapeo a valor interno
    tipo_interno = "recibida" if "RECIBIDAS" in tipo_factura_ui else "emitida"
    
    st.markdown("---")
    
    st.markdown("### 📊 Estadísticas")
    if st.session_state.datos_facturas:
        st.metric("Facturas procesadas", len(st.session_state.datos_facturas))
        total_importe = sum([f.get('total_factura', 0) or 0 for f in st.session_state.datos_facturas])
        st.metric("Importe total", f"{total_importe:.2f} €")
    else:
        st.info("Sin facturas procesadas aún")
    
    st.markdown("---")
    
    if st.button("🗑️ Limpiar todo"):
        st.session_state.datos_facturas = []
        st.session_state.procesamiento_completo = False
        st.rerun()

# Tabs principales
tab1, tab2, tab3 = st.tabs(["📤 Subir Facturas", "✏️ Revisar Datos", "💾 Exportar Excel"])

with tab1:
    st.markdown("### 📁 Arrastra tus facturas aquí")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_files = st.file_uploader(
            "Sube archivos PDF, JPG o PNG",
            type=['pdf', 'jpg', 'jpeg', 'png'],
            accept_multiple_files=True,
            help="Puedes subir múltiples archivos a la vez"
        )
    
    with col2:
        st.markdown("#### 📋 Formatos")
        st.markdown("""
        - ✅ PDF
        - ✅ JPG/JPEG
        - ✅ PNG
        """)
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} archivo(s) cargado(s)")
        
        if st.button("🚀 Procesar Facturas", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            nuevas_facturas = []
            
            for i, uploaded_file in enumerate(uploaded_files):
                # Actualizar progreso
                progreso = (i + 1) / len(uploaded_files)
                progress_bar.progress(progreso)
                status_text.text(f"Procesando {uploaded_file.name}... ({i+1}/{len(uploaded_files)})")
                
                # Guardar archivo temporalmente
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                try:
                    # Extraer datos con Gemini 3 Pro Preview
                    data = extract_invoice_data(tmp_path, model_name=modelo_seleccionado, tipo_factura=tipo_interno)
                    data["file_name"] = uploaded_file.name
                    nuevas_facturas.append(data)
                    
                except Exception as e:
                    st.error(f"❌ Error procesando {uploaded_file.name}: {str(e)}")
                
                finally:
                    # Limpiar archivo temporal
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass
            
            # Añadir a session_state
            st.session_state.datos_facturas.extend(nuevas_facturas)
            st.session_state.procesamiento_completo = True
            
            progress_bar.progress(1.0)
            status_text.text("✅ ¡Procesamiento completado!")
            
            st.balloons()
            st.success(f"🎉 {len(nuevas_facturas)} facturas procesadas correctamente")

with tab2:
    st.markdown("### ✏️ Revisa los datos extraídos")
    
    if not st.session_state.datos_facturas:
        st.info("📭 No hay facturas procesadas. Ve a la pestaña 'Subir Facturas' para comenzar.")
    else:
        # Convertir a DataFrame
        df_data = []
        for factura in st.session_state.datos_facturas:
            df_data.append({
                "Archivo": factura.get("file_name", ""),
                "NIF": factura.get("contraparte_nif", ""),
                "Nombre": factura.get("contraparte_nombre", ""),
                "Fecha": factura.get("fecha_expedicion", ""),
                "Nº Factura": factura.get("numero_factura", ""),
                "Base": factura.get("base_imponible", 0),
                "IVA": factura.get("cuota_iva", 0),
                "Total": factura.get("total_factura", 0),
                "Confianza": f"{factura.get('confidence_score', 0):.0%}"
            })
        
        df = pd.DataFrame(df_data)
        
        st.dataframe(
            df,
            use_container_width=True,
            height=400
        )
        
        st.markdown("---")
        st.markdown("##### 🔍 Inspeccionar factura")
        
        seleccion = st.selectbox(
            "Selecciona una factura:",
            options=range(len(st.session_state.datos_facturas)),
            format_func=lambda x: st.session_state.datos_facturas[x].get("file_name", f"Factura {x+1}")
        )
        
        if seleccion is not None:
            factura_sel = st.session_state.datos_facturas[seleccion]
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**📝 Básicos**")
                st.text(f"Archivo: {factura_sel.get('file_name', 'N/A')}")
                st.text(f"Tipo: {factura_sel.get('doc_type', 'N/A')}")
                st.text(f"Fecha: {factura_sel.get('fecha_expedicion', 'N/A')}")
                st.text(f"Número: {factura_sel.get('numero_factura', 'N/A')}")
            
            with col2:
                st.markdown("**👤 Contraparte**")
                st.text(f"Nombre: {factura_sel.get('contraparte_nombre', 'N/A')}")
                st.text(f"NIF: {factura_sel.get('contraparte_nif', 'N/A')}")
            
            with col3:
                st.markdown("**💰 Importes**")
                
                # Proteger conversión a float para evitar TypeError con None o strings vacíos
                def safe_float(val):
                    try:
                        return float(val) if val is not None and val != "" else 0.0
                    except (ValueError, TypeError):
                        return 0.0

                base_imp = safe_float(factura_sel.get('base_imponible', 0))
                cuota_iva = safe_float(factura_sel.get('cuota_iva', 0))
                total_factura = safe_float(factura_sel.get('total_factura', 0))

                st.text(f"Base: {base_imp:.2f} €")
                st.text(f"IVA: {cuota_iva:.2f} €")
                st.text(f"Total: {total_factura:.2f} €")
            
            # Mostrar issues
            issues = factura_sel.get('issues', [])
            if issues:
                st.warning(f"⚠️ Avisos: {', '.join(issues) if isinstance(issues, list) else issues}")

with tab3:
    st.markdown("### 💾 Exportar a Excel")
    
    if not st.session_state.datos_facturas:
        st.info("📭 No hay facturas para exportar.")
    else:
        st.success(f"✅ {len(st.session_state.datos_facturas)} facturas listas")
        
        nombre_archivo = st.text_input(
            "Nombre del archivo",
            value=f"facturas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        )
        
        if st.button("📥 Generar Excel", type="primary"):
            with st.spinner("Generando Excel..."):
                try:
                    # Inicializar
                    inicializar_excel(nombre_archivo)
                    
                    # Guardar todas
                    for data in st.session_state.datos_facturas:
                        save_to_excel(data, nombre_archivo)
                    
                    # Finalizar
                    finalizar_y_guardar_excel(nombre_archivo)
                    finalizar_excel(nombre_archivo)
                    
                    st.success(f"✅ Excel generado: {nombre_archivo}")
                    
                    # Descarga
                    with open(nombre_archivo, "rb") as file:
                        st.download_button(
                            label="⬇️ Descargar Excel",
                            data=file,
                            file_name=nombre_archivo,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# Footer con branding
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <small>AutoGestor Facturas · Muñiz & Nuño Asesores · Gemini 3 Pro · v3.0</small>
    </div>
    """,
    unsafe_allow_html=True
)
