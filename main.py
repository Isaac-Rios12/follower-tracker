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



def main():
    args = get_args()
    #me aseguro que exista
    os.makedirs("output", exist_ok=True)

    followers_day1 = parse_raw_followers(args.day1)
    followers_day2 = parse_raw_followers(args.day2)

    unfollowers, new_followers = compare_followers(
        followers_day1,
        followers_day2
    )

    # print("Unfollowers: ")
    # if unfollowers:
    #     for user in sorted(unfollowers):
    #         print(f"- {user}")
    # else:
    #         print("Ninguno")
        

    # print("------------------------------------------------------")
    # print("nuevos seguidores")
    # if new_followers:
    #     for user in sorted(new_followers):
    #         print(f"+ {user}")
    # else:
    #         print("Ninguno")

    write_user_list("output/unfollowers.txt", unfollowers)
    write_user_list("output/new_followers.txt", new_followers)


if __name__ == "__main__":
    main()