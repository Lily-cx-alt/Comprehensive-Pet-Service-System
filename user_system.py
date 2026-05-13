# 软件工程实验5 - 用户注册与登录系统（特性分支新代码）
import json


def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def register():
    print("=== 用户注册 ===")
    username = input("请输入用户名：")
    password = input("请输入密码：")

    users = load_users()
    if username in users:
        print("用户名已存在！")
        return
    users[username] = password
    save_users(users)
    print("注册成功！")


def login():
    print("=== 用户登录 ===")
    username = input("用户名：")
    password = input("密码：")

    users = load_users()
    if users.get(username) == password:
        print("登录成功！欢迎回来！")
    else:
        print("用户名或密码错误")


def main():
    while True:
        print("\n===== 主菜单 =====")
        print("1. 用户注册")
        print("2. 用户登录")
        print("3. 退出系统")
        choice = input("请选择功能：")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("系统退出")
            break
        else:
            print("输入无效")


if __name__ == "__main__":
    main()