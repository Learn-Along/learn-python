# Hello-World (Python) - Linux

This it the start up project for anyone attempting to learn python

## How to use git

- Installing git if you don't have it

  ```bash
  sudo apt install git
  ```

- Copying a repository

  ```bash
  git clone <repo link>
  ```

  e.g.

  ```bash
  git clone https://github.com/Learn-Along/learn-python.git
  ```

- Creating a branch on the repo

  ```bash
  git branch <name_of_branch>
  ```

- Entering the branch

  ```bash
  git checkout <name of branch>
  ```

- Update a local repository from a remote one

  ```bash
  git pull origin <name of branch>
  ```

- Update a remote repository from a local repository

  ```bash
  git push origin <name of branch>
  ```

## Python Crash Course

- [w3schools python tutorial](https://www.w3schools.com/python/default.asp)
- [Django girls](https://tutorial.djangogirls.org/en/)

## Steps

- Install Python 3 if you haven't yet
- Create the project folder, say learn-python and enter it

  ```bash
  mkdir learn-python && cd learn-python
  ```

- Create the virtual environment

  ```bash
  python -m venv env
  ```

  where `env` is the name of the environment

- Activate the environment

  ```bash
  source env/bin/activate
  ```

- Install flask

  ```bash
  pip install flask
  ```

- Follow the [Quick start tutorial for flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

## Good to Have

- [PEP 8](https://www.python.org/dev/peps/pep-0008/) - Good coding guidelines for python
- [Test drive development (TDD)](https://hackernoon.com/introduction-to-test-driven-development-tdd-61a13bc92d92) - Write automatic tests before writing the source code that makes it work

## Projects

- [Flask Scotch.io tutorial part 1 - TDD](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
- [Flask Scotch.io tutorial part 2 - TDD](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way-part-2)
