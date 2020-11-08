import math

CYCLE_DURATION = 1.5 # hours per sleep cycle
MIN_CYCLES = 4 # minimum number of sleep cycles
MAX_CYCLES = 8 # maximum number of sleep cycles
TIME_TO_BED = 0.25 # hours between bedtime and asleep
TIME_TO_BED_STR = "{:02d}:{:02d}".format(int(math.floor(TIME_TO_BED)), int(TIME_TO_BED%1 * 60))


def calculateWaketimes(bedtime):
    bedtime = float(bedtime)
    times = list()
    for sleep_cycle_num in range(MIN_CYCLES, MAX_CYCLES):
        times.append(prettifyTime(TIME_TO_BED+bedtime + sleep_cycle_num*CYCLE_DURATION))
    return times

def calculateBedtimes(waketime):
    waketime = float(waketime)
    times = list()
    for sleep_cycle_num in range(MAX_CYCLES, MIN_CYCLES, -1): #loop backwards
        times.append(prettifyTime(waketime - TIME_TO_BED - sleep_cycle_num*CYCLE_DURATION))
    return times

def prettifyTime(hour):
    twelve_hour_time = hour % 12
    return "{:02d}:{:02d}{}".format(int(math.floor(twelve_hour_time)), int(twelve_hour_time%1 * 60), 'am' if (hour <= twelve_hour_time) else 'pm')

if __name__ == '__main__':
    menu = 0 # placeholder, must not be 9.
    while True:
        try:
            menu = input("---MENU---\n0: give bedtime, get waketime.\n1: give waketime, get bedtime.\n9: quit\n")
        except SyntaxError: #most likely EOF
            print ("No selection. Please select one of the menu items by entering its number.")
            continue #skip to next iteration
        except NameError: #most likely alphabet input
            print ("Invalid selection. Please select one of the menu items by entering its *number*.") #note different message **
            continue #skip to next iteration
        if menu == 0:
            bedtime = input("When are you going to bed? \n")
            results = calculateWaketimes(bedtime)
            print ("If you go to bed at {} and it takes you {} to get to sleep, you should wake up at".format(prettifyTime(bedtime), TIME_TO_BED_STR), ", or ".join(results) + ".")
        elif menu == 1:
            waketime = input("When would you like to wake up? \n")
            results = calculateBedtimes(waketime)
            print ("If you want to wake up at {} and it takes you {} to get to sleep, you should go to bed at".format(prettifyTime(waketime), TIME_TO_BED_STR), ", or ".join(results) + ".")
        elif menu == 9:
            print ("Quitting.")
            break #quit
        else:
            print ("Invalid selection. Please select one of the menu items by entering its number.")
            continue #skip to next iteration
