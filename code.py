#Program for Science Fair

import copy
import math
import random

##Patterns
patterns = {
    1: "Standard grid",
    2: "Concentric circles",
    3: "Parabolas",
    4: "Stagger grid",
    5: "Hexegonal"
}
##Number of Trials Per pattern
NUM_TRIAL = 25
###plant spaceing - optimal is 30 inches convert to cm
PLANT_SPACING = 30 / 0.39370
SQ_YARD_IN_ACRE = 4840
###assuming a square we take the sqare root to get linear yards
YARDS_IN_ACRE = math.sqrt(SQ_YARD_IN_ACRE)
FEET_IN_ACRE = 3.0*YARDS_IN_ACRE
METERS_IN_ACRE = FEET_IN_ACRE*0.3048
CM_IN_ACRE = METERS_IN_ACRE*100
TOTAL_AREA_OF_FIELD = CM_IN_ACRE * CM_IN_ACRE
CENTER_OF_FIELD = 0.5*CM_IN_ACRE


DEATH_PERCENT_LOW = 1
DEATH_PERCENT_HIGH = 15
###Percent percent of totalfield  area to determine area of circle
###then calulate radius. Random placement of weed within box of worst case so no 
###circle is clipped on the edge of the field

MAX_AREA_OF_IMPACT = (DEATH_PERCENT_HIGH/100.0)*TOTAL_AREA_OF_FIELD
MAX_OFFSET = math.sqrt(MAX_AREA_OF_IMPACT/math.pi)
print(CENTER_OF_FIELD+MAX_OFFSET)
print(CENTER_OF_FIELD-MAX_OFFSET)

def placeRandomWeed():
    ### Randomly pick the center of the weed circle
    x = random.uniform(CENTER_OF_FIELD-MAX_OFFSET,CENTER_OF_FIELD+MAX_OFFSET)
    y = random.uniform(CENTER_OF_FIELD-MAX_OFFSET,CENTER_OF_FIELD+MAX_OFFSET)
    w = {"x": x, "y": y}
    ### Now caluclate radius based on random death percent
    d = random.uniform(DEATH_PERCENT_LOW, DEATH_PERCENT_HIGH)
    area_effecteed = 0.01*d*TOTAL_AREA_OF_FIELD
    radius = math.sqrt(area_effecteed/math.pi)
    w["r"] = radius
    return w

def createLayout(pattern):
    plants = []
    x = 0.0
    y = 0.0
    while y < CM_IN_ACRE:
        while x < CM_IN_ACRE:
            p = {'x': x, 'y': y, 'dead': False}
            plants.append(p)
            x = x + PLANT_SPACING
        x = 0
        y = y + PLANT_SPACING


    return plants

## Start Main Program
    placeRandomWeed()

print("Choose a Pattern - ")
for i in patterns:
    print("%d: %s" % (i, patterns[i]))

desired_pattern = int(input("Choose a Pattern number - "))

##Choose Trials


### lay out the plants

master_layout = createLayout(desired_pattern)
print("Number of plants placed: %d" % (len(master_layout)))

### loop NUM_TRIALS

for t in range(NUM_TRIAL):
    print("Starting trial %d..." % (t+1))

    ### make copy of layout
    trail_run_layout = copy.deepcopy(master_layout)

    weed = placeRandomWeed()
    print("Weed - %s" % (str(weed)))
    ### apply death rate
    ### save trial results

    print("Trial %d complete" % (t+1))

### end loop
### calculate the fianl results individual trials
### print the results
