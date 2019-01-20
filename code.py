#Program for Science Fair

import math

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
YARDS_IN_ACRE = math.sqrt(SQ_YARD_IN_ACRE)
FEET_IN_ACRE = 3.0*YARDS_IN_ACRE
METERS_IN_ACRE = FEET_IN_ACRE*0.3048
CM_IN_ACRE = METERS_IN_ACRE*100

###assuming a square we take the sqare root to get linear yards

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
    ### apply death rate
    ### save trial results

    print("Trial %d complete" % (t+1))

### end loop
### calculate the fianl results individual trials
### print the results
