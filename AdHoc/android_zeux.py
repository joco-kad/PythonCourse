import random
class _Sensor:
    def _read_stat_phys(self):
        return random.random()

class PhysRobot:
    def __init__(self):
        self._sensor = _Sensor()

    def __str__(self):
        return "Bessere Ausgabe... Mein Status: %4.2f" % (self.read_status())

    def __repr__(self):
        return super().__repr__() + " " + str(self.read_status())

    def read_status(self):
        return self._sensor._read_stat_phys()

class _Brain:
    def __read_kyb_status(self):
        return random.random()

    def _get_status_value(self, stat_phys):
        stat_gesamt = (stat_phys + self.__read_kyb_status()) / 2.0
        if stat_gesamt < 0.25:
            return "schlecht"
        elif stat_gesamt >= 0.25 and stat_gesamt < 0.5:
            return "geht so"
        elif stat_gesamt >= 0.5 and stat_gesamt < 0.75:
            return "gut"
        else:
            return "hervorragend"

class Android(PhysRobot):
    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__brain = _Brain()

    def __str__(self):
        stat_phys = self._sensor._read_stat_phys()
        return "Ich heisse %s und fühle mich: %s" % (self.__name, \
                                                     self.__brain._get_status_value(stat_phys))
        
    status = property(__str__)
     
