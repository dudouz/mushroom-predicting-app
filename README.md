# Avaliador de Cogumelos

## MBA em Engenharia de Software - PUCRIO

Olá, este é o quarto MVP do MBA em engenharia de software da PUCRIO.

Este exemplo consiste num sistema que faz uso de um modelo de aprendizado de máquina para realizar uma predição.

A idéia aqui é avaliar um cogumelo de acordo com suas características em detalhe e, através disso, prever se ele
é comestível ou venenoso.

### Dataset utilizado

[mushroom - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/73/mushroom)

# Instalação e uso

Esta aplicação consite em dois módulos separados, um para o front-end e outro para o back-end.

Enquanto o front-end é desenvolvido em TypeScript, utilizando React, o back-end foi construído em Python e usa o framework flask.

Tenha em mente que precisamos de um ambiente de desenvolvimento node e python para rodar estas aplicações, ou se preferir podemos rodá-las a partir de um container Docker.

## Rodar usando docker

Temos um `docker.compose.yaml` em nosso repositório, assim podemos buildar e rodar nossas aplicações com apenas um comando, lembrando que precisamos ter o docker instalado e configurado corretamente:

```shell
foo@bash:~$ docker compose up
```

## Front-end compilando manualmente

Para buildar individualmente nosso front-end recomendamos o package manager `yarn`

Entre na pasta `/mvp/frontend/` execute o comando

```shell
foo@bash:~$ yarn
```

Para rodar a aplicação, realize um build e depois o seu preview:

```shell
foo@bash:~$ yarn build; yarn preview
```

Usando o `;` nós rodamos um comando após a finalização do outro :)

## Back-end compilando manualmente

Para buildar individualmente nosso back-end recomendamos usar o `venv` do `Python`

Entre na pasta `/mvp/backend/` execute o comando a seguir para isolar seu build em um ambiente virtual:

```shell
foo@bash:~$ python3 -m venv venv; source venv/bin/activate
```

Usando o `;` nós rodamos um comando após a finalização do outro :)

Após isso, ainda na pasta `/mvp/backend` instale as dependências do projeto:

```shell
foo@bash:~$ pip install -r requirements.txt
```

Para rodar a aplicação, realize um build e depois o seu preview:

```shell
foo@bash:~$ flask --app app run --host 0.0.0.0
```

# Acessando o sistema

Independente do meio que você escolheu, nossos apps estarão disponíveis nas seguintes urls:

### Front-end

[http://localhost:4173/](http://localhost:4173/)

### Back-end

[http://localhost:5000/](http://localhost:5000/)

#### Swagger

[http://localhost:5000/openapi](http://localhost:5000/openapi)
