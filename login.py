from UCASSrunLogin.LoginManager import LoginManager

lm = LoginManager()
lm.login(
    username = "username",
    password = "password"
)
print('为避免流量误用，请使用logout.py脚本手动下线账户！')
