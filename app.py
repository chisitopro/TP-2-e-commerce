"""
RetroVerse - Demo académica de e-commerce de objetos vintage y retro.
Aplicación de demostración con Streamlit.

NOTA: No incluye autenticación, pagos reales ni base de datos persistente.
Los datos se simulan en memoria a partir del registro "Producto" diseñado
previamente, para fines exclusivamente didácticos.
"""

import streamlit as st

# -----------------------------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="RetroVerse",
    page_icon="🕹️",
    layout="wide",
)

# -----------------------------------------------------------------------
# DATOS DE EJEMPLO (simulan la tabla "Producto" de la base de datos)
# Cada diccionario respeta el modelo de registro diseñado anteriormente.
# -----------------------------------------------------------------------
PRODUCTOS = [
    {
        "producto_id": "8f14e45f-ceea-4a9a-9c1b-2b1d3e4f5a6b",
        "titulo": "Cámara Polaroid SX-70 Land Camera",
        "descripcion": "Cámara instantánea plegable de los años 70, funcionamiento "
                       "mecánico verificado, fuelle sin roturas, incluye correa original.",
        "categoria": "Fotografía",
        "subcategoria": "Cámaras analógicas",
        "marca": "Polaroid",
        "modelo": "SX-70",
        "anio_fabricacion": 1973,
        "condicion": "Buen estado",
        "nivel_rareza": "Raro",
        "puntuacion_conservacion": 8,
        "completo_con_caja_manual": False,
        "funcional": True,
        "certificado_autenticidad": False,
        "precio": 185.00,
        "moneda": "USD",
        "modalidad_venta": "Venta directa",
        "acepta_intercambio": True,
        "peso_kg": 0.6,
        "dimensiones_cm": "18 x 10 x 4",
        "ubicacion": "Resistencia, Chaco, Argentina",
        "etiquetas": ["fotografía analógica", "polaroid", "vintage 70s"],
        "imagen": "polaroid.jpg",
    },
    {
        "producto_id": "1a2b3c4d-5e6f-7081-92a3-b4c5d6e7f809",
        "titulo": "Consola Nintendo Game Boy Clásica (1989)",
        "descripcion": "Game Boy original color gris, pantalla sin rayas ni píxeles "
                       "muertos. Incluye cartucho de Tetris.",
        "categoria": "Tecnología",
        "subcategoria": "Consolas",
        "marca": "Nintendo",
        "modelo": "DMG-01",
        "anio_fabricacion": 1989,
        "condicion": "Usado",
        "nivel_rareza": "Poco común",
        "puntuacion_conservacion": 6,
        "completo_con_caja_manual": False,
        "funcional": True,
        "certificado_autenticidad": False,
        "precio": 95.50,
        "moneda": "USD",
        "modalidad_venta": "Subasta",
        "acepta_intercambio": False,
        "peso_kg": 0.4,
        "dimensiones_cm": "15 x 9 x 3",
        "ubicacion": "Buenos Aires, Argentina",
        "etiquetas": ["nintendo", "8 bits", "videojuegos retro"],
        "imagen": "https://placehold.co/400x300?text=Game+Boy+1989",
    },
    {
        "producto_id": "9c8b7a6d-5e4f-3a2b-1c0d-e9f8a7b6c5d4",
        "titulo": "Vinilo \"Abbey Road\" - Edición original 1969",
        "descripcion": "Disco de vinilo en buen estado de conservación, funda con "
                       "leves signos de uso, sin rayas profundas en el surco.",
        "categoria": "Música",
        "subcategoria": "Vinilos",
        "marca": "Apple Records",
        "modelo": "LP Abbey Road",
        "anio_fabricacion": 1969,
        "condicion": "Buen estado",
        "nivel_rareza": "Muy raro",
        "puntuacion_conservacion": 7,
        "completo_con_caja_manual": True,
        "funcional": None,
        "certificado_autenticidad": True,
        "precio": 320.00,
        "moneda": "USD",
        "modalidad_venta": "Venta directa",
        "acepta_intercambio": True,
        "peso_kg": 0.3,
        "dimensiones_cm": "31 x 31 x 1",
        "ubicacion": "Córdoba, Argentina",
        "etiquetas": ["vinilo", "beatles", "música 60s"],
        "imagen": "https://placehold.co/400x300?text=Vinilo+Abbey+Road",
    },
    {
        "producto_id": "4d3c2b1a-0f9e-8d7c-6b5a-4938271605f4",
        "titulo": "Máquina de escribir Remington Rand modelo 5",
        "descripcion": "Máquina de escribir mecánica completamente funcional, "
                       "teclas originales, cinta nueva instalada.",
        "categoria": "Hogar y oficina",
        "subcategoria": "Máquinas de escribir",
        "marca": "Remington Rand",
        "modelo": "Modelo 5",
        "anio_fabricacion": 1938,
        "condicion": "Restaurado",
        "nivel_rareza": "Pieza única",
        "puntuacion_conservacion": 9,
        "completo_con_caja_manual": False,
        "funcional": True,
        "certificado_autenticidad": True,
        "precio": 450.00,
        "moneda": "USD",
        "modalidad_venta": "Subasta",
        "acepta_intercambio": False,
        "peso_kg": 5.2,
        "dimensiones_cm": "35 x 30 x 20",
        "ubicacion": "Rosario, Argentina",
        "etiquetas": ["máquina de escribir", "art déco", "restaurado"],
        "imagen": "https://placehold.co/400x300?text=Remington+Rand",
    },
]

# -----------------------------------------------------------------------
# ESTADO DE NAVEGACIÓN
# Streamlit no maneja "páginas" con URL por defecto en esta demo,
# por lo que usamos st.session_state para simular la navegación
# entre el catálogo y el detalle de producto.
# -----------------------------------------------------------------------
if "producto_seleccionado" not in st.session_state:
    st.session_state.producto_seleccionado = None


def ir_a_detalle(producto_id: str):
    st.session_state.producto_seleccionado = producto_id


def volver_al_catalogo():
    st.session_state.producto_seleccionado = None


def buscar_producto_por_id(producto_id: str):
    """Busca un producto en la lista en memoria usando su clave única."""
    for p in PRODUCTOS:
        if p["producto_id"] == producto_id:
            return p
    return None


# -----------------------------------------------------------------------
# PANTALLA 2: DETALLE DE PRODUCTO
# -----------------------------------------------------------------------
def mostrar_detalle(producto: dict):
    st.button("← Volver al catálogo", on_click=volver_al_catalogo)

    st.markdown("---")

    # Clave principal destacada
    st.code(f"producto_id: {producto['producto_id']}", language="text")

    col_img, col_info = st.columns([1, 2])

    with col_img:
        st.image(producto["imagen"], use_container_width=True)

    with col_info:
        st.title(producto["titulo"])

        m1, m2, m3 = st.columns(3)
        m1.metric("Rareza", producto["nivel_rareza"])
        m2.metric("Conservación", f"{producto['puntuacion_conservacion']}/10")
        m3.metric("Año", producto["anio_fabricacion"])

        st.subheader(f"{producto['moneda']} {producto['precio']:.2f}")
        st.caption(f"Modalidad: {producto['modalidad_venta']}")

        if producto["acepta_intercambio"]:
            st.success("✅ Este vendedor acepta intercambios")

        col_a, col_b = st.columns(2)
        col_a.button("🛒 Comprar (demo)", type="primary", use_container_width=True)
        col_b.button("💖 Agregar a favoritos (demo)", use_container_width=True)

    st.markdown("---")

    with st.expander("📋 Descripción completa", expanded=True):
        st.write(producto["descripcion"])
        st.write(f"**Marca:** {producto['marca']}  |  **Modelo:** {producto['modelo']}")
        st.write(f"**Categoría:** {producto['categoria']} / {producto['subcategoria']}")

    with st.expander("🔍 Autenticidad y estado"):
        if producto["certificado_autenticidad"]:
            st.write("✔ Cuenta con certificado de autenticidad")
        else:
            st.write("✘ Sin certificado de autenticidad registrado")
        st.write(f"**Condición general:** {producto['condicion']}")
        st.write(f"**Caja y manual original:** {'Sí' if producto['completo_con_caja_manual'] else 'No'}")
        if producto["funcional"] is None:
            st.write("**Funcional:** No aplica")
        else:
            st.write(f"**Funcional:** {'Sí' if producto['funcional'] else 'No'}")

    with st.expander("📦 Datos de envío"):
        st.write(f"**Peso:** {producto['peso_kg']} kg")
        st.write(f"**Dimensiones:** {producto['dimensiones_cm']} cm")
        st.write(f"**Ubicación de origen:** {producto['ubicacion']}")

    with st.expander("🏷️ Etiquetas"):
        st.write(" ".join([f"`{tag}`" for tag in producto["etiquetas"]]))


# -----------------------------------------------------------------------
# PANTALLA 1: CATÁLOGO
# -----------------------------------------------------------------------
def mostrar_catalogo():
    st.title("🕹️ RetroVerse")
    st.caption("Marketplace de objetos vintage, coleccionables y tecnología retro")

    # --- Filtros en la barra lateral ---
    st.sidebar.header("Filtros")

    categorias = ["Todas"] + sorted({p["categoria"] for p in PRODUCTOS})
    categoria_filtro = st.sidebar.selectbox("Categoría", categorias)

    rarezas = ["Todas"] + sorted({p["nivel_rareza"] for p in PRODUCTOS})
    rareza_filtro = st.sidebar.selectbox("Nivel de rareza", rarezas)

    texto_busqueda = st.sidebar.text_input("Buscar por título")

    # --- Aplicar filtros sobre la lista en memoria ---
    productos_filtrados = PRODUCTOS
    if categoria_filtro != "Todas":
        productos_filtrados = [p for p in productos_filtrados if p["categoria"] == categoria_filtro]
    if rareza_filtro != "Todas":
        productos_filtrados = [p for p in productos_filtrados if p["nivel_rareza"] == rareza_filtro]
    if texto_busqueda:
        productos_filtrados = [
            p for p in productos_filtrados
            if texto_busqueda.lower() in p["titulo"].lower()
        ]

    st.write(f"Mostrando **{len(productos_filtrados)}** de **{len(PRODUCTOS)}** productos")
    st.markdown("---")

    if not productos_filtrados:
        st.info("No se encontraron productos con los filtros seleccionados.")
        return

    # --- Grilla de tarjetas (3 columnas) ---
    columnas = st.columns(3)
    for i, producto in enumerate(productos_filtrados):
        col = columnas[i % 3]
        with col:
            with st.container(border=True):
                st.image(producto["imagen"], use_container_width=True)
                st.subheader(producto["titulo"])
                st.write(f"**{producto['moneda']} {producto['precio']:.2f}**")
                st.caption(f"Condición: {producto['condicion']}  |  Rareza: {producto['nivel_rareza']}")
                # Clave única visible en la tarjeta (versión corta)
                st.caption(f"🔑 ID: {producto['producto_id'][:8]}...")
                st.button(
                    "Ver detalle",
                    key=f"btn_{producto['producto_id']}",
                    use_container_width=True,
                    on_click=ir_a_detalle,
                    args=(producto["producto_id"],),
                )


# -----------------------------------------------------------------------
# ROUTER PRINCIPAL: decide qué pantalla mostrar
# -----------------------------------------------------------------------
if st.session_state.producto_seleccionado is None:
    mostrar_catalogo()
else:
    producto_actual = buscar_producto_por_id(st.session_state.producto_seleccionado)
    if producto_actual:
        mostrar_detalle(producto_actual)
    else:
        st.error("Producto no encontrado.")
        st.button("← Volver al catálogo", on_click=volver_al_catalogo)
