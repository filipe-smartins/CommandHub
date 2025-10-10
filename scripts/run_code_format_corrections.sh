#!/bin/bash

echo ""
echo ""
echo "RUNNING CODE FORMAT CORRECTIONS"
echo ""
echo ""

# Ativação do ambiente virtual
source .venv/bin/activate

# Navegação até o diretório do source code
cd ./src/

isort .
blue .

echo.
echo.
echo PROCESS COMPLETED
echo.
echo.


# Pausa para aguardar a entrada do usuário
read -p "Pressione Enter para continuar..."
