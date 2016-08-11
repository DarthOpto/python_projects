# Magic 8 Ball
# Demonstrate the use of lists


import random


messages = ['It is certain',
            'It is decidedly so',
            'Yes, Definitely',
            'Reply hazy, try again',
            'Ask again later',
            'Concentrate, then ask again',
            'My reply is No',
            'Outlook not so good',
            'Very Doubtful']

print(messages[random.randint(0, len(messages) - 1)])
