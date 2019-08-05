# 登录成功
success = [
    {"user": "18684720553", "pwd": "python"},
]

# 登录失败：账号为空、密码为空、手机号码格式不正确、非数字
invalid_data = [
    {"user": "", "pwd": "python", "errInfo": "请输入手机号"},
    {"user": "18684720553", "pwd": "", "errInfo": "请输入密码"},
    {"user": "1868472055", "pwd": "python", "errInfo": "请输入正确的手机号"},
    {"user": "aabbcc", "pwd": "python", "errInfo": "请输入正确的手机号"},
]

# 登录失败：密码错误、手机号码未被注册
exp_snr = [
    {"user": "18684720553", "pwd": "python1", "errInfo": "帐号或密码错误!"},
    {"user": "18611111111", "pwd": "python", "errInfo": "此账号没有经过授权，请联系管理员! !"},
]
