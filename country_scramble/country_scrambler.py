from random import randrange
from country_scramble.country_getter import get_country


class CountryScrambler:

    @staticmethod
    def scrambled_country():
        """
        Scramble the country
        :return: the scramble country
        """
        jumbled = ""
        country_scrambled = ""
        country = get_country()

        while country:
            position = randrange(len(country))
            jumbled += country[position]
            country_scrambled = country[:position] + country[(position + 1):]
        return country_scrambled