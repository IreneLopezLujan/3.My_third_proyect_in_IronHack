import src.funciones_main as fm
import requests
import json
import pandas as pd
import argparse




def validaFood(food):
    correct_items = ['Beef', 'Lamb', 'BBQ', 'Hamburger or Sausage', 'Chicken','Pasta','Lobster',
       'Salmon']
    correct_items_long={'Pasta':'Pasta with Tomato Sauce',
       'Lighter Fish':'Fresh Water or Lighter Fish (trout, sole, etc.)',
       'Shellfish':'Shellfish (clams, mussels, scallops, oysters, etc.)',
       'Soft Cheeses':'Soft, Creamy Cheeses with washed rind (brie, camembert, etc.)',
       'Goat Cheeses':"Goat's Cheese",
       'Hard, Aged Cheeses':'Hard, Aged Cheeses (cheddar, aged gouda, manchego, etc.)',
        'Feathered Game':'Feathered Game (guinea fowl, pheasant, squab, etc.)'}
    if food in correct_items:
        return  correct_items_long[food]
    elif food in correct_items_long:
        return correct_items_long[food]
    else:
        error = 'Inserte un producto válido, como por ejemplo'+str(correct_items)
        raise argparse.ArgumentTypeError(error)


def validaColor(color):
    correct_items = ['White wine', 'Sweet wine', 'Red wine', 'Fortified wine',
       'Rosé wine', 'Sin definir', 'Orange wine', 'Vermouth']
    if color in correct_items:
        return color
    else:
        error = 'Inserte un producto válido, como por ejemplo'+str(correct_items)
        raise argparse.ArgumentTypeError(error)

   
        
def parser():
    
    parser = argparse.ArgumentParser(description="Hello, This is your wine recommendation App. Introduce a color wine and dish you will eat  and we will recommend you the best wine to taste :)")
    parser.add_argument("-c",dest="Colors", help="Please, insert a color wine",type=str)
    parser.add_argument("-d",dest="dishes", help="Please, insert a dish", type=str)
    parser.add_argument("-t",dest="city", help="Please, insert your city situation ", type=str)
    args = parser.parse_args()
    return args

def main():

    args = parser()
    colors = args.Colors
    dishes = args.dishes
    city=args.city
    print (args)
    x = fm.filter_dataset(colors, dishes)
    if x.empty:
        print("No wine recommendation for this selection, please introduce another option")
    else:
        print(x)
    y =fm.search(city)
    if y.empty:
        print("No wine store recommendation for this city, please introduce another city")
    else:
        print(y)
    
        
    if __name__ == "__main__":
            main()
