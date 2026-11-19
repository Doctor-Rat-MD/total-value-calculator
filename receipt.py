milk = 2
shoes =3
soap = 2
cheese = 4
apples = 1
garbage_bags = 15
cereal = 3
carrots = 7
toilet_paper = 8
laundry_detergent = 10

groceries_list = {
    "milk": 2,
    "shoes": 3,
    "soap":2,
    "cheese":4,
    "apples":1,
    "garbage bags":15,
    "cereal":3,
    "carrots":7,
    "toilet paper":8,
    "laundry detergent": 10,
    }
# this dictionary might be useless if we aren't allowed to use zip

choices = 9
picked = 1

groceries = ["milk","shoes","cheese","apples","garbage bags","cereal","carrots","toliet paper","laundry detergent"]

purchased = int(input("How many " + groceries[0] + " to buy?"))

values = []
counter = 1
values.append(purchased)

while picked < choices:
    purchase = int(input("How many " + groceries[counter] + " to buy?"))
    picked += 1
    counter += 1
    values.append(purchase)

# we gotta find another workaround instead of this giant ass maths statement
maths = str((milk * values[0])+(shoes * values[1])+(cheese * values[2])+(apples * values[3])+(garbage_bags * values[4])+(cereal * values[5])+(carrots * values[6])+(toilet_paper*values[7])+(laundry_detergent*values[8]))
print("Your total price before tax is $" + maths + ".")
