from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Pokemon type", ["Electric", "Water", "Fire", "Grass"])
print(table)