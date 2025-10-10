#!/bin/bash

echo
echo
echo "RUNNING LINTER"
echo
echo

# Ativação do ambiente virtual
source .venv/bin/activate

# Navegação até o diretório do source code
cd ./src/

# Executa o pylint
pylint .

echo.
echo.
echo RUNNING IMPORTS SORT AND FORMAT CHECK
echo.
echo.

isort . --check


echo.
echo.
echo RUNNING CODE FORMAT CHECK
echo.
echo.


blue . --check

echo.
echo.
echo PROCESS COMPLETED
echo.
echo.

# Pausa para aguardar a entrada do usuário
read -p "Pressione Enter para continuar..."