from datetime import time
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + ' menu availible from ' + str(self.start_time) + ' to ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    tot =0
    for each in purchased_items:
      if each in self.items:
        tot += self.items[each]
    return tot

class Franchise:
  def __init__(self, address, menus):
    self.menus = menus
    self.address = address

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    av_menus = []
    for each in self.menus:
      if each.start_time <= time and time <= each.end_time:
        av_menus.append(each)
    return av_menus

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('brunch', brunch_items, 1100, 1600)

eary_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('early_bird', eary_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('kids', kids_items, 1100, 2100)


arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a’ Arepa', arepa_items, 1000, 2000)
#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

all_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", all_menus)

new_installment = Franchise("12 East Mulberry Street", all_menus)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
#print(franchise1.available_menus(1200))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

franchises = [flagship_store, new_installment, arepas_place]

first_business = Business("Basta Fazoolin' with my Heart",franchises)

arepa = Business("Take a' Arepa", [arepas_place] )

print(arepa.franchises[0].menus[0])







  





