import json

with open("data/user_profile.json", "r") as f:
    profile = json.load(f)

print(profile)
print(profile["goal"])