
# аутентификация
users = [{
    "username": "ntab",
    "phone": "996555444333"
}
    ,
    {
        "username": "das",
        "phone": "996777444333"
    }
]


def auth_decarotor(func):
    def wrapper(*args, **kwargs):
        if args:
            username = args[0]
            phone = args[1]
        if kwargs:
            print(kwargs)
            username = kwargs["username"]
            phone = kwargs.get("phone_number")
        auth_dict = {"username": username, "phone": phone}
        if auth_dict in users:
            func(*args, **kwargs)
        else:
            raise Exception(f"Пользователь под именем {username} не зарегестрирован!!!")

    return wrapper

@auth_decarotor
def get_user(username, phone_number):
    print(f"hello {username}")


get_user(username="ntab", phone_number="996555444333")

# print({"username": "ntaby", "phone": "996555444333"} in users)
