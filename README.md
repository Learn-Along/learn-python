# Hello-World (Python) - Linux

This it the start up project for anyone attempting to learn python

## How to use git

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

## Steps

- Install git if you don't have it

  ```bash
  sudo apt install git
  ```

- Install Python if you haven't yet
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

## Projects
