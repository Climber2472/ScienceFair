#Program for Science Fair

import copy
import math
import random

##Patterns
patterns = {
    1: "Standard grid",
    2: "Concentric circles",
    3: "Stagger grid",
    4: "Hexegonal"
}
##Number of Trials Per pattern
NUM_TRIAL = 25
### row spacing - optimal is 30 inches convert to cm
### plant spacing - optimal is 4 inches convert to cm
ROW_SPACING = 30 / 0.39370
PLANT_SPACING = 4 / 0.39370
SQ_YARD_IN_ACRE = 4840
###assuming a square we take the sqare root to get linear yards
YARDS_IN_ACRE = math.sqrt(SQ_YARD_IN_ACRE)
FEET_IN_ACRE = 3.0*YARDS_IN_ACRE
METERS_IN_ACRE = FEET_IN_ACRE*0.3048
CM_IN_ACRE = METERS_IN_ACRE*100
TOTAL_AREA_OF_FIELD = CM_IN_ACRE * CM_IN_ACRE
CENTER_OF_FIELD = 0.5*CM_IN_ACRE

### pattern 2 constants

TWO_PI_RADIANS = 2.0*math.pi

### pattern 3 - parabolas
PY_Y_INTERCEPT = (CENTER_OF_FIELD**2/CM_IN_ACRE)
print (PY_Y_INTERCEPT)

### pattern 4 - stagger
P4_Y_ROW_SPACING = math.sqrt(ROW_SPACING**2 - (PLANT_SPACING/2)**2)

DEATH_PERCENT_LOW = 0
DEATH_PERCENT_HIGH = 15
###Percent percent of totalfield  area to determine area of circle
###then calulate radius. Random placement of weed within box of worst case so no
###circle is clipped on the edge of the field

MAX_AREA_OF_IMPACT = (DEATH_PERCENT_HIGH/100.0)*TOTAL_AREA_OF_FIELD
MAX_OFFSET = math.sqrt(MAX_AREA_OF_IMPACT/math.pi)

### corn calories
CALORIES_PER_ACRE = 15000000 ### from https://www.scientificamerican.com/article/time-to-rethink-corn/

CALORIES_PER_PLANT = CALORIES_PER_ACRE / 52668 ### from standard layout TODO calculate this

def plant_in_field(p):
    if p ['x'] < 0.0:
        return False
    elif p ['y'] < 0.0:
        return False
    elif p ['x'] > CM_IN_ACRE:
        return False
    elif p ['y'] > CM_IN_ACRE:
        return False
    else:
        return True

def createLayout1():
    plants = []
    x = 0.0
    y = 0.0
    while y < CM_IN_ACRE:
        while x < CM_IN_ACRE:
            p = {'x': x, 'y': y, 'dead': False}
            plants.append(p)
            x = x + PLANT_SPACING
        x = 0
        y = y + ROW_SPACING


    return plants

def createLayout2():
    plants = []
    ### place first plant in center of field
    cx = 0.5*CM_IN_ACRE
    cy = 0.5*CM_IN_ACRE
    p = {'x': cx, 'y': cy, 'dead': False}
    plants.append(p)

    theta = 0.0 ### angle in radians as we move around the circle
    ring_number = 1 ### first ring

    plant_placed = True ### to force start of loop
    while plant_placed:
        plant_placed = False ### start loop not having any plants placed
        theta_increment = PLANT_SPACING / (ring_number * ROW_SPACING)
        while theta < TWO_PI_RADIANS:
            x = ring_number * ROW_SPACING * math.cos(theta)
            y = ring_number * ROW_SPACING * math.sin(theta)
            theta = theta + theta_increment
            if theta < TWO_PI_RADIANS: ### if next placement doesn't overlap the ring, place
                p = {'x': cx + x, 'y': cy + y, 'dead': False}
                if plant_in_field(p):
                    plants.append(p)
                    plant_placed = True

        theta = 0.0
        ring_number = ring_number + 1

    return plants

### stagger grid
def createLayout3():
    plants = []
    x = 0.0
    y = 0.0
    staggered = False
    while y < CM_IN_ACRE:
        single_row = []
        while x < CM_IN_ACRE:
            p = {'x': x, 'y': y, 'dead': False}
            single_row.append(p)
            x = x + PLANT_SPACING
        if staggered:
            x = 0.0
            staggered = False
        else:
            x = PLANT_SPACING/2.0
            staggered = True
        y = y + P4_Y_ROW_SPACING
        plants.extend(single_row)


    return plants

### theta1 x must be less that theta2 x for this work
def placeHexRow (cx, cy, apothem, theta1, theta2):
    ### place row of plants as long as on field
    plants = []
    x1 = round(cx + apothem * math.cos(theta1), 10)
    y1 = round(cy + -1.0 * apothem * math.sin(theta1), 10) ### flip y so in proper direction
    x2 = round(cx + apothem * math.cos(theta2), 10)
    y2 = round(cy + -1.0 * apothem * math.sin(theta2), 10) ### talk about rounding error in expplaination
    theta = math.asin((y2-y1) / apothem) ### angle of the row relative to center point
    x = x1
    y = y1
    p = {'x': x, 'y': y, 'dead': False}
    if plant_in_field(p):
        plants.append(p)
    delta_x = PLANT_SPACING * math.cos(theta)
    delta_y = PLANT_SPACING * math.sin(theta)
    while x < x2 - delta_x:
        x = x + delta_x
        y = y + delta_y
        p = {'x': x, 'y': y, 'dead': False}
        if plant_in_field(p):
            plants.append(p)



    return plants



def createLayout4():
    plants = []

    apothem = ROW_SPACING/math.sqrt(3)
    cx = 0.0
    cy = 0.0
    staggered = False
    while cy <= (CM_IN_ACRE + 0.5 * ROW_SPACING):
        while cx <= (CM_IN_ACRE + apothem):
            ### lay plants on 3 sides
            plants.extend(placeHexRow(cx, cy, apothem, math.pi*2.0/3.0, math.pi/3.0))
            plants.extend(placeHexRow(cx, cy, apothem, math.pi, math.pi*4.0/3.0))
            plants.extend(placeHexRow(cx, cy, apothem, math.pi*5.0/3.0, 0.0))

            cx = cx + 2.0 * apothem

        if staggered:
            cx = 0.0
            staggered = False
        else:
            cx = 1.5 * apothem
            staggered = True
        cy = cy + 0.5 * ROW_SPACING





    return plants

def createLayout(pattern):
    switcher = {
        1: createLayout1,
        2: createLayout2,
        3: createLayout3,
        4: createLayout4,
    }
    f = switcher.get(pattern)
    if f == None:
        raise(ValueError("Invalid Layout Specified. Please Pick 1-5"))

     ### Call the specified function
    return f()

def placeRandomWeed():
    ### Randomly pick the center of the weed circle
    x = random.uniform(CENTER_OF_FIELD-MAX_OFFSET,CENTER_OF_FIELD+MAX_OFFSET)
    y = random.uniform(CENTER_OF_FIELD-MAX_OFFSET,CENTER_OF_FIELD+MAX_OFFSET)
    w = {"x": x, "y": y}
    ### Now caluclate radius based on random death percent
    d = random.uniform(DEATH_PERCENT_LOW, DEATH_PERCENT_HIGH)
    w["death_rate"] = d
    area_effecteed = 0.01*d*TOTAL_AREA_OF_FIELD
    radius = math.sqrt(area_effecteed/math.pi)
    w["r"] = radius
    return w

### helper function to detmine if given plant is in sphere of weed influence
def weedTouchPlant(weed, plant):
    dist = math.sqrt((weed["x"] - plant["x"]) ** 2 + (weed["y"] - plant["y"]) ** 2)
    return dist <= weed["r"]


### given a layout and a weed, change dead flag to true on plants affected
def killPlants(layout, weed):
    for plant in layout:
        if weedTouchPlant(weed, plant):
            plant["dead"] = True
    return layout


## Start Main Program
## Ask user for pattern to use
print("Choose a Pattern - ")
for i in patterns:
    print("%d: %s" % (i, patterns[i]))
desired_pattern = int(input("Choose a Pattern number - "))

### lay out the plants
master_layout = createLayout(desired_pattern)
number_of_plants = len(master_layout)
print("Number of plants placed: %d" % (number_of_plants))


### loop NUM_TRIALS
results = []
for t in range(NUM_TRIAL):
    print("Starting trial %d..." % (t+1))
    result = {}
    result ["number_of_plants"] = number_of_plants
    result ["possible_calories"] = CALORIES_PER_PLANT*number_of_plants

    ### make copy of layout
    layout = copy.deepcopy(master_layout)

    ### randomly pick the disease weed and radius of impact
    weed = placeRandomWeed()
    print("Weed located at - %s" % (str(weed)))
    result["weed"] = weed

    ### apply death rate
    final_layout = killPlants(layout, weed)
    ### result["layout"] = final_layout

    ### save trial results
    number_dead_plants = len(list(filter(lambda p: p["dead"], final_layout)))
    result["number_dead_plants"] = number_dead_plants
    result["number_live_plants"] = number_of_plants - number_dead_plants
    result["actual_calories"] = CALORIES_PER_PLANT*result["number_live_plants"]
    result["yield"] = result["actual_calories"]/result["possible_calories"]*100.0 ### Convert to percent
    print("Number of dead plants: %d" % (number_dead_plants))
    print("Calories per Acre: %d" % (result["actual_calories"]))
    print("Yield: %f" % (result["yield"]))

    ### Save this result in results
    results.append(result)
    print("Trial %d complete" % (t+1))

### end loop

### Average results of trials
sum = 0
for result in results:
    sum += result["actual_calories"]
average = sum / NUM_TRIAL
print("Average is %d" % (average))
### print the results
print("\n\n\n Results Follow - Put in Excel... \n\n\n")
i = 1
print("trial_no, number_live_plants, number_dead_plants, number_of_plants, death_rate, calories, yield")
for result in results:
    print("%d, %d, %d, %d, %f, %d, %f" % (i, result["number_live_plants"],
                                         result["number_dead_plants"],
                                         result["number_of_plants"],
                                         result["weed"]["death_rate"],
                                         result["actual_calories"],
                                         result["yield"]))
    i = i + 1