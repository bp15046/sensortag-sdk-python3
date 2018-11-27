import bluepy
import time


class SensorTag():
    def __init__(self, mac_addr):
        self._mac_addr = mac_addr        
    
    def enable(self):
        try:
            self._sensor_tag = bluepy.sensortag.SensorTag(self._mac_addr)

        except bluepy.btle.BTLEException:
            return 0
        
        self._sensor_tag.accelerometer.enable()
        self._sensor_tag.humidity.enable()
        self._sensor_tag.magnetometer.enable()
        self._sensor_tag.barometer.enable()
        self._sensor_tag.gyroscope.enable()
        self._sensor_tag.lightmeter.enable()
        self._sensor_tag.battery.enable()

        self.accelerometer_sensor = self._sensor_tag.accelerometer
        self.humidity_sensor      = self._sensor_tag.humidity
        self.magnetometer_sensor  = self._sensor_tag.magnetometer
        self.barometer_sensor     = self._sensor_tag.barometer
        self.gyroscope_sensor     = self._sensor_tag.gyroscope
        self.light_sensor         = self._sensor_tag.lightmeter
        self.battery_sensor       = self._sensor_tag.battery
        
        time.sleep(0.9) # This is better

        return 1

    def disable(self):
        try:
            self._sensor_tag.accelerometer.disable()
            self._sensor_tag.humidity.disable()
            self._sensor_tag.magnetometer.disable()
            self._sensor_tag.barometer.disable()
            self._sensor_tag.gyroscope.disable()
            self._sensor_tag.lightmeter.disable()
            self._sensor_tag.battery.disable()

        except bluepy.btle.BTLEException:
            return 0
        
        self.accelerometer_sensor = None
        self.humidity_sensor      = None
        self.magnetometer_sensor  = None
        self.barometer_sensor     = None
        self.gyroscope_sensor     = None
        self.light_sensor         = None
        self.battery_sensor       = None

        return 1

    def read_accelerometer_sensor(self):
        """
        return : dict
            {"accelerometer_sensor" : 
                {"accel_x" : float},
                {"accel_y" : float},
                {"accel_z" : float}
            }
        """
        accel_x, accel_y, accel_z = self.accelerometer_sensor.read()

        value_dit = dict()
        value_dit.update({'accel_x' : float(accel_x)})
        value_dit.update({'accel_y' : float(accel_y)})
        value_dit.update({'accel_z' : float(accel_z)})

        return {'accelerometer_sensor' : value_dit}

    def read_humidity_sensor(self):
        """
        return 
            {"humidity_sensor" : 
                {"temperature" : float},
                {"humidity"    : float}
            }
        """
        temperature, humidity = self.humidity_sensor.read()

        value_dit = dict()
        value_dit.update({'temperature' : float(temperature)})
        value_dit.update({'humidity'    : float(humidity)})

        return {'humidity_sensor' : value_dit}

    def read_magnetometer_sensor(self):
        """
        return
            {"magnetometer_sensor" : 
                {"mag_x" : float},
                {"mag_y" : float},
                {"mag_z" : float}
            }
        """
        mag_x, mag_y, mag_z = self.magnetometer_sensor.read()

        value_dit = dict()
        value_dit.update({'mag_x' : float(mag_x)})
        value_dit.update({'mag_y' : float(mag_y)})
        value_dit.update({'mag_z' : float(mag_z)})

        return {'magnetometer_sensor' : value_dit}
    
    def read_barometer_sensor(self):
        """
        return 
            {"barometer_sensor" : 
                {"temperature" : float},
                {"pressure"    : float}
            }
        """
        temperature, pressure = self.barometer_sensor.read()

        value_dit = dict()
        value_dit.update({'temperature' : float(temperature)})
        value_dit.update({'pressure'    : float(pressure)})

        return {'barometer_sensor' : value_dit}

    def read_gyroscope_sensor(self):
        """
        return
            {"gyroscope_sensor" : 
                {"gyro_x" : float},
                {"gyro_y" : float},
                {"gyro_z" : float}
            }
        """
        gyro_x, gyro_y, gyro_z = self.gyroscope_sensor.read()
        
        value_dit = dict()
        value_dit.update({'gyro_x' : float(gyro_x)})
        value_dit.update({'gyro_y' : float(gyro_y)})
        value_dit.update({'gyro_z' : float(gyro_z)})

        return {'gyroscope_sensor' : value_dit}

    def read_light_sensor(self):
        """
        return 
            {"light_senor" : 
                {"light" : float}
            }
        """
        light = self.light_sensor.read()

        value_dit = dict()
        value_dit.update({'light' : float(light)})

        return {'light_sensor' : value_dit}

    def read_battery_sensor(self):
        """
        return 
            {"battery_sensor" : 
                {"battery" : int}
            }
        """
        battery = self.battery_sensor.read()

        value_dit = dict()
        value_dit.update({'battery' : int(battery)})

        return {'battery_sensor' : value_dit}
