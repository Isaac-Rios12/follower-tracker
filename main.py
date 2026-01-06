import argparse

from src.parser import parse_raw_followers
from src.comparator import compare_followers

from src.writer import write_user_list
import os

def get_args():
    parser = argparse.ArgumentParser(
        description="Instagram follower tracker"
    )

    parser.add_argument(
        "day1",
        help="Follower file from day 1"
    )
    parser.add_argument(
        "day2",
        help="Follower file from day 2"
    )

    return parser.parse_args()

def validate_input_file(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file doesnt exist: {path}")
    if os.path.getsize(path) == 0:
        raise ValueError(f"The file is empty: {path}")



def main():
    args = get_args()
    #me aseguro que exista
    try:
        validate_input_file(args.day1)
        validate_input_file(args.day2)
        os.makedirs("output", exist_ok=True)

        followers_day1 = parse_raw_followers(args.day1)
        followers_day2 = parse_raw_followers(args.day2)

        unfollowers, new_followers = compare_followers(
            followers_day1,
            followers_day2
        )
        if not unfollowers and not new_followers:
            print("No hay cambios entre los días.")
            return


        write_user_list("output/unfollowers.txt", unfollowers)
        write_user_list("output/new_followers.txt", new_followers)

        print("Archivos generados en /output")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()