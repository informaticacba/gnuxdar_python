# vamos a importar flask
from flask import Flask, render_template, request, redirect, url_for
import os  # importar el módulo del sistema operativo

app = Flask(__name__)
# para dejar de almacenar en caché el archivo estático
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')  # este decorador crea la ruta home
def home():
    techs = ['PHP', 'Codeigniter', 'Laravel', 'Magento2', 'Python', 'Flask']
    users = ['luis angles coc', 'crash', 'master pro', 'wukong', 'delvis', 
             'otto', 'el papu xd', 'espectrohn', 'pata de hierro', 'computer', 
             'yo', 'antonio', 'blasete', 'destructor', 'billied', 'k2', 'joseaguilera', 
             'alfonso', 'mk', 'cris', 'king cat', 'andres vnzla', 'renato cfc', 
             'recucus', 'daniel', 'anderson', 'rey torres', 'gaston ramos', 'marcos', 
             'kevin pro', 'popo', 'faraon', 'hugo 11', 'jose manuel', 'samugamer', 
             'elias', 'lopez', 'alauakbar', 'juan david', 'memosau'
             ]
    size_users = len(users)
    users_to_delete = ['master pro', 'espectrohn',
                       'joseaguilera', 'alfonso', 'mk', 'king cat', 'andres vnzla', 
                       'renato cfc', 'recucus', 'anderson', 'gaston ramos', 'marcos',
                       'kevin pro', 'faraon', 'jose manuel', 'samugamer', 'juan david']
    size_delete = len(users_to_delete)
    users_success = [x for x in users if x not in users_to_delete]
    size_us = len(users_success)
    name = 'Elearning Python'
    # return '<h1>Welcome</h1>'
    return render_template('home.html', techs=techs, name=name, users=users, users_to_delete=users_to_delete,size_users=size_users, size_delete=size_delete, users_success=users_success, size_us=size_us, title='home')


@app.route('/about')
def about():
    name = 'Elearning Python'
    # return '<h1>About us</h1>'
    return render_template('about.html', name = name, title = 'Sobre nosotros')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    name = 'Formulario de Contacto'
    if request.method == 'GET':
        return render_template('contact.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('home'))

if __name__ == '__main__':
    # para el despliegue
    # para que funcione tanto para la producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)