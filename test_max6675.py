#!/usr/bin/python

from max6675 import MAX6675, MAX6675Error
import time

cs_pin = 8
clock_pin = 11
data_pin = 9
units = "c"

thermocouple = MAX6675(cs_pin, clock_pin, data_pin)
thermocouple.cleanup()
time.sleep(1)
thermocouple = MAX6675(cs_pin, clock_pin, data_pin)
t_end = time.time() + 30
while time.time()  < t_end:
	print(thermocouple.get())
	time.sleep(1)

thermocouple.cleanup()
