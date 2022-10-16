from random import randint


def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)


def get_pressure(sensor):
    return randint(720, 740) if sensor else randint(740, 760)


def get_wind_speed(sensor):
    return randint(0, 15) if sensor else randint(15, 50)