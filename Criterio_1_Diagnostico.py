import streamlit as st
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(layout="wide", page_title="Diagnóstico Financiero MYPE 'El Profe'")

# --- 2. ESTILOS CSS (Nivel Consultor) ---
st.markdown("""
<style>
    /* Estilos base */
    [data-testid="stAppViewContainer"] > .main {
        background-color: #F8F9FA; /* Un gris muy sutil */
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #0A111F; /* Más oscuro, más premium */
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
    
    [data-testid="stSidebar"] [data-testid="stExpander"] details {
        background-color: #1a273b;
        border-radius: 8px;
    }
    [data-testid="stSidebar"] [data-testid="stExpander"] summary {
        color: white;
        font-weight: 500;
    }

    /* Contenedores principales */
    [data-testid="stVerticalBlock"] [data-testid="stContainer"] {
        background-color: #FFFFFF; 
        border: 1px solid #E0E0E0; 
        box-shadow: 0 8px 16px rgba(0,0,0,0.05); /* Sombra más profesional */
        border-radius: 12px; 
        padding: 25px; 
        margin-bottom: 20px; 
    }
    
    /* Títulos */
    h1, h2, h3, h4 {
        color: #0A111F; 
        font-weight: 600;
    }

    /* Métrica Personalizada */
    [data-testid="stMetricValue"] {
        font-size: 3.5rem;
        color: #D9534F; /* Rojo para el riesgo */
        font-weight: 600;
    }
    [data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    
    /* Pestañas */
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 500;
    }

    /* Expander Personalizado */
    [data-testid="stExpander"] details {
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        background-color: #FDFEFE;
    }
    [data-testid="stExpander"] summary {
        font-size: 1.1rem;
        font-weight: 600;
        color: #0A111F;
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


# --- 3. LÓGICA DE LA APLICACIÓN (FUNCIONES) ---

@st.cache_data
def get_maturity_levels():
    """Define los niveles de madurez para la auditoría."""
    return {
        "balance": {
            "No Registrado": 1,
            "Básico (Excel)": 4,
            "Software Contable": 10
        },
        "resultados": {
            "No Registrado": 1,
            "Estimado (Notas)": 3,
            "Software Contable": 10
        },
        "flujo_caja": {
            "Inexistente (Caja Chica)": 1,
            "Básico (Excel)": 5,
            "Proyectado (Software)": 10
        }
    }

def render_sidebar():
    """Crea el Panel de Auditoría y retorna las selecciones."""
    st.sidebar.title("TA4 - Gestión Financiera")
    st.sidebar.divider()
    
    st.sidebar.header("Panel de Auditoría")
    st.sidebar.markdown("Define el estado actual de la MYPE:")
    
    levels = get_maturity_levels()
    
    balance_status = st.sidebar.selectbox(
        "1. Balance General", 
        options=list(levels["balance"].keys()),
        index=0, # Default: "No Registrado"
        help="Nivel de formalidad del Balance General."
    )
    
    resultados_status = st.sidebar.selectbox(
        "2. Estado de Resultados",
        options=list(levels["resultados"].keys()),
        index=0, # Default: "No Registrado"
        help="Nivel de formalidad del Estado de Resultados."
    )
    
    flujo_status = st.sidebar.selectbox(
        "3. Flujo de Caja",
        options=list(levels["flujo_caja"].keys()),
        index=0, # Default: "Inexistente (Caja Chica)"
        help="Nivel de control sobre el Flujo de Caja."
    )
    
    st.sidebar.divider()
    with st.sidebar.expander("Ver Metodología del Diagnóstico"):
        st.markdown("<small>El diagnóstico se basa en los hallazgos de la entrevista con el propietario, aplicados a la rúbrica de la TA4.</small>", unsafe_allow_html=True)
        
    return balance_status, resultados_status, flujo_status

def calculate_maturity(b_status, r_status, f_status):
    """Calcula el puntaje de madurez basado en las selecciones."""
    levels = get_maturity_levels()
    max_score = sum(max(d.values()) for d in levels.values()) # 10 + 10 + 10 = 30
    
    score = levels["balance"][b_status] + levels["resultados"][r_status] + levels["flujo_caja"][f_status]
    
    percentage = int((score / max_score) * 100)
    
    if percentage <= 10:
        level_text = "Nivel 1: Empírico"
        delta_color = "inverse"
        style_color = "#D9534F" # Rojo
    elif percentage <= 40:
        level_text = "Nivel 2: Básico"
        delta_color = "normal"
        style_color = "#F0AD4E" # Naranja
    else:
        level_text = "Nivel 3: Controlado"
        delta_color = "normal"
        style_color = "#5CB85C" # Verde
        
    return percentage, level_text, delta_color, style_color

def render_tab_content(title, diagnostic_status, content_map):
    """Función genérica para renderizar el contenido de las pestañas."""
    
    if diagnostic_status in [list(content_map.keys())[0]]: # Si es la peor opción
        st.error(f"**Diagnóstico:** {diagnostic_status}", icon="🚨")
    elif diagnostic_status in [list(content_map.keys())[1]]: # Si es la opción intermedia
        st.warning(f"**Diagnóstico:** {diagnostic_status}", icon="⚠️")
    else:
        st.success(f"**Diagnóstico:** {diagnostic_status}", icon="✅")

    content = content_map[diagnostic_status]
    st.markdown(content["definicion"], unsafe_allow_html=True) # Permitir HTML en la definición
    
    with st.expander(f"Ver Análisis y Riesgos de este Nivel..."):
        st.markdown(content["riesgos"], unsafe_allow_html=True) # Permitir HTML en los riesgos
        if "ejemplo" in content:
            st.dataframe(content["ejemplo"], use_container_width=True)

# --- MAPAS DE CONTENIDO (La "Base de Datos" del Dashboard) ---
BALANCE_CONTENT = {
    "No Registrado": {
        # --- CORREGIDO AQUÍ (class='highlight') ---
        "definicion": "Es la <span class='highlight'>'fotografía del patrimonio'</span> de la empresa. Muestra **Activos** (posee), **Pasivos** (debe) y **Patrimonio** (valor real).",
        "riesgos": """
        * ❌ **Falta de Medición Patrimonial:** El dueño <span class="highlight">desconoce el valor real de su negocio</span>.
        * ❌ **Barrera para Financiamiento:** Es un <span class="highlight">requisito indispensable para obtener créditos bancarios</span>.
        * ❌ **Evaluación de Solvencia:** Imposibilidad de evaluar la <span class="highlight">solidez financiera</span> de la empresa.
        """
    },
    "Básico (Excel)": {
        "definicion": "Es un registro manual en hojas de cálculo. Es un primer paso, pero sigue siendo vulnerable.",
        "riesgos": """
        * ⚠️ **Riesgo de Error Humano:** Un error de fórmula o de tipeo puede distorsionar toda la contabilidad.
        * ⚠️ **Falta de Integridad:** No está conectado a bancos ni a ventas, requiriendo doble digitación.
        * ⚠️ **Consumo de Tiempo:** El registro manual es lento y propenso a desfases.
        * ✅ **Punto Positivo:** Permite una visión básica de Activos vs. Pasivos.
        """
    },
    "Software Contable": {
        "definicion": "Uso de un sistema (ej. CONCAR, Siscont, o SaaS en la nube) que automatiza la generación del balance.",
        "riesgos": """
        * ✅ **Nivel Óptimo:** Genera reportes confiables y en tiempo real.
        * ✅ **Integridad de Datos:** Se integra con facturación, bancos y planillas.
        * ✅ **Requisito para Auditoría:** Es la única fuente válida para auditorías y financiamiento serio.
        """
    }
}

RESULTADOS_CONTENT = {
    "No Registrado": {
        # --- CORREGIDO AQUÍ (class='highlight') ---
        "definicion": "Es la <span class='highlight'>'película de la rentabilidad'</span> en un período. Compara **Ingresos** vs. **Costos y Gastos** para hallar la **Utilidad Neta**.",
        "riesgos": """
        * ❌ **Confusión entre Caja y Utilidad:** El dueño <span class="highlight">confunde tener dinero con ser rentable</span>.
        * ❌ **Gestión de Costos Ineficaz:** Imposibilidad de <span class="highlight">identificar y controlar costos</span> que merman las ganancias.
        * ❌ **Cumplimiento Fiscal:** Es la base para el Impuesto a la Renta y su ausencia puede generar <span class="highlight">multas con la SUNAT</span>.
        """
    },
    "Estimado (Notas)": {
        "definicion": "El dueño tiene una idea general o 'al ojo' de sus ganancias, restando costos obvios (alquiler, insumos) de las ventas diarias.",
        "riesgos": """
        * ⚠️ **Costos Ocultos Ignorados:** Falla en contabilizar depreciación, amortizaciones, gastos pequeños (transporte, comisiones bancarias).
        * ⚠️ **Sin Precisión:** Imposible saber el margen de utilidad exacto (ej. 10% vs 12%).
        * ⚠️ **No Válido para Impuestos:** Sigue siendo insuficiente para una declaración de renta precisa.
        * ✅ **Punto Positivo:** Indica una preocupación básica por la rentabilidad.
        """
    },
    "Software Contable": {
        "definicion": "El sistema genera automáticamente el Estado de Resultados a partir de los registros de ventas y compras.",
        "riesgos": """
        * ✅ **Nivel Óptimo:** Permite análisis de rentabilidad por servicio, cliente o período.
        * ✅ **Decisiones de Precios:** Fundamental para fijar precios basados en márgenes reales.
        * ✅ **Cumplimiento Fiscal Total:** Base para el cálculo de impuestos.
        """
    }
}

FLUJO_CAJA_CONTENT = {
    "Inexistente (Caja Chica)": {
        # --- CORREGIDO AQUÍ (class='highlight') ---
        "definicion": "Es el <span class='highlight'>movimiento de dinero en efectivo</span>. Es el indicador más vital de la <span class='highlight'>salud a corto plazo</span> (liquidez).",
        "riesgos": """
        * ❌ **RIESGO DE INSOLVENCIA/QUIEBRA:** La amenaza más grave. <span class="highlight">Quedarse sin efectivo</span> para pagar planillas, alquiler o proveedores.
        * ❌ **Estrés Financiero Constante:** El dueño vive en incertidumbre sobre si tendrá dinero para las próximas obligaciones.
        * ❌ **Oportunidades Perdidas:** Incapacidad para aprovechar descuentos o invertir por <span class="highlight">falta de liquidez</span>.
        """
    },
    "Básico (Excel)": {
        "definicion": "Se lleva un registro manual de entradas y salidas de efectivo en una hoja de cálculo, a menudo al final del día o la semana.",
        "riesgos": """
        * ⚠️ **No es Proyectivo:** Es un registro *histórico*, no una *proyección*. No ayuda a anticipar problemas de liquidez futuros.
        * ⚠️ **Desactualizado:** El registro manual puede tener días de retraso, ocultando un problema inmediato.
        * ✅ **Punto Positivo:** Es el primer paso para entender dónde se va el dinero.
        """
    },
    "Proyectado (Software)": {
        "definicion": "Uso de una herramienta (como la propuesta en el Criterio 2) para *proyectar* el flujo de caja futuro, basándose en cuentas por cobrar, por pagar y proyecciones de ventas.",
        "riesgos": """
        * ✅ **Nivel Óptimo:** Permite tomar decisiones *antes* de que falte el dinero.
        * ✅ **Gestión de Tesorería:** Permite planificar pagos e inversiones de excedentes.
        * ✅ **Base para la Estrategia:** Responde a preguntas como "¿Podemos contratar a alguien el próximo mes?".
        """
    }
}


# --- 4. RENDERIZADO DE LA APLICACIÓN ---

# Llama a la sidebar y obtiene los valores seleccionados
b_status, r_status, f_status = render_sidebar()

# Spinner de carga
with st.spinner('Calculando Diagnóstico basado en la Auditoría...'):
    time.sleep(1) # Simula un cálculo
    percentage, level_text, delta_color, style_color = calculate_maturity(b_status, r_status, f_status)

# Título principal
st.title("🚗 Criterio 1: Análisis y Diagnóstico Financiero")
st.markdown("### Carwash 'El Profe' - Trabajo Académico 4")

# --- Diagnóstico General (Consolidado) ---
st.header("Diagnóstico General y Nivel de Madurez")
with st.container(border=True):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        Tras la auditoría, se detecta que la MYPE opera con una gestión financiera en el nivel **{level_text}**.
        
        El estado actual de sus registros contables y financieros se basa en:
        * **Balance:** `{b_status}`
        * **Resultados:** `{r_status}`
        * **Flujo de Caja:** `{f_status}`
        """)
        
        if percentage <= 10:
             st.markdown(f'<div class="risk-high">RIESGO CRÍTICO: La MYPE opera sin visibilidad y está expuesta a riesgos de liquidez y sostenibilidad.</div>', unsafe_allow_html=True)

    with col2:
        # Métrica de Impacto (KPI) con estilo dinámico
        st.markdown(f'<style>[data-testid="stMetricValue"] {{ color: {style_color}; }}</style>', unsafe_allow_html=True)
        st.metric(
            label="Nivel de Madurez Financiera", 
            value=f"{percentage}%", 
            delta=level_text,
            delta_color=delta_color,
            help="Puntaje máximo = 100% (Gestión Optimizada)"
        )
    
    st.progress(percentage)

st.divider() 
st.header("Análisis de los 3 Aspectos")

tab1, tab2, tab3 = st.tabs([
    "🏦 Balance General (Patrimonio)", 
    "📈 Estado de Resultados (Rentabilidad)", 
    "💵 Flujo de Caja (Liquidez)"
])

with tab1:
    render_tab_content("Balance General", b_status, BALANCE_CONTENT)

with tab2:
    render_tab_content("Estado de Resultados", r_status, RESULTADOS_CONTENT)

with tab3:
    render_tab_content("Flujo de Caja", f_status, FLUJO_CAJA_CONTENT)


# --- Pie de Página ---
st.markdown("""
<div class="footer">
    <p>Proyecto TA4 - Gestión Financiera de MYPEs | Carwash 'El Profe'</p>
    <p>&copy; 2025 Todos los derechos reservados.</p>
</div>
""", unsafe_allow_html=True)