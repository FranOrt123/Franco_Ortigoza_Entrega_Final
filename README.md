# Instrucciones de Instalación y Ejecución

## Requisitos Previos
- Python 3.x instalado
- Git instalado

## Pasos para Iniciar el Proyecto

1. **Clonar el repositorio**
   ```
   git clone <url-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. **Crear y activar el entorno virtual**
   ```
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**
   ```
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor**
   ```
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Abrir el navegador en: http://127.0.0.1:8000/