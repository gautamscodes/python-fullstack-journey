"""

We have the following dictionary containing details:

user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}

Delete the sensitive information from the dictionary
present in a list
sensitive_info = ["password", "address"]

"""
user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_user@example.com",
    "address": "ABC road, 111111",
    "country": "Australia"
}

sensitive_info = ["password", "address", "phone"]

# for i in sensitive_info:
#     user.pop(i)
# print(sensitive_info)
# print(user)

# for i in sensitive_info:
#     print(f"Key: {i}, Value: {user[i]}")
#     user.pop(i)
# print(user)
# print(sensitive_info)

# if keys are not in the dictionary
for i in sensitive_info:
    if i in user:
        print(f"DELETED => Key: {i}, Value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")
print(user)

# if we're using list or dictionary we want to change on that list or dictionary then it will give error.

# for key in user:
#     if key in sensitive_info:
#         user.pop(key)
# print(user)

