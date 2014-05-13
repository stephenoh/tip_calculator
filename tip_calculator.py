meal = 20.00
tax_value = 0.15 * meal
meal_with_tax = meal + tax_value
tip_value = 0.15 * meal_with_tax 
total = meal_with_tax + tip_value


print ("The base cost of your meal was $%.2f") % (meal)
print ("You need to pay $%.2f for tax") % (tax_value)
print ("Tipping at a rate of %s, you should leave $%.2f for a tip") % ("15%", tip_value)
print ("The grand total of your meal is $%.2f.") % (total)