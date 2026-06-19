# RetroVerse — Demo académica (Streamlit)

Aplicación de demostración para un trabajo de análisis de sistemas. Simula
un catálogo de e-commerce de objetos vintage/retro usando el registro
`Producto` diseñado previamente.

## Alcance de la demo

- No incluye autenticación de usuarios.
- No incluye pagos reales (los botones de compra son solo demostrativos).
- Los datos están almacenados en memoria (lista de diccionarios en Python),
  no en una base de datos real. Esto facilita su lectura y modificación
  con fines didácticos.

## Cómo ejecutar

1. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```
   streamlit run app.py
   ```

3. Se abrirá automáticamente en el navegador (por defecto en
   `http://localhost:8501`).

## Estructura de pantallas

- **Catálogo**: lista de productos con filtros por categoría, rareza y
  búsqueda por título.
- **Detalle de producto**: muestra el registro completo, incluyendo la
  clave única (`producto_id`) de forma destacada.

## Modelo de datos

Cada producto es un diccionario en Python que respeta los campos definidos
en el modelo de datos de RetroVerse (ver documento de diseño), incluyendo
campos obligatorios (`titulo`, `precio`, `condicion`, etc.) y opcionales
(`certificado_autenticidad`, `etiquetas`, etc.).
