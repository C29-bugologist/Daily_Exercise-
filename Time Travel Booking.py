class TimeTravelTrip:
  """
  A class representing a time travel trip with destination year, description, and travelers.
  """
  def __init__(self, destination_year, description):
    self.destination_year = destination_year
    self.description = description
    self.travelers = []

  def add_traveler(self, traveler_name):
    """
    Adds a new traveler to the trip.
    """
    self.travelers.append(traveler_name)

  def remove_traveler(self, traveler_name):
    """
    Removes a traveler from the trip (if they exist).
    """
    if traveler_name in self.travelers:
      self.travelers.remove(traveler_name)

  def get_trip_details(self):
    """
    Prints the trip details including destination year, description, and travelers.
    """
    print(f"Destination Year: {self.destination_year}")
    print(f"Description: {self.description}")
    if not self.travelers:
      print("No travelers booked yet.")
    else:
      print("Travelers:")
      for traveler in self.travelers:
        print(f"- {traveler}")

def find_most_popular_trip(trips):
  """
  Finds the trip with the most travelers from a list.
  """
  most_popular = None
  max_travelers = 0
  for trip in trips:
    if len(trip.travelers) > max_travelers:
      most_popular = trip
      max_travelers = len(trip.travelers)
  return most_popular

# Example usage
trip1 = TimeTravelTrip(2077, "Explore Neo-Tokyo")
trip1.add_traveler("Alice")
trip1.add_traveler("Bob")

trip2 = TimeTravelTrip(1993, "Witness the fall of the Berlin Wall")
trip2.add_traveler("Charlie")

trips = [trip1, trip2]

most_popular_trip = find_most_popular_trip(trips)
print("The most popular trip:")
most_popular_trip.get_trip_details()
    