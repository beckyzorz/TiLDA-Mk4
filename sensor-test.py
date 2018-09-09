# This file contains some tests to ensure that the sensors on the TiLDA Mk4 are working correctly.

# Libraries
from tilda import Sensors

# TMP102 / Temperature Sensor (in degrees celsius)
print(Sensors.get_tmp_temperature())

# HDC2080 / Humidity Sensor (in relative humidity percentage)
print(Sensors.get_hdc_temperature())

# OPT3001 / Light Level Sensor (in Lux)
print(Sensors.get_lux())

# Magnetic Flux Sensor
Sensors.hall_effect.get_flux()
