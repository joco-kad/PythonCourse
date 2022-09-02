import random

class _Sensor:
    def __init__(self):
        self.__stat_phys = self._read_stat_phys()
        print("Hilfe! Ich werde aufgerufen")

    def _read_stat_phys(self):
        return random.random()
"""
class PhysRobot:
    def __init__(self):
        self.__sensor = _Sensor()

    def __str__(self):
        return "Mein physikalischer Zustand: %s" % (self.__sensor._read_stat_phys())

class _Brain:
    def __read_stat_kyb(self):
        return random.random()

    def _read_readable_stat(self, stat_phys):
        stat = (stat_phys + self.__read_stat_kyb()) / 2.0
        if stat < 0.25:
            return "schlecht"
        elif stat >= 0.25 and stat < 0.5:
            return "geht so"
        elif stat >= 0.5 and stat < 0.75:
            return "gut"
        else:
            return "hevorragend"
    
class Android(PhysRobot):
    def __init__(self):
        super().__init__()
        self.__brain = _Brain()
        self.__sensor = self._PhysRobot__sensor
    
    def __str__(self):
        return "Mein Zustand: " + self.__brain._read_readable_stat(self.__sensor._read_stat_phys())
    """
