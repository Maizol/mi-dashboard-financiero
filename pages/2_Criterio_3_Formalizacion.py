import streamlit as st
import time
import pandas as pd
import altair as alt

# --- LIBRERÍAS EXTERNAS (LOTTIE, GRAPHVIZ) ELIMINADAS ---

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(layout="wide", page_title="Análisis de Formalización 'El Profe'")

# --- 2. ESTILOS CSS (Mejora Espectacular V8.0) ---
st.markdown("""
<style>
    /* Fondo Atractivo */
    [data-testid="stAppViewContainer"] > .main {
        background-color: #F0F4F8; /* Gris azulado profesional */
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Barra lateral (Se mantiene oscura) */
    [data-testid="stSidebar"] {
        background-color: #0A111F; 
        color: white;
        font-family: 'Segoe UI', sans-serif;
        border-right: 1px solid #E0E0E0;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: white; 
    }
    
    /* ESTILOS PARA ENLACES DE NAVEGACIÓN DE PÁGINAS */
    [data-testid="stSidebar"] a, [data-testid="stSidebar"] a:link, [data-testid="stSidebar"] a:visited {
        color: white !important;
        text-decoration: none;
    }
    [data-testid="stSidebar"] a:hover {
        color: #D6EAF8 !important;
        text-decoration: underline;
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: white !important;
    }
    /* Enlaces de navegación específicos */
    [data-testid="stSidebar"] ul li a {
        color: white !important;
    }
    [data-testid="stSidebar"] .stPageLink {
        color: white !important;
    }
    
    .sidebar-metric-container {
        background-color: #1a273b;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
    }
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: #FFFFFF;
    }

    /* Tarjetas y Sombras Mejoradas */
    [data-testid="stVerticalBlock"] [data-testid="stContainer"] {
        background-color: #FFFFFF; 
        border: 1px solid #E0E0E0; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.07); 
        border-radius: 12px; 
        padding: 25px; 
        margin-bottom: 20px; 
        height: 100%; 
    }
    
    /* Títulos */
    h1, h2, h3, h4 {
        color: #0A111F; 
        font-weight: 600;
    }

    /* Métrica Personalizada (Principal) */
    .main [data-testid="stMetricValue"] {
        font-size: 2.2rem;
        color: #D9534F;
        font-weight: 600;
    }
    .main [data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    
    /* Pestañas */
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem; 
        font-weight: 500;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    /* Clases de Riesgo */
    .risk-high { background-color: #F8D7DA; color: #721C24; padding: 12px; border-radius: 8px; font-weight: bold; border: 1px solid #F5C6CB;}
    
    .highlight { 
        color: #0A111F; 
        font-weight: 600; 
        background-color: #D6EAF8; 
        padding: 2px 5px;
        border-radius: 4px;
    }
    
    /* Separador Notable */
    .fancy-divider {
        width: 100%;
        border-top: 3px solid #0A111F;
        border-radius: 3px;
        margin-top: 20px;
        margin-bottom: 20px;
        opacity: 0.7;
    }
    
    /* Pie de página */
    .footer {
        font-size: 0.8em;
        color: #6c757d;
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL (Sidebar) ---
st.sidebar.title("TA4 - Gestión Financiera")
st.sidebar.divider()
st.sidebar.header("Criterio 3: Formalización")
st.sidebar.markdown("Análisis de la situación legal y tributaria de la MYPE.")

with st.sidebar.container():
    st.markdown("<div class='sidebar-metric-container'>", unsafe_allow_html=True)
    st.subheader("Diagnóstico Actual")
    st.metric(
        label="Forma Legal",
        value="Persona Natural",
        delta="Riesgo Patrimonial Alto",
        delta_color="inverse"
    )
    st.metric(
        label="Régimen Tributario",
        value="NRUS (Supuesto)",
        delta="Límite de Crecimiento",
        delta_color="normal"
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.divider()
st.sidebar.info(
    "Este análisis identifica las barreras para la formalización (Criterio 3) y propone soluciones directas (Criterio 4)."
)

# --- Inicializar el "Session State" para navegación ---
if 'c3_view' not in st.session_state:
    st.session_state.c3_view = 'main' # 'main', 'barrera1', 'barrera2', 'barrera3'

# --- Funciones para las vistas detalladas ---
def show_barrera1_detail():
    if st.button("⬅️ Retroceder al Diagnóstico"):
        st.session_state.c3_view = 'main'
        st.rerun()
    
    st.header("🧱 Barrera 1: Análisis de Costos y Burocracia")
    st.markdown("El dueño percibe que 'crear una empresa' es un proceso largo, complejo y caro (notarios, abogados, SUNARP), viéndolo como un gasto y no una inversión.")
    st.info("**Solución Directa:** Esta barrera se supera con la **Propuesta 2: Usar 'Tu Empresa'**, que anula casi todos los costos y la burocracia.", icon="🎁")
    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    
    st.subheader("Percepción vs. Realidad")
    st.markdown("""
    * **Percepción:** "Me costará miles de soles y tomará semanas."
    * **Realidad (usando P.2):** Con el programa "Tu Empresa", el costo de constitución es casi **cero** y puede hacerse en **24-72 horas**.
    * **El Verdadero Costo:** El único costo real e ineludible es el *Capital Social* (que puede ser en bienes, ej. una hidrolavadora) y el costo del contador (P.3).
    """)

    st.markdown("---") 
    
    st.subheader("Gráfico: Costo Percibido vs. Costo Real")
    
    chart_data = pd.DataFrame({
        "Tipo de Costo": ["Costo Percibido", "Costo Real (con 'Tu Empresa')"],
        "Monto (S/)": [2000, 150],
        "Color": ["#D9534F", "#5CB85C"] 
    })
    
    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X('Tipo de Costo', sort=None),
        y=alt.Y('Monto (S/)'),
        color=alt.Color('Tipo de Costo', 
                        scale=alt.Scale(domain=chart_data["Tipo de Costo"].tolist(), 
                                        range=chart_data["Color"].tolist()),
                        legend=None),
        tooltip=['Tipo de Costo', 'Monto (S/)']
    ).properties(
        title="Comparativa de Costos de Formalización"
    )
    st.altair_chart(chart, use_container_width=True)
    st.caption("Costo real estimado incluye tasas registrales mínimas (con 'Tu Empresa').")

def show_barrera2_detail():
    if st.button("⬅️ Retroceder al Diagnóstico"):
        st.session_state.c3_view = 'main'
        st.rerun()
        
    st.header("📊 Barrera 2: Análisis de Complejidad Tributaria")
    st.markdown("Miedo a dejar el NRUS. Los regímenes más avanzados (RMT, General) exigen registros contables y la contratación de un contador, visto como un costo fijo inasumible.")
    st.info("**Solución Directa:** Esta barrera se supera con la **Propuesta 3: Migrar al Régimen MYPE (RMT)**, que ofrece beneficios fiscales y contabilidad simple.", icon="📈")
    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    
    st.subheader("Comparativa de Regímenes: NRUS vs. RMT (Propuesta)")
    col1, col2 = st.columns(2)
    with col1:
        st.error("Régimen Actual (NRUS)")
        st.markdown("""
        * **Contabilidad:** Ninguna.
        * **Impuesto:** Cuota fija (S/ 20 o S/ 50).
        * **Comprobantes:** Solo Boletas.
        * **Límite:** S/ 8,000 / mes.
        * **Mercado:** Solo B2C (Consumidor final).
        """)
    with col2:
        st.success("Régimen Propuesto (RMT)")
        st.markdown("""
        * **Contabilidad:** 3 Registros Simples (Compras, Ventas, Diario Simpl.).
        * **Impuesto:** 10% sobre la ganancia neta.
        * **Comprobantes:** ¡Facturas y Boletas!
        * **Límite:** S/ 1,700 UIT (Millones).
        * **Mercado:** B2C y B2B (¡Empresas!).
        """)
    st.markdown("**Conclusión:** La 'complejidad' del RMT es mínima y es el precio de entrada para acceder al mercado corporativo, que es mucho más rentable.")

def render_fallback_diagram():
    # Diagrama de texto 100% seguro
    col1, col2 = st.columns(2)
    with col1:
        st.error("Escenario como Persona Natural (Riesgo Alto)")
        st.markdown("""
        **[ Dueño ]** ↔️ **[ Negocio ]**
        
        *Patrimonio Personal (Casa, Auto)* vulnerable a...
        
        *Deudas del Negocio (Préstamos, Demandas)*
        
        **No existe separación legal.**
        """)
    with col2:
        st.success("Escenario como E.I.R.L. (Riesgo Controlado)")
        st.markdown("""
        **[ Dueño ]** ➡️ **[ 🛡️ E.I.R.L. 🛡️ ]** ↔️ **[ Negocio ]**
        
        *Patrimonio Personal (Casa, Auto)* **PROTEGIDO**
        
        *Deudas del Negocio (Préstamos, Demandas)*
        
        **El "muro" (🛡️) es la Responsabilidad Limitada.**
        """)

def show_barrera3_detail():
    if st.button("⬅️ Retroceder al Diagnóstico"):
        st.session_state.c3_view = 'main'
        st.rerun()
        
    st.header("💡 Barrera 3: Análisis del Desconocimiento de Beneficios")
    st.markdown("El dueño no ve el valor de la formalización. Desconoce el beneficio clave: **Responsabilidad Limitada**, que protege su patrimonio personal (casa, auto) de las deudas del negocio.")
    st.info("**Solución Directa:** Esta barrera se supera con la **Propuesta 1: Crear una E.I.R.L.**, que implementa este escudo de protección.", icon="🚀")
    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    st.subheader("Diagrama: El Escudo Patrimonial")
    st.markdown("La formalización (E.I.R.L.) crea un 'muro' legal (responsabilidad limitada) entre el dueño y el negocio.")
    
    # --- PLAN B: Renderizado de respaldo ---
    render_fallback_diagram()

# --- 4. CUERPO PRINCIPAL DEL INFORME ---
with st.spinner('Cargando Análisis Legal y Tributario...'):
    time.sleep(1) 

st.title("⚖️ Criterio 3 y 4: Análisis de Formalización")

tab_diag, tab_prop = st.tabs([
    " Diagnóstico (Criterio 3) ", 
    " Propuestas (Criterio 4) "
])

with tab_diag:
    if st.session_state.c3_view == 'main':
        st.header("Sumario Ejecutivo: Diagnóstico")
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Forma Legal Actual", value="Persona Natural", delta="Riesgo: Ilimitado", delta_color="inverse")
            with col2:
                st.metric(label="Riesgo Patrimonial", value="ALTO", delta="Bienes personales expuestos", delta_color="inverse")
            with col3:
                st.metric(label="Límite de Mercado", value="Solo B2C (Boletas)", delta="Excluido de Clientes Empresa", delta_color="normal")
                
        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
        st.header("Diagnóstico Legal, Tributario y Barreras")

        with st.container(border=True):
            st.markdown("Análisis de la estructura actual de 'Carwash El Profe' y sus implicancias.")
            tab1, tab2 = st.tabs(["🏦 Análisis Legal (Forma Societaria)", "🧾 Análisis Tributario (Régimen)"])
            with tab1:
                st.subheader("Forma Legal Actual: Persona Natural con Negocio (PNcN)")
                st.error("**Diagnóstico:** La MYPE opera como Persona Natural con Negocio. Esto significa que **el dueño y el negocio son la misma entidad legal**.", icon="🚨")
                st.markdown("#### El Riesgo Principal: Responsabilidad Ilimitada")
                st.markdown("El dueño asume todas las deudas del negocio con su **patrimonio personal** (casa, auto, ahorros). No existe separación legal.")
            with tab2:
                st.subheader("Régimen Tributario Supuesto: Nuevo Régimen Único Simplificado (NRUS)")
                st.warning("**Diagnóstico Supuesto:** Es probable que opere en el NRUS (o en informalidad total).", icon="⚠️")
                st.markdown("#### Las Limitaciones del NRUS")
                st.markdown("Impone un **límite de S/ 8,000/mes** y **prohíbe emitir Facturas**, condenando al negocio al mercado B2C (consumidor final) y excluyéndolo de clientes corporativos.")

        st.subheader("Identificación de 3 Barreras Clave (Haz clic para analizar)")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                # --- ANIMACIÓN ELIMINADA, EMOJI AÑADIDO ---
                st.subheader("🧱 Barrera 1: Costos")
                st.markdown("Percepción de que formalizarse es un proceso largo, complejo y caro (notarios, abogados, SUNARP).")
                if st.button("Analizar Barrera de Costos ➡️", key="btn_b1", use_container_width=True, type="primary"):
                    st.session_state.c3_view = 'barrera1'
                    st.rerun()
        with col2:
            with st.container(border=True):
                # --- ANIMACIÓN ELIMINADA, EMOJI AÑADIDO ---
                st.subheader("📊 Barrera 2: Complejidad")
                st.markdown("Miedo a dejar el NRUS y tener que contratar un contador, visto como un costo fijo inasumible.")
                if st.button("Analizar Barrera de Complejidad ➡️", key="btn_b2", use_container_width=True, type="primary"):
                    st.session_state.c3_view = 'barrera2'
                    st.rerun()
        with col3:
            with st.container(border=True):
                # --- ANIMACIÓN ELIMINADA, EMOJI AÑADIDO ---
                st.subheader("💡 Barrera 3: Desconocimiento")
                st.markdown("No ve el valor de la formalización. Desconoce el beneficio clave: **Responsabilidad Limitada**.")
                if st.button("Analizar Barrera de Desconocimiento ➡️", key="btn_b3", use_container_width=True, type="primary"):
                    st.session_state.c3_view = 'barrera3'
                    st.rerun()

    elif st.session_state.c3_view == 'barrera1':
        show_barrera1_detail()
    elif st.session_state.c3_view == 'barrera2':
        show_barrera2_detail()
    elif st.session_state.c3_view == 'barrera3':
        show_barrera3_detail()

with tab_prop:
    st.header("Propuestas de Mejora para la Formalización")
    st.success("✅ **Plan de Acción:** Para superar las 3 barreras, se definen las siguientes 4 propuestas estratégicas.", icon="🎯")
    
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        with st.container(border=True):
            st.subheader("🚀 Propuesta 1: Crear una E.I.R.L.")
            st.markdown("**Objetivo:** Atacar la Barrera 3 (Desconocimiento) y el riesgo de Responsabilidad Ilimitada.")
            st.markdown("Es la solución directa al riesgo más grave. Una **E.I.R.L. (Empresa Individual de Responsabilidad Limitada)** crea una Persona Jurídica separada, con un único dueño.")
            st.markdown("---")
            st.error("**Actual (PNcN):** Responsabilidad Ilimitada (Patrimonio personal en riesgo).")
            st.success("**Propuesta (E.I.R.L.):** Responsabilidad Limitada (Patrimonio personal protegido).")
    with row1_col2:
        with st.container(border=True):
            st.subheader("🎁 Propuesta 2: Usar 'Tu Empresa'")
            st.markdown("**Objetivo:** Atacar la Barrera 1 (Costos y Burocracia).")
            st.markdown("Usar el programa **'Tu Empresa'** del Ministerio de la Producción (PRODUCE) para una formalización casi gratuita.")
            st.markdown("---")
            st.markdown("""
            * ✅ **Asesoría Gratuita:** Guían en todo el proceso.
            * ✅ **Constitución en 24h (SACS):** Permite constitución digital rápida.
            * ✅ **Ahorro en Notaría y Registros:** El programa subsidia o elimina la mayoría de costos.
            """)
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        with st.container(border=True):
            st.subheader("📈 Propuesta 3: Migrar al Régimen MYPE (RMT)")
            st.markdown("**Objetivo:** Atacar la Barrera 2 (Complejidad) y abrir nuevos mercados.")
            st.markdown("Al crear la E.I.R.L., acogerla al **Régimen MYPE Tributario (RMT)**, que es ideal para MYPEs.")
            st.markdown("---")
            st.markdown("""
            * ✅ **Emite Facturas:** ¡Permite vender a empresas (B2B)!
            * ✅ **Impuesto Bajo:** Tasa de solo 10% sobre la ganancia neta (hasta 15 UIT).
            * ✅ **Contabilidad Simple:** Requiere registros básicos (Compras, Ventas).
            """)
    with row2_col2:
        with st.container(border=True):
            st.subheader("🗺️ Propuesta 4: Hoja de Ruta de Licencias")
            st.markdown("**Objetivo:** Diferenciar la formalización legal de la operativa.")
            st.markdown("Una hoja de ruta clara para obtener la Licencia de Funcionamiento Municipal (ej. en Municipalidad de Surquillo).")
            st.markdown("---")
            st.markdown("""
            1. **Constitución (SUNARP):** Crear la E.I.R.L. (Propuesta 1+2).
            2. **Inscripción RUC (SUNAT):** Activar RUC y acogerse al RMT (Propuesta 3).
            3. **Licencia Municipal:**
                * Solicitar "Compatibilidad de Uso".
                * Pasar Inspección "ITSE" (Riesgo Bajo/Medio).
            """)

# --- Pie de Página (Fuera de las pestañas) ---
st.markdown("""
<div class="footer">
    <p>Proyecto TA4 - Gestión Financiera de MYPEs | Carwash 'El Profe'</p>
    <p>&copy; 2025 Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)