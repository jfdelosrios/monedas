#!/bin/bash

python -m venv .env # Crea ambiente en path (carpeta) .env
source .env/Scripts/activate # activa el ambiente
pip install -r requirements.txt # Lee el archivo requirements.txt e instala los modulos que esten escritos en este
deactivate