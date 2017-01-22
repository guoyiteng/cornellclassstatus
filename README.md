# Cornell Class Ctatus

A python script to check the availability of class in Cornell from [Class Roster](https://classes.cornell.edu)

说白了就是一个可以帮你抢到课的小工具，它会在有空位的时候发邮件提醒你。

## Dependencies

```
python3
requests
bs4
```

Recommend using linux server

这样就可以不用挂着电脑啦

## Usage

- Edit the config.json

```Json
{
	"sender": {
		"email_addr": "example@example.com", 
		"password": "password", 
		"smtp_server": "smtp.example.com", 
		"smtp_port": "465, Please use SSL Connection"
	},
	"receiver": {
		"email_addr": "example@gmail.com"
	}
}
```

推荐sender使用qq邮箱，qq邮箱的smtp是smtp.qq.com，端口是465

- Run the script
```
python Main.py CS 3410 LEC 001
python Main.py CS 2110 DIS 202

Using nohup command on linux server
nohup python Main.py CS 3410 LEC 001

Please use kill -2 to kill the process in order to get a full log
```
最后，祝大家选课加油，好好学习，鸡年大吉吧！

You can ignore any Chinese in this README

If there is any bug, please report it. I will fix that soon.