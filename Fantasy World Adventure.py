class Creature:
  """
  A class representing a mythical creature with name, type, and abilities.
  """
  def __init__(self, name, creature_type):
    self.name = name
    self.type = creature_type
    self.abilities = []

  def add_ability(self, ability):
    """
    Adds a new ability to the creature's list.
    """
    self.abilities.append(ability)

  def remove_ability(self, ability):
    """
    Removes an ability from the creature's list (if it exists).
    """
    if ability in self.abilities:
      self.abilities.remove(ability)

  def display_abilities(self):
    """
    Prints all abilities of the creature.
    """
    if not self.abilities:
      print(f"{self.name} has no abilities yet.")
    else:
      print(f"{self.name} abilities:")
      for ability in self.abilities:
        print(f"- {ability}")

def find_most_powerful(creatures):
  """
  Finds the creature with the most abilities from a list.
  """
  most_powerful = None
  max_abilities = 0
  for creature in creatures:
    if len(creature.abilities) > max_abilities:
      most_powerful = creature
      max_abilities = len(creature.abilities)
  return most_powerful

# Example
creature1 = Creature("Smaug", "Dragon")
creature1.add_ability("Fire Breath")
creature1.add_ability("Flight")

creature2 = Creature("Sparkles", "Unicorn")
creature2.add_ability("Healing Touch")
creature2.add_ability("Teleportation")
creature2.add_ability("Horn Strike")

creatures = [creature1, creature2]

most_powerful_creature = find_most_powerful(creatures)
print(f"The most powerful creature is: {most_powerful_creature.name}")
most_powerful_creature.display_abilities()
