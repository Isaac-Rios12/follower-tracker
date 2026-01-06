from typing import Set

def write_user_list(file_path: str, users: Set[str]) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        for user in sorted(users):
            file.write(f"{user}\n")