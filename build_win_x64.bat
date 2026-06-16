@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

set VENV_DIR=.venv
set REQUIREMENTS=requirements-dev.txt

echo [INFO] Проверка наличия виртуального окружения
if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo [INFO] Виртуальное окружение не найдено. Создаём
    python -m venv %VENV_DIR%
    if errorlevel 1 (
        echo [ERROR] Не удалось создать виртуальное окружение
        pause
        exit /b
    )
)

echo [INFO] Активация виртуального окружения
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo [ERROR] Не удалось активировать виртуальное окружение
    pause
    exit /b
)

echo [INFO] Установка зависимостей из %REQUIREMENTS%
pip install -r %REQUIREMENTS%
    if errorlevel 1 (
        echo [ERROR] Ошибка установки зависимостей
        pause
        exit /b
    )

echo [INFO] Stage 1/2. Сборка проекта
pyinstaller --noconfirm "WatermarkEditor.spec"
if errorlevel 1 (
    echo [ERROR] Ошибка сборки
    pause
    exit /b
)

echo [INFO] Stage 2/2. Копирование файлов
xcopy /E /I /Y pics dist\WatermarkEditor\pics
xcopy /E /I /Y fonts dist\WatermarkEditor\fonts

echo [SUCCESS] Сборка завершена. Результат в dist\WatermarkEditor\