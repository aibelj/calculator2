#Random class
#random methods
import random

class Random:

    def random_num_noSeed():
        #Generates a random number without a seed between a range of two numbers - Integer
        random_int = random.randrange(1, 11, 1)

        # Generates a random number without a seed between a range of two numbers - Decimal rounded to the hundredth place
        random_flt = round(random.uniform(1, 11),2)

        return (random_int, random_flt)

    def random_num_seed():
        #Generate a random number with a seed between a range of two numbers - Integer
        random.seed (5)
        random_int = random.randint(1, 11, 1)

        # Generate a random number with a seed between a range of two numbers - Decimal
        random.seed (5)
        random_flt =  round(random.uniform(1,11), 2)