import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_age = [user for user in users if user["age"] == age]

    if len(filtered_users_age) > 0:
        for user in filtered_users_age:
         print(user)
    else:
        print("No users found")

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_email = [user for user in users if email.lower() in user["email"].lower()]

    if len(filtered_users_email) > 0:
        for user in filtered_users_email:
            print(user)
    else:
        print("No users found")

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name', 'age' and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(int(age_to_search))
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
