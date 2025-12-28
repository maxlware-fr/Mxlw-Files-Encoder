from pathlib import Path
from mxlw import encrypt_file

password = "PASSWORD_HERE"

file = Path("exemple.txt")

encrypt_file(file, password)
