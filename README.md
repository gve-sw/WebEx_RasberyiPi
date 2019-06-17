# WebEx teams IoT integration
This is a prototype for an IoT automation using WebExteams APIs and a Rasbery Pi

## Usage:
Clone this repo into your raspbery PI:
```
$ git clone hhttps://github.com/Abdellbar/Asset_tracking_POV
```
set up a DHT11 tempreature sensor with your Raspbery Pi, click here for instruction of wiring and hardwar setup.
get your WebEx room id and update the code with your WebEx teams API key

Install dependencies :
```
$ pip install Adafruit_DHT
$
```

Lunch the code by issueing 
```
$ python tempsensor.py
```