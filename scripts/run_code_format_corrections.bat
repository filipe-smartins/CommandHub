@echo off

echo.
echo.
echo RUNNING CODE FORMAT CORRETIONS
echo.
echo.

:: Ativação do ambiente virtual
call .venv\Scripts\activate

:: Navegação até o diretório do source code
cd .\src\

isort .
blue .

echo.
echo.
echo PROCESS COMPLETED
echo.
echo.

:: Pausa para aguardar a entrada do usuário
pause