'''

The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
Unless it is summer, then the upper limit is 100 instead of 90.
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
'''

def squirrel_play(temp, is_summer):
    playing = False
#check if the temp is summer
    if temp > 90 and temp <=100 and is_summer== True:
    # return True
        playing = True
#if not, check if temperature is between 60 and 90
    elif temp <= 90 and temp >= 60:
        playing = True
#else return False
    return playing

print(squirrel_play(95, True))