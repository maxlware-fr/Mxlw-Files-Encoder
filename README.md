# Mxlw Files Encoder

Un petit script Python pour **chiffrer et déchiffrer des fichiers** en utilisant un format `.mxlw` sécurisé.  
Les fichiers `.mxlw` ne peuvent être ouverts qu'avec ce script et le mot de passe correct.

## Chiffrer un fichier
1. Choisis 1 dans le menu.
2. Indique le chemin du fichier à chiffrer.
3. Entre un mot de passe.
4. Le fichier chiffré sera créé avec l’extension .mxlw.

## Déchiffrer un fichier
1. Choisis 2 dans le menu.
2. Indique le chemin du fichier .mxlw.
3. Entre le mot de passe utilisé pour le chiffrer.
4. Le fichier déchiffré sera créé avec .decrypted ajouté à son nom.

## Notes
- Le mot de passe est nécessaire pour déchiffrer le fichier. Sans lui, le contenu reste illisible.
- Compatible Windows, Linux et macOS.
- Les chemins Windows doivent utiliser des raw strings (r"C:\chemin\...") ou / comme séparateur.
