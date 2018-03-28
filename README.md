## Curso Python Web Rest

### Pré - requisitos
* MongoDB
* Python 3.*
* NodeJS

Após clonar o repositório segue abaixo os passos para a execução

### BackEnd
1. Entrar na pasta do projeto
```
 $ cd CursoPythonWeb/backend
```
2. Instale o virtualenv
```
 $ pip install virtualenv
```
3. Agora habilite o virtualenv
```
 $ virtualenv env
 $ env\Scripts\activate
```
4. Você irá visualizar que o command line mudou para (env)
```
 $ (env)
```
5. Agora instale todas as dependencias que estão no arquivo requirements.txt
```
 $ pip install -r requirements.txt
```
6. Após isso certifique-se que o MongoDB está instalado e execute a aplicação
```
$ python run.py -h 0.0.0.0 
```
Resultado esperado
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-123-123
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
*** Não feche o terminal, ele irá mostrar todo o log do projeto.

### FrontEnd
Tendo o nosso servidor de API todo em funcionamento, vamos excutar o servidor de FrontEnd.
1. possuindo o node instalado, execute o comando abaixo em outra janela de terminal.
```
 $ cd CursoPythonWeb/frontend
```
2. Instalando todos as dependencias do FrontEnd.
```
 $ npm install
```
2. Após tudo instalado vamos iniciar nosso servidor.
```
 $ npm start
```
Resultado Esperado.
```
> curso_python_web@1.0.0 start C:\Users\lclpe\Projetos\CursoPythonWeb\frontend
> nodemon server.js

[nodemon] 1.17.2
[nodemon] to restart at any time, enter `rs`
[nodemon] watching: *.*
[nodemon] starting `node server.js`
```
*** Também não feche o terminal, irá gerar log do frontend

Após tudo isso concluido, entre no navegador e digite 

http://localhost:8080

E faça o uso da aplicação!
