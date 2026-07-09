from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpresssionadora.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class FormCriarConta(FlaskForm):
    """
    username(str), email(str), senha(password), confirmacao(password), botao_submit_criarconta(button);
    """
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Seu e-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Sua senha', validators=[DataRequired(), Length(8, 20)])
    confirmacao_senha =PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Crie sua conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Faça login ou utilize outro e-mail para se cadastrar")

    def validate_username(self, username):
        username = Usuario.query.filter_by(username= username.data).first()
        if username:
            raise ValidationError("Nome de usuário já está em uso, necessário que seu nome de usuário seja único")


class FormLogin(FlaskForm):
    """
        email(str), senha(password), botao_submit_login(button);
    """
    email = StringField('Seu e-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Sua senha', validators=[DataRequired(), Length(8, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer login')


class FormEditarConta(FlaskForm):
    email = StringField(label= 'Seu e-mail', validators=[DataRequired(), Email()])
    username = StringField(label='Seu nome de usuário', validators=[DataRequired()])
    foto_perfil = FileField('Atualizar a foto de perfil', validators=[FileAllowed(['jpg', 'png', 'webp', 'jpeg'])])
    curso_python = BooleanField('Python Impressionador')
    curso_powerbi = BooleanField('PBI Impressionador')
    curso_analise_dados = BooleanField('Analise de dados Impressionadora')
    curso_excel = BooleanField('Excel Impressionador')
    curso_N8N = BooleanField('N8N Impressionador')
    botao_submit_editar_perfil = SubmitField('Confirmar edições de perfil')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email= email.data).first()
            if usuario:
                raise ValidationError("E-mail já cadastrado. Utilize outro endereço.")

    def validate_username(self, username):
        if current_user.username != username.data:
            nome_usuario = Usuario.query.filter_by(username= username.data).first()
            if nome_usuario:
                raise ValidationError("Nome de usuário já em uso. Escolha outro nome de exibição")


class FormCriarPost(FlaskForm):
    titulo = StringField("Titulo do post", validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField("Escreva seu post aqui", validators=[DataRequired()])
    botao_submit_post = SubmitField('Criar post')