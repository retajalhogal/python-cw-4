def my_name():
    print("my name is retaj")

my_name()

def my_meal(food,drink):
    print(f"i like to eat {food} and while drinking {drink}")

my_meal("chcolota" , "water")

def cube(number):
    return(number**3)

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

print(by_three(5))