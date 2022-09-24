from UCASSrunLogin.LoginManager import LoginManager

lm = LoginManager()
lm.login(
    username = "username",
    password = "password"
)
print('在公用服务器上登录校园网账户后，为避免流量误用，请在网络使用完毕后，运行logout.py脚本手动下线账户！')
