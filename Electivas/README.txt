django-admin startproject project_name
manage.py startapp app_name
manage.py migrate
nanage.py makemigrations

en app_name/admin se escribre todo la logica de negocio
admin.site.register(Electiva)

en project_name/settings 
se debe agregar app_name.apps.app_name
                              |nombre de la clase|
y se debe colocar en templates
os.path.join(BASE_DIR,'Template')

en project_name/urls incluir
path('',include('app_name.urls')), 
e importar include