# cozie-examples

Coming December 2019. See the Wiki for Documentation

## Purchasing Fitbits

The cozie app is compatible with fitbit models:
* [Ionic](https://www.fitbit.com/ionic)
* [Versa](https://www.fitbit.com/versa)
* [Versa Lite](https://www.fitbit.com/versa-lite) - recommended as it is the cheapest, and has full cozie functionality

https://www.fitbit.com/home

Set up your Fitbit as per instructions on the device, and pair to your mobile phone.

## Downloading Cozie App
Click the following link on your cellphone, and let it autodirect towards the fitbit store. 
https://gam.fitbit.com/gallery/clock/d787c911-ce11-432e-8b68-69da0f3446c8

## Setting Up
In the clock face configurations set
* User ID: This is an anonymous-id to identify the user
* Experiment ID: This is an experiment-id to identify the experiment that your results belong to. You will use this ID to querry the results later
* Questions: Set the questions that you plan on asking.

Make sure that bluetooth is on, and your fitbit is close by and connected. Syncing the fitbit can ensure that the settings persist from the phone to watch

## Extracting Data
Data can be extracted via our API

**URL Key:** https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/

**Parameters**
* experiment-id: The name you set in the cozie settings above (required)
* user-id: The user-id set above (optional, if not included all users are extracted)
* weeks: Weeks of data (optional, default is 2 weeks)

### Extracting Data with Python

```python
import requests

payload = {'experiment-id': 'besh', 'weeks': '30', 'user-id': 'Vivid Vervet'}
response = requests.get('https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/', params = payload)

print(response.content)
```

### Extracting Data with Bash

```bash
$ curl https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/?experiment-id=besh&weeks=3
```

### Extracting Data with Node js

There are multiple methods to access data. You may use `fetch` or `https`

https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

```js
fetch('https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/?experiment-id=besh&weeks=3')
.then(function(response) {return response.json()})
.then(function(myJson) {console.log(JSON.stringify(myJson))});
```

### Extracting as a human using a browser
https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/?experiment-id=<YOUR EXPERIMENT ID>&weeks=<NUMBER_OF_WEEKS>&user-id=<USER-ID(OPTIONAL)>

for example. For Experiment-ID = besh, User-ID = Vivid Vervet, and the last 30 weeks of data:

https://ay1bwnlt74.execute-api.us-east-1.amazonaws.com/test/request/?experiment-id=besh&weeks=30&user-id=Vivid%20Vervet

## Troubleshooting
Please submit any issues to our issue tracker and it will be dealt with :)

https://github.com/buds-lab/cozie-examples/issues 


Here is a quick checklist before submitting an issue
* Check that bluetooth and internet is on, on your cellphone
* Check that you are using the latest version of the cozie app
* Check that your fitbit is up to date
* If settings are not persisting, then try sync your phone to your fitbit manually 
