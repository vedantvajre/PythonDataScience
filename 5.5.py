current_users = ['Bob', 'Billy', 'anupama', 'sam', 'Kathryn']
new_users = ['Clark', 'bob', 'Vedant', 'Pinot', 'john']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry, " + new_user + " has been used. Try another one!")
    else:
        print(new_user + " is available.")