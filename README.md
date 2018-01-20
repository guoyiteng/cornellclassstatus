# Cornell Class Status

A python script to check the availability of class in Cornell from [Class Roster](https://classes.cornell.edu)

## Dependencies

```
python3
requests
bs4
selenium
phantomjs
```

Recommend using linux server

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

- Run the script
```
python Main.py CS 3410 LEC 001 config.json
python Main.py CS 2110 DIS 202 config.json

Using nohup command on linux server
nohup python -u Main.py CS 3410 LEC 001 &
```
# Enrollment Course

## Usage

- edit the user.json file

- Run the script

python Status.py MATH 4370

Using nohup command on linux server
nohup python -u Status.py MATH 4370 &
