class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    if item in self.items:
      self.items.remove(item)
    else:
      print(f"{item} not found in player inventory")

  def update_score(self, points):
    self.score += points

  def display_info(self):
    print(f"\nPlayer Name: {self.name}")
    print(f"Score: {self.score}")
    if self.items:
      print(f"Items: {', '.join(self.items)}")
    else:
      print("No items found.")

def find_highest_score_player(players):
  highest_score = 0
  highest_score_player = None
  for player in players:
    if player.score > highest_score:
      highest_score = player.score
      highest_score_player = player
  return highest_score_player

def main():
  players = []

  while True:
    print("\nVR Game - Player Management")
    print("1. Add Player")
    print("2. Manage Player")
    print("3. Find Highest Score Player")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      player_name = input("Enter player name: ")
      players.append(Player(player_name))
      print(f"Player {player_name} added successfully!")

    elif choice == 2:
      if not players:
        print("No players found. Please add players first.")
        continue

      print("\nSelect Player:")
      for i, player in enumerate(players):
        print(f"{i+1}. {player.name}")

      player_choice = int(input("Enter player number: ")) - 1

      if player_choice < 0 or player_choice >= len(players):
        print("Invalid player choice. Please try again.")
        continue

      player = players[player_choice]

      while True:
        print("\nPlayer Management -", player.name)
        print("1. View Info")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Score")
        print("5. Back")

        player_choice = input("Enter your choice: ")

        if player_choice == "1":
          player.display_info()

        elif player_choice == "2":
          item_to_add = input("Enter item name: ")
          player.add_item(item_to_add)
          print(f"Item '{item_to_add}' added to {player.name}'s inventory.")

        elif player_choice == "3":
          item_to_remove = input("Enter item name to remove: ")
          player.remove_item(item_to_remove)

        elif player_choice == "4":
          score_update = int(input("Enter score update (integer): "))
          player.update_score(score_update)
          print(f"{player.name}'s score updated!")

        elif player_choice == "5":
          break

        else:
          print("Invalid choice. Please try again.")

    elif choice == 3:
      if not players:
        print("No players found. Please add players first.")
        continue

      highest_scorer = find_highest_score_player(players)
      if highest_scorer:
        highest_scorer.display_info()
        print(f"{highest_scorer.name} has the highest score!")
      else:
        print("No players found.")

    elif choice == 4:
      print("Exiting VR Game...")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
