from comunidadeimpresssionadora import app, database, bcript
from flask import render_template
from comunidadeimpresssionadora.forms import FormLogin, FormCriarConta, FormEditarConta, FormCriarPost
from flask import redirect, url_for, flash, request, abort
from comunidadeimpresssionadora.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


# lista_usuarios = ['Luan', 'Rodrigo', 'Luide']

@app.route("/")
def homepage():
    posts = Post.query.order_by(Post.id.desc())
    return render_template("homepage.html", posts=posts)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/usuarios")
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)

@app.route('/login_criarconta', methods= ['GET', 'POST'])
def login_criarconta():
    criar_conta_form = FormCriarConta()
    login_form = FormLogin()

    if login_form.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=login_form.email.data).first()
        if usuario and bcript.check_password_hash(usuario.senha, login_form.senha.data):
            login_user(usuario, remember= login_form.lembrar_dados.data)
            flash(f"Login feito com sucesso com o e-mail: {login_form.email.data}", 'alert-success')
            request_url = request.args.get('next')
            if request_url:
                return redirect(request_url)
            else:
                return redirect(url_for("homepage"))
        else:
            flash("Falha no login. E-mail ou senha incorretos", 'alert-danger')
    if criar_conta_form.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcript.generate_password_hash(criar_conta_form.senha.data)
        usuario = Usuario(username=criar_conta_form.username.data, email= criar_conta_form.email.data,
                        senha= senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f"Conta criada com sucesso com o e-mail: {criar_conta_form.email.data}",
              'alert-success')
        return redirect(url_for("homepage"))
    return render_template("login_criarconta.html", login_form=login_form,
                           criar_conta_form=criar_conta_form)

@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash('Logout feito com sucesso', 'alert-sucess')
    return redirect(url_for('homepage'))

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename= f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('perfil.html', foto_perfil=foto_perfil)


def salvar_imagem(imagem):
    # codigo de "encriptação unica da imagem, separação do nome e da extensão (splitext.filename), nome do arquivo
    # caminho completo, definição do tamanho, imagem reduzida (Image.open()) imagem.save
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    imagem_reduzida = Image.open(imagem)
    tamanho = (380, 380)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_arquivo


def atualizar_curso(formulario):
    lista_cursos = []
    for campo in formulario:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return ';'.join(lista_cursos)

@app.route('/perfil/editar', methods= ['GET', 'POST'])
@login_required
def editar_perfil():
    formulario = FormEditarConta()
    if formulario.validate_on_submit():
        current_user.email = formulario.email.data
        current_user.username = formulario.username.data
        if formulario.foto_perfil.data:
            imagem = salvar_imagem(formulario.foto_perfil.data)
            current_user.foto_perfil = imagem
        current_user.cursos = atualizar_curso(formulario)
        database.session.commit()
        flash('Perfil atualizado com sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        formulario.email.data = current_user.email
        formulario.username.data = current_user.username

    foto_perfil = url_for('static', filename= f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editar_perfil.html',formulario= formulario, foto_perfil= foto_perfil)

@app.route('/post/criar', methods= ['GET', 'POST'])
@login_required
def criar_post():
    formulario = FormCriarPost()
    if formulario.validate_on_submit():
        post = Post(titulo=formulario.titulo.data, corpo=formulario.corpo.data, autor= current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso', 'alert-success')
        return redirect(url_for('homepage'))
    return render_template('criar_post.html', formulario= formulario)

@app.route('/post/<post_id>', methods= ['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        formulario = FormCriarPost()
        if request.method == 'GET':
            formulario.titulo.data = post.titulo
            formulario.corpo.data = post.corpo
        elif formulario.validate_on_submit():
            post.titulo = formulario.titulo.data
            post.corpo = formulario.corpo.data
            database.session.commit()
            flash('Post atualizado com sucesso' 'alert-success')
            return redirect(url_for('homepage'))
    else:
        formulario = None
    return render_template('post.html', post= post, formulario=formulario)

@app.route('/post/<post_id>/excluir', methods= ['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post exluído com sucesso', 'alert-danger')
        return redirect(url_for('homepage'))
    else:
        abort(403)
