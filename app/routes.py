from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        nome = form.get('nome')
        telefone = form.get('telefone')
        endereco = form.get('endereco')
        cpf = form.get('cpf')
        if not nome or telefone or endereco or cpf:
            entry = Entry(nome = nome, telefone = telefone, endereco=endereco, cpf=cpf)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "usuário cadastrado"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "usuário atualizado"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            nome = form.get('nome')
            telefone = form.get('telefone')
            endereco = form.get('endereco')
            cpf = form.get('cpf')
            entry.nome = nome
            entry.telefone = telefone
            entry.endereco = endereco
            entry.cpf = cpf
            db.session.commit()
        return redirect('/')

    return "usuário atualizado"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "usuário deletado"

@app.route('/turn/<int:id>')
def turn(id):
    
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            nome = form.get('nome')
            telefone = form.get('telefone')
            endereco = form.get('endereco')
            cpf = form.get('cpf')
            db.session.commit()
        return redirect('/')

    return "usuário"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"