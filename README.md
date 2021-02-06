
This application enables you to create notes about your events with the possibility of notification by email. 
You can also get a list of holidays of the country that you indicated during registration. 

## Usage
Event_book provides an API that gives you several ways to create and get your holidays and events.

#### Register (https://pythonpetproject.monster/event/register)
```
data = {
    "username": "exampleuser",
    "email": "example@example.com",
    "password": "example",
    "country": "13"
}
response = post("https://pythonpetproject.monster/event/register", data=data)
```
Country - from 3 to 224

#### Create token(https://pythonpetproject.monster/event/create_token)
```
data = {
    "login": "exampleuser",
    "pwd": "example",
    "email": "example@example.com"
}
response = post("https://pythonpetproject.monster/event/create_token", data=data)
```
You will receive the token to the email

#### Login(https://pythonpetproject.monster/event/loginuser)
```
data = {
    "email": "example@example.com",
    "password": "example"
}
response = post("https://pythonpetproject.monster/event/loginuser", data=data)
```

#### Add event (https://pythonpetproject.monster/event/addevent) (use your token in headers)
```
headers = {"Authorization": "Token 55b78141eb7795aba66d8bd20f93793b74a627dc"}
data = {
    "event": "Suprize",
    "date_event": "2021-02-05",
    "time_start": "19:00:00"
}
response = post("https://pythonpetproject.monster/event/addevent", headers=headers)
```
You can use in data time_end for your event and remind.
Types of remind:
- timedelta(seconds=3600) - 1 hour reminder
- timedelta(seconds=7200) - 2 hour reminder
- timedelta(seconds=14400) - 3 hour reminder
- timedelta(seconds=86400) - week reminder
- timedelta(seconds=604800) - month reminder

#### Getting a list of events for today (pythonpetproject.monster/event/yourevents) (use your token in headers)
```
headers = {"Authorization": "Token 55b78141eb7795aba66d8bd20f93793b74a627dc"}
response = get("https://pythonpetproject.monster/event/yourevents", headers=headers)
```
#### Getting a list of events for month (pythonpetproject.monster/event/yourmonthevents) (use your token in headers)
```
headers = {"Authorization": "Token 55b78141eb7795aba66d8bd20f93793b74a627dc"}
response = get("https://pythonpetproject.monster/event/yourmonthevents", headers=headers)
```
#### Getting a list of holidays for month (pythonpetproject.monster/event/yourmonthevent) (use your token in headers)
```
headers = {"Authorization": "Token 55b78141eb7795aba66d8bd20f93793b74a627dc"}
response = get("https://pythonpetproject.monster/event/yourmonthevent", headers=headers)
```
You can use params holiday_begin and you get holidays for year, month or day
```
data = {"holiday_begin": "2022-08"}
headers = {"Authorization": "Token 55b78141eb7795aba66d8bd20f93793b74a627dc"}
response = get("https://pythonpetproject.monster/event/yourmonthevents", headers=headers, data=data)
```
