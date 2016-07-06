# Coin Flipper
#
# Flips a coin 100 times and tells the user how many heads v. tails

from random import choice

coin = ["heads", "tails"]
flip_count = 0
heads_count = 0
tails_count = 0

while flip_count < 100:
    coin_choice = choice(coin)
    if coin_choice == "heads":
        heads_count += 1
    else:
        tails_count += 1
    flip_count += 1
print("After {} flips, the total number of Heads was: {}"
      .format(flip_count, heads_count))
print("After {} flips, the total number of Tails was: {}"
      .format(flip_count, tails_count))
