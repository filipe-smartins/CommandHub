@echo off

echo.
echo.
echo RUNNING LINTER
echo.
echo.

:: Ativação do ambiente virtual
call .venv\Scripts\activate

:: Navegação até o diretório do source code
cd .\src\

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


:: Pausa para aguardar a entrada do usuário
pause