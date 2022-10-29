# Entrega_Intermedia_Sebastian_Moreno
- Entrega intermedia del proyecto final de coder
1. Abrir Git Bash para Windows o una terminal para Linux/Unix.
2. Seleccionar alguna carpeta de preferencia
3. Utilizar comando
cd git clone https://github.com/sealmoar/Entrega_Intermedia_Sebastian_Moreno.git
4. Abrir VS Code y una terminal allí
code .
En seguida en VSCode damos Ctrl+j o Terminal/New Terminal y en esta terminal seguimos ejecutando los comandos que siguen a continuación.

5. Activar entorno virtual
(Windows)
6. Instalar las dependencias del proyecto
pip install -r requirements.txt
8. Se crean las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django
python manage.py makemigrations
9. Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
python manage.py migrate
10. Se crea el super usuario para nuestro proyecto de Django, Solo si no se ha creado
python manage.py createsuperuser
Ingrese Username, Email address y Password
11. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto http://127.0.0.1:8000/
python manage.py runserver
12. En la parte izquierda están las aplicaciones del blog
13. Consta de una guarderia de moscotas en donde se pueden crear y visualizar Mascotas, Dueños de mascotas, servicios de la guardería y sucursales.
Cuenta con un buscador de mascotas en el home.
