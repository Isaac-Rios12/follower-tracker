import argparse

from src.parser import parse_raw_followers, load_snapshot
from src.comparator import compare_followers

from src.writer import write_user_list
import os

def get_args():
    parser = argparse.ArgumentParser(
        description="Instagram follower tracker"
    )

    parser.add_argument(
        "current",
        help="Raw file of today's followers"
    )
    return parser.parse_args()

def validate_input_file(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file doesnt exist: {path}")
    if os.path.getsize(path) == 0:
        raise ValueError(f"The file is empty: {path}")

STATE_DIR = "data/state"
LAST_SNAPSHOT = f"{STATE_DIR}/last_followers.txt"

def main():
    args = get_args()
    #me aseguro que exista
    try:
        validate_input_file(args.current)

        os.makedirs(STATE_DIR, exist_ok=True)
        os.makedirs("output", exist_ok=True)

        current_followers = parse_raw_followers(args.current)

        if not os.path.exists(LAST_SNAPSHOT):
            write_user_list(LAST_SNAPSHOT, current_followers)
            print("Base de seguidores creada, ejecute nuevamente para comparar")
            return
        
        previous_followers = load_snapshot(LAST_SNAPSHOT)

        unfollowers, new_followers = compare_followers(
            previous_followers,
            current_followers
        )
        if not unfollowers and not new_followers:
            print("No hay cambios desde la última ejecución.")
        else:
            write_user_list("output/unfollowers.txt", unfollowers)
            write_user_list("output/new_followers.txt", new_followers)
            print("Cambios detectados. Archivos actualizados en /output")


        write_user_list(LAST_SNAPSHOT, current_followers)

        print("Archivos generados en /output")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()