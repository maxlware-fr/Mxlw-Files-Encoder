from pathlib import Path
from mxlw import encrypt_file

# Mot de passe à mettre ici
password = "PASSWORD_HERE"

# Le chemin du fichier
file = Path("exemple.txt")

# La fonction d'encrypt
encrypt_file(file, password)
