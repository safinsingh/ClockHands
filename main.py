from math import * # Import math library for rounding function
import datetime # Import datetime for second to HH:MM:SS conversion

times = [] # Create empty array for verified degree measures
degSec = [] # Create empty array for verified timestamps

for i in range(0,43200): # I iterated through each second of the 12 hours displayed on the clock
    hrPos = floor(i/120) # The hour hand moves 1/120th of a degree of a second
    minPos = floor((i/10) % 360) # The minute hand moves 1/10th of a degree every second
    if hrPos == minPos: # If the rounded degree measures are the same,
        if hrPos not in times: # And if this isn't a duplicate,
            times.append(hrPos) # Add this to the verified degrees list!

for i in times[:11]: # For degree measure in array (EDIT: caps at 11 to avoid overlap due to rounding),
    secForm = (i/360)*43200 # Turn the degree measures into seconds passed after 00:00:00
    timeFormat = str(datetime.timedelta(seconds=secForm)) # Turn the seconds into HH:MM:SS format
    degSec.append(timeFormat) # Append the timings to the correct array

print(degSec) # Finally, print the array!
