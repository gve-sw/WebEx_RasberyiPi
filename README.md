# WebEx teams IoT integration
This is a prototype for an IoT automation using WebExteams APIs and a Rasbery Pi

## Usage:
Clone this repo into your raspbery PI:
```
$ git clone hhttps://github.com/Abdellbar/WebEx_RasberyiPi
```
set up a DHT11 tempreature sensor with your Raspbery Pi, click [here](https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/) for instruction of wiring and hardwar setup.
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