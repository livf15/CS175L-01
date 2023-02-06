#CS175L
#Olivia Franczykowski
#Restaurant

    
repeat='yes'
vegetarian=False
vegan=False
gluten_free=False
while repeat == 'yes':
    answer1=input("Is anyone in your party a vegetarian?: ")
    if answer1=='yes':
        vegetarian=True
    answer2=input("Is anyone in your party a vegan?: ")
    if answer2=='yes':
        vegan=True
    answer3=input("Is anyone in your party gluten-free?: ")
    if answer3=='yes':
        gluten_free=True
    print(gluten_free)
    print("Here are your restaurant choices: ")
    if vegetarian == False and vegan == False and gluten_free == False:
        print("   Joe's Gourment Burgers")
    if vegetarian == True and vegan == False and gluten_free == True:
        print("   Main Street Pizza Company")
    if vegetarian == True and vegan == False and gluten_free == True:
        print("   Corner cafe")
    if vegetarian == True and vegan == False and gluten_free ==False:
        print("   Mama's Fine Italian")
    if vegetarian == True and vegan == False and gluten_free == True:
        print("   The Chef's Kitchen")
    repeat=(input('Do you want to search for more restaraunts?' ))

            

    


