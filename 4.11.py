friend_pizzas = ["Cheese Pizza", "Chicken Pizza", "Pepperoni Pizza"]
pizza_name = ["Cheese Pizza", "Chicken Pizza", "Pepperoni Pizza"]
pizza_name.insert(0, "Veggie Pizza")
friend_pizzas.insert(0, "Pineapple Pizza")
print(pizza_name)
print(friend_pizzas)
message = "My favorite pizzas are "
friend = "My friend's favorite pizzas are "
for pizza in pizza_name:
    print(message + pizza)
for food in friend_pizzas:
    print(friend + food)
