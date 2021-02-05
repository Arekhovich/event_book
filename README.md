
This application enables you to create notes about your events with the possibility of notification by email. 
You can also get a list of holidays of the country that you indicated during registration. 

## Usage
Event_book provides an API that gives you several ways to create and get your holidays and events.

#### Register
```
data = {
    'username': 'exampleuser',
    'email': 'example@example.com',
    'password': 'example',
    'country': '13'
}
response = post('https://pythonpetproject.monster/event/register', data=data)
```
#### Create token
```
data = {
    'login': 'exampleuser',
    'pwd': 'example',
    'email': 'example@example.com'
}
response = post('https://pythonpetproject.monster/event/create_token', data=data)
```
You will receive the token to the email

#### Add event (use your token in headers)
```
headers = {'Authorization': 'Token 55b78141eb7795aba66d8bd20f93793b74a627dc'}
response = post('https://pythonpetproject.monster/event/addevent', headers=headers)
```
#### Getting a list of events for today (use your token in headers)
```
headers = {'Authorization': 'Token 55b78141eb7795aba66d8bd20f93793b74a627dc'}
response = get('https://pythonpetproject.monster/event/yourevents', headers=headers)
```
#### Getting a list of events for month (use your token in headers)
```
headers = {'Authorization': 'Token 55b78141eb7795aba66d8bd20f93793b74a627dc'}
response = get('https://pythonpetproject.monster/event/yourmonthevents', headers=headers)
```
#### Getting a list of holidays for month (use your token in headers)
```
headers = {'Authorization': 'Token 55b78141eb7795aba66d8bd20f93793b74a627dc'}
response = get('https://pythonpetproject.monster/event/yourmonthevents', headers=headers)
```
You can use params holiday_begin and you get holidays for year, month or day
```
data = {'holiday_begin': '2022-08'}
headers = {'Authorization': 'Token 55b78141eb7795aba66d8bd20f93793b74a627dc'}
response = get('https://pythonpetproject.monster/event/yourmonthevents', headers=headers, data=data)
```
