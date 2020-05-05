"""Generates funny names by randomly combining names
from three separate lists"""

import sys
import random


def main():
    """Choose names at random from three tuples of name and print to screen"""
    print("Welcome to the Psych 'Sidekick' name picker \n")
    print("A name just like Sean would pick for Gus: \n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill",
             "Bob", 'Bowel Noises', 'Boxelder', "Bud",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston", 'Worms')

    middle = ('Beenie-Weenie', 'Stinkbug', 'Lite', 'Clawhammer', 'Pottin Soil',
              '"Lunch Money"', 'The Squirts', 'Jazz Hands', 'Ashle', 'Joly',
              'Lott', 'Darlen', 'Mercedes', 'Fiat', 'Oxmaul', 'Issmall',
              'Moon', 'Tad', 'Clare', 'Husein', 'Tinkie-Winkie',
              'Twinkle Toes', 'Strike Force')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette',
            'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey',
            'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        # Generate a random number to make it so that middle name only is
        # used some of the time
        middle_yes = random.randint(0, 1)

        first_name = random.choice(first)
        last_name = random.choice(last)

        if middle_yes:
            middle_name = random.choice(middle)
            print('\n\n')
            print(f"{first_name} {middle_name} {last_name}", file=sys.stderr)
            print('\n\n')
        else:
            print('\n\n')
            print(f"{first_name} {last_name}", file=sys.stderr)
            print('\n\n')

        try_again = input('\n\nTry again? (Press ENTER else n to quit)\n')
        if try_again.lower() == "n":
            break

        input('\nPress ENTER to exit')


if __name__ == '__main__':
    main()
