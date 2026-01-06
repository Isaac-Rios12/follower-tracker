from src.parser import parse_raw_followers
from src.comparator import compare_followers

# followers = parse_raw_followers("data/raw/followers_day1.txt")
# # print(followers)

# print("usernames detectados: ")
# for user in sorted(followers):
#     print(user)

def main():
    followers_day1 = parse_raw_followers("data/raw/followers_day1.txt")
    followers_day2 = parse_raw_followers("data/raw/followers_day2.txt")

    unfollowers, new_followers = compare_followers(
        followers_day1,
        followers_day2
    )

    print("Unfollowers: ")
    if unfollowers:
        for user in sorted(unfollowers):
            print(f"- {user}")
    else:
            print("Ninguno")
        

    print("------------------------------------------------------")
    print("nuevos seguidores")
    if new_followers:
        for user in sorted(new_followers):
            print(f"+ {user}")
    else:
            print("Ninguno")


if __name__ == "__main__":
    main()