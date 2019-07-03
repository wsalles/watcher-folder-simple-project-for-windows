@echo off

IF EXIST venv (
	cmd /k "venv\Scripts\activate & python file-copy\run.py"
) ELSE (
	python -m venv venv
	cmd /k "venv\Scripts\activate & pip install -r requirements.txt & python file-copy\run.py"
)