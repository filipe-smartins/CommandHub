#!/bin/bash

# ..\run_tests.sh

# Activation of the virtual environment
source .venv/bin/activate

# Navigation to the source code directory
cd .\tests\

echo.
echo.
echo RUNNING TESTS
echo.
echo.

# Running tests with pytest
pytest -v

echo.
echo.
echo RUNNING COVERAGE TESTS
echo.
echo.

# Running coverage tests with pytest-cov
pytest --cov


echo.
echo.
echo RUNNING COMPLEXITY CHECK
echo.
echo.

:: Navigation to the project directory
cd ..

:: Navigation to the source code directory
cd .\src\

:: Execution of Cyclomatic Complexity check
radon cc -s .

:: Halstead Maintenance Index Check Execution
radon mi -s .

echo.
echo.
echo PROCESS COMPLETED
echo.
echo.

# Pause to wait for user input
read -p "Pressione Enter para continuar..."
