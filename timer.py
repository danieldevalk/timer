import time

def timer():
    fractions = 0.0
    seconds = 0
    minutes = 0
    hours = 0
    while hours < 100:
        minutes = 0
        while minutes <60:
            seconds = 0
            if minutes == 59:
                hours += 1
            while seconds < 60:
                fractions = 0.0
                if seconds == 59:
                    minutes += 1
                while fractions < 1.0:
                    f = format (fractions, '.2f')
                    fractions = float(f)
                    time.sleep(.1)
                    print(hours,':',minutes,':',seconds,'.',fractions)
                    fractions += 0.1
                    if fractions == 0.9:
                        seconds += 1
timer()
