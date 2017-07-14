def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have {} cheeses!".format(cheese_count))
    print("you have {} boxes of crackers!".format(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
