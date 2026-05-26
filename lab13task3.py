class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print (f"имя ресторана: {self.restaurant_name} ")
        print (f"тип кухни: {self.cuisine_type}")
        print (f"рейтинг: {self.rating}")
    def open_restaurant(self):
        print ("ресторан открыт")
    def up_rating(self, new_rating):
        self.rating=new_rating
        print (f"новый рейтинг: {self.rating} ")
               
newRestaurant = Restaurant("pizza","итальянская кухня")
print (newRestaurant.restaurant_name)
print (newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

newRestaurant.up_rating(5)
newRestaurant.describe_restaurant()