修改自：[BIT-srun-login-script](https://github.com/coffeehat/BIT-srun-login-script)，修改了查询IP的正则表达式以在国科大校园网使用，测试时间2022年3月10日。


# 文件说明
下线脚本似乎会踢掉所有在线设备，不管了将就着用。

|文件|说明|
|:-:|:-:|
|BitSrunLogin/|深澜登录函数包|
|login.py|登录示例脚本|
|logout.py|下线示例脚本|
|always_online.py|在线监测脚本，如果监测到掉线则自动重连|

always_online.py可采用`nohup`命令挂在后台：
``` bash
nohup python always_online.py &
```
