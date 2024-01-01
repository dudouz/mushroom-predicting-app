# Mushroom Evaluator

![Mushroom Evaluator](https://github.com/dudouz/mvp-4/blob/master/mvp/frontend/public/android-chrome-192x192.png)

## MBA in Software Engineering - PUCRIO

Hello, this is the fourth MVP of the MBA in Software Engineering at PUCRIO.

This example consists of a system that uses a machine learning model to make predictions.

The idea here is to evaluate a mushroom based on its detailed characteristics and, through this, predict whether it is edible or poisonous.

### Used Dataset

[Mushroom - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/73/mushroom)

# Installation and Usage

This application consists of two modules, one for the front-end and another for the back-end.

While the front-end is developed in TypeScript, using React, the back-end was built in Python and uses the Flask framework.

Keep in mind that we need a Node.js and Python development environment to run these applications, or if you prefer, we can run them from a Docker container.

## Running using Docker

We have a `docker.compose.yaml` in our repository, so we can build and run our applications with just one command, remembering that we need to have Docker installed and configured correctly:

```shell
foo@bash:~$ docker compose up
```

## Front-end Manual Compilation

To individually build our front-end, we recommend using the yarn package manager.

Go to the /mvp/frontend/ folder and execute the following command:

```shell
foo@bash:~$ yarn
```

To run the application, build it first, and then preview it:

```shell
foo@bash:~$ yarn build; yarn preview
```

Using `;` we run one command after the completion of the other :)

## Back-end Manual Compilation

To individually build our back-end, we recommend using venv in Python.

Go to the /mvp/backend/ folder and execute the following command to isolate your build in a virtual environment:

```shell
foo@bash:~$ python3 -m venv venv; source venv/bin/activate
```

Using `;` we run one command after the completion of the other :)

After that, still in the /mvp/backend folder, install the project dependencies:

```shell
foo@bash:~$ pip install -r requirements.txt
```

To run the application, build it first, and then preview it:

```shell
foo@bash:~$ flask --app app run --host 0.0.0.0
```
# Accessing the System

Regardless of the method you choose, our apps will be available at the following URLs:

### Front-end

[http://localhost:4173/](http://localhost:4173/)

### Back-end

[http://localhost:5000/](http://localhost:5000/)

#### Swagger

[http://localhost:5000/openapi](http://localhost:5000/openapi)

# Running Tests

Our back-end has tests to validate the effectiveness of the provided model. We assume a high criterion for this predictor, expecting an accuracy of 98% or more.

To run the tests, go to the /mvp/backend/ folder and execute the following command to isolate your build in a virtual environment:

```shell
foo@bash:~$ python3 -m venv venv; source venv/bin/activate
```

Using `;` we run one command after the completion of the other :)

After that, still in the /mvp/backend folder, install the project dependencies:

```shell
foo@bash:~$ pip install -r requirements.txt
```

After that, still in the /mvp/backend folder, execute pytest and wait for the output:

```shell
foo@bash:~$ pytest
```
