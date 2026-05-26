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