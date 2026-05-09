# Atividade Pratica - Arquitetura Cliente-Servidor (Cliente / UI)

Este repositorio contem a aplicacao Front-end (Lado Cliente) do MVP da livraria virtual, desenvolvido para a disciplina de Engenharia de Software. Neste modulo da **Arquitetura Cliente-Servidor**, o sistema e responsavel exclusivamente pela Interface do Usuario (Views) e pela experiencia de navegacao.

## 1. O Papel do Cliente

O Cliente atua como uma "vitrine". Ele nao possui acesso direto ao banco de dados e nao processa regras de negocio complexas. Toda vez que um usuario faz uma pesquisa, adiciona um item ao carrinho ou finaliza uma compra, o Cliente encapsula essa acao e faz uma solicitacao (Request) ao Servidor, aguardando a resposta para atualizar a tela.

## 2. Tecnologias e Conceitos Aplicados

Para tornar a comunicacao possivel, implementamos:

* **Consumo de API (Biblioteca Requests):** Utilizamos a biblioteca `requests` do Python para realizar chamadas HTTP aos endpoints do Servidor. O Cliente solicita os dados, aguarda o recebimento do JSON e, em seguida, injeta essas informacoes nos templates HTML.
* **Desacoplamento Total:** Como o Cliente e o Servidor estao separados, a equipe de Front-end pode alterar cores, fontes e layouts sem qualquer risco de quebrar o banco de dados. Da mesma forma, se o Servidor mudar o banco de TXT para SQL, o Cliente nao precisara sofrer nenhuma alteracao.
* **Tratamento de Excecoes:** O codigo do Cliente foi protegido com blocos `try/except` para garantir que, caso o Servidor esteja offline, a aplicacao nao quebre bruscamente, mas sim exiba telas vazias tratadas (Empty States) para o usuario.

## 3. Como Executar

O Cliente depende do Servidor (API) para exibir os livros. Certifique-se de que o Servidor esta rodando na porta 5000 antes de iniciar.

1. Instale as dependencias: `pip install Flask requests`
2. Execute o arquivo principal: `python app.py`
3. O Cliente estara disponivel no navegador na porta 5001 (`http://127.0.0.1:5001`).

## Front Conectado com o back: 

<img width="1023" height="489" alt="image" src="https://github.com/user-attachments/assets/a9763639-b3fb-4a95-a622-b5b6ee6337f9" />
