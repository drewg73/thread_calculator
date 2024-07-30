import math

def truncate(f, n):
    return math.trunc(f * (10 ** n)) / 10 ** n

# intent is to have multiple thread profiles
class Thread():
    def __init__(self, size, pitch):
        self._size = size
        self._pitch = pitch

class United_National(Thread):
    def __init__(self, size, pitch, series, thread_class, engagement=None):
        super().__init__(size, (1/pitch))
        self._series = series
        self._thread_class = thread_class
        if engagement:
            self._engagement = engagement
        else:
            # a majority of the tolerance calcs are applicable for thread engagement up to 1.5 * D
            self._engagement = size * 1.5
        
    def __repr__(self):
        return f"{format(self._size, '.3f')}-{format((1/self._pitch), '.0f')} {self._series}-{self._thread_class}"

    # All calc functions are interprited from ASME B1.1-2019 section 5 
    def calc_basic_dimensions(self):
        if self._thread_class.endswith("A"):
            major = self._size
            pitch = major - (2 * (0.32475953 * self._pitch))
            minor = major - (2 * (0.54126588 * self._pitch))
        return list(map(lambda x: format(x, ".4f"), (major, pitch, minor))) 
        
    def calc_allowance(self):
        allowance = 0
        if self._thread_class == "1A" or self._thread_class == "2A":
            td2_2a = truncate(((0.0015 * (self._size ** (1/3))) + (0.0015 * (self._engagement ** (1/2))) + (0.0150 * (self._pitch ** (2/3)))), 6)
            allowance = 0.300 * td2_2a
        return round(allowance, 4)

    def calc_major_tolerance(self):
        if self._thread_class == "1A":
            major_tolerance = 0.0900 * (self._pitch ** (2/3))
        elif self._thread_class == "2A" or self._thread_class == "3A":
            major_tolerance = 0.0600 * (self._pitch ** (2/3))
        elif self._thread_class.endswith("B"):
            major_tolerance = 0.14433757 + self.calc_pitch_tolerance()
        else:
            raise ValueError("Invalid UN Thread Class")
        return round(major_tolerance, 4)

    # not accounting for UNJ threads
    def calc_minor_tolerance(self):
        if self._thread_class.endswith("A"):
            if "R" in self._series:
                minor_tolerance = self.calc_pitch_tolerance() + (0.10825318 * self._pitch)
            else:
                minor_tolerance = self.calc_pitch_tolerance() + (0.21650635 * self._pitch)
            return round(minor_tolerance, 4)
        if self._thread_class == "1B" or self._thread_class == "2B":
            if self._size < 0.250:
                minor_tolerance = ((0.0500 * (self._pitch ** (2/3))) - 0.030 - (self._pitch / self._size)) - 0.002
                if minor_tolerance > 0.39500 * self._pitch:
                    minor_tolerance = 0.39500 * self._pitch
                elif minor_tolerance < ((0.2500 * self._pitch) - (.400 * (self._pitch ** 2))):
                    minor_tolerance = ((0.2500 * self._pitch) - (.400 * (self._pitch ** 2)))
            else:
                if (1/self._pitch) <= 80 and (1/self._pitch) >= 4:
                    minor_tolerance = ((0.2500 * self._pitch) - (.400 * (self._pitch ** 2)))
                else:
                    minor_tolerance = 0.1500 * self._pitch
            return round(minor_tolerance, 4)
        if self._thread_class == "3B":
            minor_tolerance = ((0.0500 * (self._pitch ** (2/3))) + (0.0300 * (self._pitch / self._size))) - 0.002
            if minor_tolerance > 0.39400 * self._pitch:
                minor_tolerance = 0.39400 * self._pitch
            else:
                if (1/self._pitch) <= 80 and (1/self._pitch) >= 13:
                    if minor_tolerance < ((0.2300 * self._pitch) - (1.500 * (self._pitch ** 2))):
                        minor_tolerance = ((0.2300 * self._pitch) - (1.500 * (self._pitch ** 2)))
                else:
                    if minor_tolerance < (0.1200 * self._pitch):
                        minor_tolerance = (0.1200 * self._pitch)
            return round(minor_tolerance, 4)
            
    def calc_pitch_tolerance(self):
        pitch_tolerance = (0.0015 * (self._size ** (1/3))) + (0.0015 * (self._engagement ** (1/2))) + (0.0150 * (self._pitch ** (2/3)))
        if self._thread_class == "1A":
            pitch_tolerance = 1.5000 * truncate(pitch_tolerance, 6)
        elif self._thread_class == "3A":
            pitch_tolerance = 0.7500 * truncate(pitch_tolerance, 6)
        elif self._thread_class == "1B":
            pitch_tolerance = 1.9500 * truncate(pitch_tolerance, 6)
        elif self._thread_class == "2B":
            pitch_tolerance = 1.3000 * truncate(pitch_tolerance, 6)
        elif self._thread_class == "3B":
            pitch_tolerance == 0.9750 * truncate(pitch_tolerance, 6)
        return round(pitch_tolerance, 4) 
    
