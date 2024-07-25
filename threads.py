from math import floor

def truncate(f, n):
  return floor(f * 10 ** n) / 10 ** n

class Threads():
  def __init__(self, basic_diameter, thread_pitch, thread_class, thread_designation=None):
    self.units = True # True if imperial, False is metric
    self._basic_diameter = basic_diameter
    self._thread_pitch = thread_pitch
    self._thread_class = thread_class
    self._thread_designation = thread_designation
    self._height = 0.86603 * (1 / self._thread_pitch)

def __repr__(self):
  if self.unit:
    return f"{self._basic_diameter:.3f}-{self._thread_pitch} {self._thread_designation}-{self._thread_class}"
  return f"M{self._basic_diameter} x {self._thread_pitch} - {self._thread_class}"

def get_basic_dimensions(self):
  basic_pitch = self._basic_diameter - (2 * (0.375 * self._height))
  basic_minor = self._basic_diameter - (2 * (0.625 * self._height))
  # Accounting for UNR threads
  if self._thread_class.endswith("A") and "R" in self._thread_designation:
    basic_minor -= (.108 * (1 / self._thread_pitch))
  return truncate(basic_minor, 4), truncate(basic_pitch, 4)
  
def calculate_major_diameter_tolerance(self):
  if self._thread_class.endswith("A"):
    if self._thread_class.startswith("1"):
      return 0.0900 * (self._thread_pitch ** (2/3))
    if self._thread_class.startswith("2") or self._thread_class.startswith("3"):
      return 0.0600 * (self._thread_pitch ** (2/3))
    raise ValueError("Invalid Thread Class")
  if self._thread_class.endswith("B"):
    return 0.14433757 + self.calculate_pitch_diameter_tolerance()
  raise ValueError("Invalid Thread Class")

def calculate_minor_diameter_tolerance(self):
    if self._thread_class.endswith("A"):
      if "R" in self._thread_designation:
          return self.calculate_pitch_diameter_tolerance() + (0.10825318 * self._thread_pitch)
      return self.calculate_pitch_diameter_tolerance() + (0.21650635 * self._thread_pitch)
    if self._thread_class.endswith("B"):
      if self._thread_class.startswith("1") or self._thread_class.startswith("2"):
        if self._basic_diameter < 0.250:
          minor_dia_tolerance_max = 0.39400 * self._thread_pitch
          minor_dia_tolerance_min = (0.2500 * self._thread_pitch) - (0.400 * (self._thread_pitch ** 2))
          minor_dia_tolerance_actual = ((0.0500 * (self._thread_pitch ** (2/3))) + 0.030 - (self._thread_pitch / self._basic_diameter)) - 0.002
          if minor_dia_tolerance_actual > minor_dia_tolerance_max:
            return minor_dia_tolerance_max
          if minor_dia_tolerance_actual < minor_dia_tolerance_min:
            return minor_dia_tolerance_min
          return minor_dia_tolerance_actual
        if self._basic_diameter >= 0.250:
          if (self._thread_pitch / 1) <= 80 and (self._thread_pitch / 1) >= 4:
            return (0.2500 * self._thread_pitch) - (0.400 * (self._thread_pitch ** 2))
          if (self._thread_pitch / 1) < 4:
            return 0.1500 * self._thread_pitch
      if self._thread_class.startswith("3"):
        minor_dia_tolerance_max = 0.39400 * self._thread_pitch
        if (self._thread_pitch / 1) <= 80 and (self._thread_pitch / 1) >= 13:
          minor_dia_tolerance_min = (0.2300 * self._thread_pitch) - (1.500 * (self._thread_pitch ** 2))
        elif (self._thread_pitch / 1) < 13:
          minor_dia_tolerance_min = (.1200 * self._thread_pitch) 
        minor_dia_tolerance_actual = ((0.0500 * (self._thread_pitch ** (2/3))) + (0.030(self._thread_pitch / self._basic_diameter))) - 0.002
        if minor_dia_tolerance_actual > minor_dia_tolerance_max:
          return minor_dia_tolerance_max
        if minor_dia_tolerance_actual < minor_dia_tolerance_min:
          return minor_dia_tolerance_min
        return minor_dia_tolerance_actual

  def calculate_pitch_diameter_tolerance(self):
    if self._thread_class.endswith("A"):
      if self._thread_class.startswith("1"):
        return 1.5000 * self._Td2_2A
      if self._thread_class.startswith("2"):
        return self._Td2_2A
      if self._thread_class.startswith("3"):
        return 0.7500 * self._Td2_2A
      raise ValueError("Invalide Thread Class")
    if self._thread_class.endswith("B"):
      if self._thread_class.startswith("1"):
        return 1.9500 * self._Td2_2A
      if self._thread_class.startswith("2"):
        return 1.3000 * self._Td2_2A
      if self._thread_class.startswith("3"):
        return 0.9750 * self._Td2_2A
        raise ValueError("Invalid Thread Class")
    raise ValueError("Invalid Thread Class")
