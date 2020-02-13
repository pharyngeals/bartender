# bartender

# takes input of ingredients, then cross-references them from a dictionary
# of drinks

# drinks is a dictionary, each string key is paired to a list value
# of ingredients
# drinks = {"drink1": ['ing1', 'ing 2', 'ing3'], "drink2": ['ing1', 'ing2']}

# fix_my_drink function takes input (up to five(?) ingredients and then returns
# possibles drinks that can be make with it)

# so like, make the entire app (why not flask it lmao)
# a function called bartend()
# it says something like "i'm ur neighborhood friendly bartender
# what'll you have? LIST UP TO FIVE INGREDIENTS"
# then it checks for a drink that has those ingredients
# (all five? at least three?) and returns the drink with the ingredients
# each drink could maybe also have a recipe?? idk that sounds kinda...

# drink is a dictionary of dictionaries?? bc each drink should have
# ingredients and also maybe brief mixing instructions???

# input = give me an ingredient and returns a list of possible drinks
# from there you can either 1) pick a drink from the list or 2) add
# another ingredient to further narrow it down

# get_drink(ingredient):
# ingredient = input("give me an ingredient and i'll tell you what to make: ")

def get_drink(ingredient):
    for drink in drinks:
        if ingredient in drink
        return drink
    else:
        print("Sorry, I can't think of any drinks that use
              {}".format(ingredient))
