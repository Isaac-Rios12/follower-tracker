
import re
from typing import Set


def is_candidate_username(line: str) -> bool:
    """
    Reglas básicas de un username de Instagram
    """
    if not line:
        return False
    if line == "·":
        return False
    if " " in line:
        return False
    if line != line.lower():
        return False
    if not re.search(r"[a-z0-9]", line):
        return False
    return True

def parse_raw_followers(file_path: str) -> Set[str]:
    usernames: Set[str] = set()
    expecting_username = True

    with open(file_path, "r", encoding="utf-8") as file:
        for i, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            print(f"\nLínea {i}: '{line}'")
            print(f"  expecting_username = {expecting_username}")

            # Separadores explícitos
            if not line or line == "·":
                print(" Separador detectado, espero nuevo username")
                expecting_username = True
                continue

            # Línea NO candidata
            if not is_candidate_username(line):
                print("  No es candidata a username, reseteo estado")
                expecting_username = True
                continue

            # Línea candidata
            if expecting_username:
                print(f" username detectado: {line}")
                usernames.add(line)
                expecting_username = False
            else:
                print(f"candidata ignorada (ya hay username en bloque): {line}")

    return usernames