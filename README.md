# comunidadeimpressionadora
Projeto de desenvolvimento web com Python utilizando Flask, Bootstrap, HTML, CSS. 

Projeto web em python de site em formato de blog. Contém tela de login e criação de usuários com integração em banco de dados para armazenamento de dados de usuários. 
-> **Tela de homepage**: contém a exibição dos posts criados, exibidos da forma mais recente de criação. Neste tela temos os posts, usuário que realizou aquele post, data de criação, informações daquele usuário, o corpo e o título daquele post. 
-> **Edição de posts**: cada post leva consigo um link que direciona o usuário para uma tela onde é possível editar o corpo, o titulo e até mesmo excluir aquele post do banco de dados (caso o usuário seja o autor daquele post, caso contrário, não há essa opção). 
-> **Criação de posts**: tela onde o usuário logado consegue criar novos posts de discussão. O post fica guardando em banco e é atrelado ao perfil que criou aquele post, sendo um dos itens que é mostrado nos perfis dos usuários. 
-> **Tela de usuários**: possui informações de todos os usuários que constam na base de dados, incluindo o nome de usuário, cursos atrelados naquele perfil, quantidade de posts que ele fez e a imagem de perfil. 
-> **Tela de perfil**: tela onde o usuário visualiza e consegue editar suas informações do perfil, como alterar o email, senha e a imagem do perfil. Alteração reflete no banco de dados e armazena as mudanças.
-> **Tela de criação de perfil / Login**: tela onde usuários que não estejam logados consigam logar com contas já pré criadas ou então realizar a criação de novas contas para que o acesso seja realizado posteriormente, habilitando todos os campos do site para criação de posts e outras edições que liberam apenas com um usuário válido logado.  
