@echo off
echo Installing required Python packages...
python -m pip install --upgrade pip

REM 
pip install openai
pip install exa-py
pip install TTS
pip install gTTS
pip install requests

echo.
echo All packages have been installed successfully!
pause