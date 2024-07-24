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
