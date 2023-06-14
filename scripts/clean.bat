rd /s /q .\Data
rem Eliminare il file output.txt
del /F /Q .\output.txt
rem Eliminare i file risposta_{}.png
del /F /Q .\risposta*
rem Eliminare il pycache
rd /s /q .\scarica\__pycache__ 
rd /s /q .\cerca\__pycache__   