class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print (f"имя ресторана: {self.restaurant_name} ")
        print (f"тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print ("ресторан открыт")

newRestaurant = Restaurant("lalala","японская кухня")
print (newRestaurant.restaurant_name)
print (newRestaurant.cuisine_type)


newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

newRestaurant1 = Restaurant("баня","русская кухня")
print (newRestaurant1.restaurant_name)
print (newRestaurant1.cuisine_type)


newRestaurant1.describe_restaurant()
newRestaurant1.open_restaurant()

newRestaurant2 = Restaurant("маргарита", "итальянская кухня")
print (newRestaurant2.restaurant_name)
print (newRestaurant2.cuisine_type)

newRestaurant2.describe_restaurant()
newRestaurant2.open_restaurant()

newRestaurant3 = Restaurant("пупупу","китайская кухня")
print (newRestaurant3.restaurant_name)
print (newRestaurant3.cuisine_type)


newRestaurant3.describe_restaurant()
newRestaurant3.open_restaurant()