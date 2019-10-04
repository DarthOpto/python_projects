"""
A Psych Sidekick Name Generator
"""
import sys
import random

FIRST = ('Baby Oil', 'Bad News', 'Big Burps', 'Bill "Beenie-Weenie"',
         'Bob "Stinkbug"', 'Bowel Noises', 'Boxelder',
         'Bud "Lite"', 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
         'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
         'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
         'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim',
         'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
         'Joe "Pottin Soil"', 'Johnny', 'Lemongrass', 'Lil Debil',
         'Longbranch', '"Lunch Money"', 'Mergatroid',
         'Mr. Peabody', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
         'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
         'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         'Snorki', 'Sid "The Squirts"', 'Skidmark',
         'Slaps', 'Snakes', 'Snoobs', 'Storyboard', 'Sweet Tea', 'TeeTee',
         'Wheezy Joe', 'Winston "Jazz Hands"',
         'Worms')

LAST = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
        'Clutterbuck', 'Cocktoastem', 'Endicott', 'Fewhairs',
        'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster',
        'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson',
        'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine',
        'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge',
        'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle',
        'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
        'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
        'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
        'Stroganoff', 'Sugar-Gold', 'Swackhammer', 'Tippins', 'Turnipseed',
        'Vinaigrette', 'Walkingstick', 'Wallbanger',
        'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
        'Winkerton', 'Woolysocks')


def main():
    """
    Generate a Psych pseudonym
    """
    print('Welcome to the Psych "Sidekick Name Generator" \n')
    while True:
        first_name = random.choice(FIRST)
        last_name = random.choice(LAST)

        print('A name just like Sean would pick for Gus: \n')
        print(f'{first_name} {last_name}', file=sys.stderr)
        print('\n\n')

        try_again = input('\n\nTry again? (Press ENTER else n to quit)\n')
        if try_again.lower() == 'n':
            break
    input('\nPress ENTER to exit')

if __name__ == "__main__":
    main()