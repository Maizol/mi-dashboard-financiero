import streamlit as st
import time
import pandas as pd
import altair as alt

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(layout="wide", page_title="Propuestas de Crecimiento 'El Profe'")

# --- 2. ESTILOS CSS (Con Mejoras de Pulido) ---
st.markdown("""
<style>
    /* Fondo Atractivo */
    [data-testid="stAppViewContainer"] > .main {
        background-color: #F0F4F8; /* Gris azulado profesional */
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Barra lateral */
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
        /* MEJORA 1: Transición para el hover */
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    
    /* MEJORA 1: Efecto Hover */
    [data-testid="stVerticalBlock"] [data-testid="stContainer"]:hover {
        transform: scale(1.02); /* Escala la tarjeta */
        box-shadow: 0 12px 24px rgba(0,0,0,0.12); /* Sombra más pronunciada */
    }
    
    /* Títulos */
    h1, h2, h3, h4 {
        color: #0A111F; 
        font-weight: 600;
    }

    /* Pestañas */
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem; 
        font-weight: 500;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    /* Métricas principales (KPIs) */
    .main [data-testid="stMetricValue"] {
        font-size: 2.5rem; /* Tamaño ajustado para KPIs */
        color: #0068C9; /* Azul corporativo */
        font-weight: 600;
    }
    .main [data-testid="stMetricDelta"] {
        font-size: 1rem;
        color: #28A745; /* Verde para deltas positivos */
    }
    
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
    
    /* MEJORA 5: Pie de Página Pulido */
    .footer {
        font-size: 0.75em; /* Más pequeño */
        color: #6c757d;
        text-align: center;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
        opacity: 0.8; /* Más sutil */
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL (Sidebar) ---
st.sidebar.title("TA4 - Gestión Financiera")
st.sidebar.divider()
# MEJORA 3: Pulido de Título de Sidebar
st.sidebar.header("🎯 Criterio 5: Crecimiento")
st.sidebar.markdown("Planteamiento de 4 propuestas de mejora con TICs.")

with st.sidebar.container():
    st.markdown("<div class='sidebar-metric-container'>", unsafe_allow_html=True)
    st.subheader("Enfoque de Propuestas")
    st.markdown("""
    <small>
    Propuestas estratégicas de crecimiento para el sector carwash, centradas en la incorporación de TICs para escalar el negocio.
    </small>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.divider()
st.sidebar.info(
    "Estas propuestas transforman a 'El Profe' de un negocio de supervivencia a una empresa con potencial de crecimiento y escalabilidad."
)

# --- Inicializar el "Session State" para navegación ---
if 'c5_view' not in st.session_state:
    st.session_state.c5_view = 'main' # 'main', 'prop1', 'prop2', 'prop3', 'prop4'

# --- Funciones para las vistas detalladas (PULIDAS) ---
def show_prop1_detail():
    with st.container():
        if st.button("⬅️ Retroceder a Propuestas"):
            st.session_state.c5_view = 'main'
            st.rerun()
        
        st.header("🚀 Propuesta 1: Sistema de Gestión de Clientes (CRM)")
        st.info("**TICs a Incorporar:** Software CRM (Cloud) para organizar base de datos, registrar visitas, preferencias y frecuencia de consumo.")
        
        st.subheader("Indicadores Clave de Crecimiento (KPIs)")
        kpi1, kpi2 = st.columns(2)
        kpi1.metric(label="Aumento Proyectado en Tasa de Retención", value="+25%")
        kpi2.metric(label="Reducción de 'No Presentación' (No-Shows)", value="-30%")
        
        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
        
        st.subheader("Beneficios Clave para el Crecimiento")
        st.markdown("""
        * **Campañas Personalizadas:** Permite crear promociones de fidelización (descuentos por 5ta visita, regalos de cumpleaños).
        * **Visión de Negocio:** El dashboard permite ver métricas en tiempo real como Ingresos Totales, Clientes Registrados y Alertas de Stock.
        * **Eficiencia Operativa:** Centraliza la información del cliente, mejorando la velocidad y calidad de la atención.
        """)
        
        st.subheader("Prototipo del Dashboard de Gestión")
        try:
            st.image("crm_dashboard.png",
                     caption="Prototipo del CRM 'El Profe' para uso interno",
                     use_container_width=True)
        except FileNotFoundError:
            st.warning("No se encontró la imagen 'crm_dashboard.png'. Asegúrate de guardarla en la misma carpeta que el script.")

def show_prop2_detail():
    with st.container():
        if st.button("⬅️ Retroceder a Propuestas"):
            st.session_state.c5_view = 'main'
            st.rerun()
            
        st.header("🔁 Propuesta 2: Modelo de Suscripción (Club del Profe)")
        st.info("**TICs a Incorporar:** Pasarela de Pagos Recurrentes (ej. Stripe, Culqi), Módulo de Cuentas de Usuario (Login) en la web.")

        st.subheader("Indicadores Clave de Crecimiento (KPIs)")
        kpi1, kpi2 = st.columns(2)
        kpi1.metric(label="Ingreso Mensual Recurrente (MRR) Proyectado", value="S/ 6,000")
        kpi2.metric(label="Aumento de Frecuencia de Visita", value="+70%")

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        st.subheader("Beneficios Clave para el Crecimiento")
        st.markdown("""
        * **Flujo de Caja Predecible:** Asegura ingresos recurrentes mensuales (MRR), crucial para la sostenibilidad financiera.
        * **Aumento de Fidelización:** Un cliente suscrito no se va a la competencia. Estabiliza el flujo de caja y aumenta el *valor de vida del cliente (LTV)*.
        * **Planes Escalables:** Se ofrecen múltiples niveles (Bronce, Plata, Oro) para capturar diferentes tipos de clientes.
        """)
        
        st.subheader("Proyección de Ingresos por Suscripción (6 Meses)")
        mrr_data = {
            'Mes': ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4', 'Mes 5', 'Mes 6'],
            'Ingreso (S/)': [1500, 2500, 3800, 4800, 5500, 6000] 
        }
        df_mrr = pd.DataFrame(mrr_data)
        mrr_chart = alt.Chart(df_mrr).mark_area(
            line={'color':'#0068C9'},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='white', offset=0),
                       alt.GradientStop(color='#0068C9', offset=1)],
                x1=1, x2=1, y1=1, y2=0
            ),
            opacity=0.7 # MEJORA 4: Pulido de Gráfico
        ).encode(
            x=alt.X('Mes', sort=None),
            y=alt.Y('Ingreso (S/)'),
            tooltip=['Mes', 'Ingreso (S/)']
        ).properties(
            title="Crecimiento Proyectado del MRR"
        ).interactive()
        st.altair_chart(mrr_chart, use_container_width=True)

        st.subheader("Prototipo de Planes de Membresía")
        try:
            st.image("web_membresias.png",
                     caption="Prototipo de la sección de Membresías",
                     use_container_width=True)
        except FileNotFoundError:
            st.warning("No se encontró la imagen 'web_membresias.png'. Asegúrate de guardarla en la misma carpeta que el script.")

def show_prop3_detail():
    with st.container():
        if st.button("⬅️ Retroceder a Propuestas"):
            st.session_state.c5_view = 'main'
            st.rerun()
            
        st.header("🎯 Propuesta 3: E-commerce y Marketing Digital Local")
        st.info("**TICs a Incorporar:** Página Web Transaccional (Reservas/Pagos), Google My Business (Maps), SEM (Google/Facebook Ads).")

        st.subheader("Indicadores Clave de Crecimiento (KPIs)")
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Objetivo de Captación (6 Semanas)", value="200 Clientes")
        kpi2.metric(label="Retorno de Inversión (ROI) Proyectado", value="3:1")
        kpi3.metric(label="Alcance Geográfico", value="3km (Hiper-local)")

        st.markdown("<div class'fancy-divider'></div>", unsafe_allow_html=True)
        
        st.subheader("Beneficios Clave para el Crecimiento")
        st.markdown("""
        * **Reducción de Tiempos de Espera:** Un sistema de reservas online mejora drásticamente la experiencia del cliente.
        * **Optimización de la Operación:** Permite agendar más clientes por día de forma ordenada.
        * **Captación Activa de Clientes:** La publicidad pagada en Google Maps y redes sociales permite captar clientes en Surquillo y distritos cercanos.
        """)

        st.subheader("Prototipo de la Plataforma E-commerce")
        try:
            st.image("web_home.png",
                     caption="Prototipo de la página web con botones de reserva",
                     use_container_width=True)
        except FileNotFoundError:
            st.warning("No se encontró la imagen 'web_home.png'. Asegúrate de guardarla en la misma carpeta que el script.")

def show_prop4_detail():
    with st.container():
        if st.button("⬅️ Retroceder a Propuestas"):
            st.session_state.c5_view = 'main'
            st.rerun()
            
        st.header("💧 Propuesta 4: Servicios Eco-Premium y Delivery")
        st.info("**TICs a Incorporar:** Sistema de reciclaje de agua (IoT/Sensores), App de logística (para servicio a domicilio), TICs de Detailing (Grafeno).")

        st.subheader("Indicadores Clave de Crecimiento (KPIs)")
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Reducción Proyectada de Costo de Agua", value="-60%")
        kpi2.metric(label="Margen en Servicios Premium", value="+40%")
        kpi3.metric(label="Nuevos Mercados", value="B2B / Flotas")

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        st.subheader("Beneficios Clave para el Crecimiento")
        st.markdown("""
        * **Diferenciación de Mercado:** Lanzar un "Lavado Eco-Profe" con productos biodegradables y sistemas de reciclaje de agua.
        * **Atracción de Nuevos Segmentos:** Se atrae a clientes con conciencia ambiental y a clientes premium (detailing con grafeno).
        * **Ampliación del Mercado (B2B y Delivery):** Ofrecer servicio a domicilio y convenios con flotas (taxis, Uber) amplía el mercado más allá del local físico.
        """)
        
        st.subheader("Prototipo de Servicios Premium")
        try:
            st.image("web_servicios.png",
                     caption="Prototipo de la sección de Servicios Premium",
                     use_container_width=True)
        except FileNotFoundError:
            st.warning("No se encontró la imagen 'web_servicios.png'. Asegúrate de guardarla en la misma carpeta que el script.")

def render_main_page():
    """Dibuja solo la página principal (la cuadrícula de propuestas)."""
    with st.container():
        st.header("4 Propuestas de Mejora (Haz clic para analizar)")
        st.markdown("Las siguientes propuestas estratégicas están diseñadas para el crecimiento de 'El Profe', incorporando TICs.")
        
        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            with st.container(border=True):
                st.subheader("🚀 Propuesta 1: CRM (TIC)")
                st.markdown("Implementar un sistema de gestión de clientes (CRM) para organizar la base de datos, registrar visitas y fidelizar.")
                # MEJORA 2: Tooltip añadido
                if st.button("Analizar Propuesta CRM ➡️", key="btn_p1", use_container_width=True, type="primary", 
                             help="Haz clic para ver el análisis detallado de la Propuesta 1: CRM"):
                    st.session_state.c5_view = 'prop1'
                    st.rerun()
        with row1_col2:
            with st.container(border=True):
                st.subheader("🔁 Propuesta 2: Suscripciones (TIC)")
                st.markdown("Crear un 'Club del Profe' con pagos mensuales recurrentes para asegurar un flujo de caja predecible y lealtad.")
                # MEJORA 2: Tooltip añadido
                if st.button("Analizar Modelo de Suscripción ➡️", key="btn_p2", use_container_width=True, type="primary",
                             help="Haz clic para ver el análisis detallado de la Propuesta 2: Suscripciones"):
                    st.session_state.c5_view = 'prop2'
                    st.rerun()

        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            with st.container(border=True):
                st.subheader("🎯 Propuesta 3: E-commerce y Marketing (TIC)")
                st.markdown("Desarrollar una web con reservas/pagos online y usar Google/Facebook Ads para captar clientes en Surquillo.")
                # MEJORA 2: Tooltip añadido
                if st.button("Analizar E-commerce y Marketing ➡️", key="btn_p3", use_container_width=True, type="primary",
                             help="Haz clic para ver el análisis detallado de la Propuesta 3: E-commerce"):
                    st.session_state.c5_view = 'prop3'
                    st.rerun()
    with row2_col2:
        with st.container(border=True):
            st.subheader("💧 Propuesta 4: Servicios Eco-Premium")
            st.markdown("Incorporar servicios de 'Lavado Eco-Profe' (con TICs de reciclaje) y 'Detailing Pro' para diferenciar y captar clientes B2B.")
            # MEJORA 2: Tooltip añadido
            if st.button("Analizar Servicios Eco-Premium ➡️", key="btn_p4", use_container_width=True, type="primary",
                             help="Haz clic para ver el análisis detallado de la Propuesta 4: Servicios Eco-Premium"):
                st.session_state.c5_view = 'prop4'
                st.rerun()

# --- 4. CUERPO PRINCIPAL DEL INFORME ---
with st.spinner('Cargando Propuestas de Crecimiento...'):
    time.sleep(1) 

# MEJORA 3: Pulido de Título Principal
st.title("🚀 Criterio 5: Plan de Crecimiento y TICs")

# --- ENRUTADOR DE VISTAS (Router) ---
if st.session_state.c5_view == 'main':
    render_main_page()
elif st.session_state.c5_view == 'prop1':
    show_prop1_detail()
elif st.session_state.c5_view == 'prop2':
    show_prop2_detail()
elif st.session_state.c5_view == 'prop3':
    show_prop3_detail()
elif st.session_state.c5_view == 'prop4':
    show_prop4_detail()


# --- Pie de Página (Fuera de las pestañas) ---
st.markdown("""
<div class="footer">
    <p>Proyecto TA4 - Gestión Financiera de MYPEs | Carwash 'El Profe'</p>
    <p>&copy; 2025 Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)