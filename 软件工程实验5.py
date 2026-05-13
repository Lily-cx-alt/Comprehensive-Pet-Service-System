# 综合宠物服务平台：实现用户注册功能，校验用户名和密码，返回注册结果
def pet_platform_register(username, password):
    # 校验用户名：长度必须在3-20之间，且只能包含字母、数字和下划线
    if not (3 <= len(username) <= 20):
        return "用户名长度必须在3-20之间"
    if not username.isalnum() and "_" not in username:
        return "用户名只能包含字母、数字和下划线"

    # 校验密码：长度必须至少6个字符，且必须包含至少一个大写字母、一个小写字母和一个数字
    if len(password) < 6:
        return "密码长度必须至少6个字符"
    if not any(c.isupper() for c in password):
        return "密码必须包含至少一个大写字母"
    if not any(c.islower() for c in password):
        return "密码必须包含至少一个小写字母"
    if not any(c.isdigit() for c in password):
        return "密码必须包含至少一个数字"

    # 注册成功
    return "注册成功"