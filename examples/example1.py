from sensortag.sensortag import SensorTag
import sys


if not len(sys.argv) == 2:
    print("please put your SensorTag Mac Address")
    sys.exit(1)

sensor_tag = SensorTag(sys.argv[1])

print("begin...")


if sensor_tag.enable():
    try:
        while True:
            print("enable SensorTag")
            print(sensor_tag.read_accelerometer_sensor())
            print(sensor_tag.read_humidity_sensor())
            print(sensor_tag.read_magnetometer_sensor())
            print(sensor_tag.read_barometer_sensor())
            print(sensor_tag.read_gyroscope_sensor())
            print(sensor_tag.read_light_sensor())
            print(sensor_tag.read_battery_sensor())
            print()

    except KeyboardInterrupt:
        if sensor_tag.disable():
            print("disable SensorTag")

        else:
            print("didn't disable SensorTag")
    
else:
    print("didn't enable SensorTag")