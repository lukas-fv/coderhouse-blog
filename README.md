Intento de proyecto de blog
===================

Este proyecto es un blog muy básico desarrollado en Django para probar los contenidos del curso con el patrón MVT (Modelo-Vista-Template). 
Permite crear publicaciones, categorías y autores para las publicaciones

---------------------------------------------
Funcionalidades principales:
1. Ver publicaciones en la página principal.
2. Agregar nuevas publicaciones con autor y categoría.
3. Listar todas las categorías.
4. Agregar nuevas categorías.
5. Buscar publicaciones por título (de autor, debería funcionar)

---------------------------------------------
Configuración:
1. Clona este repositorio:
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>

2. Activa el entorno virtual:
   Windows: .\env\Scripts\activate
   Linux/Mac: source env/bin/activate

3. Instala las dependencias:
   pip install -r requirements.txt

4. Ejecuta las migraciones:
   python manage.py makemigrations
   python manage.py migrate

5. Inicia el servidor:
   python manage.py runserver

---------------------------------------------
Rutas principales:
- Página principal: `/`
- Listar categorías: `/categories/`
- Agregar categoría: `/categories/add/`
- Agregar publicación: `/add_post/`
- Buscar publicaciones: `/search/`

---------------------------------------------
Orden de prueba sugerido:
1. Accede a la página principal (`/`) para ver las publicaciones.
2. Crea nuevas categorías desde `/categories/add/`.
3. Agrega publicaciones en `/add_post/`.
4. Busca publicaciones con `/search/`.