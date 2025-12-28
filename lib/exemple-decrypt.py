from pathlib import Path
from mxlw import decrypt_file

# Chemin du fichier à décrypter
fichier_mxlw = Path("exemple.txt.mxlw")

# Ici le même mot de passe que vous avez encodé
mot_de_passe = "PASSWORLD_HERE"

try:
    fichier_dechiffre = decrypt_file(fichier_mxlw, mot_de_passe)
    print(f"Fichier déchiffré → {fichier_dechiffre}")
except Exception as e:
    print("Erreur lors du déchiffrement :", e)
