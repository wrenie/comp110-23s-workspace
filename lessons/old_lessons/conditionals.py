"""if it's running tell me to pack an umbrella"""

weather: str = input("Hey Siri what's the weather like?")

if (weather == "rain"):
    print("Pack your umbrella!!")
    print("but splash in the puddles!")
else:
    if (weather == "snow"):
        print("Pack a jacket, silly goose!")
    print("No need for the 'brella")
print("Have a good day sunshine")