from src.parser import parse_raw_followers

followers = parse_raw_followers("data/raw/followers_day1.txt")
# print(followers)

print("usernames detectados: ")
for user in sorted(followers):
    print(user)