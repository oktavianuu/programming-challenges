# Scenario
"""
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes
(it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result 
has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
"""
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# find total all minutes 
mins = mins + dura
# find total hours
hour += mins // 60 
# correct minutes to tall in 0..59 range
mins %= 60
# correct hours to fall in 0..23 range
hour %= 24

print(hour, ":", mins, sep='')