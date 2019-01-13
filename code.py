#Program for Science Fair

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
print (PLANT_SPACING)
def createLayout(pattern):
    print("layout pattern %d" % (pattern))
    return "hello"

print("Choose a Pattern - ")
for i in patterns:
    print("%d: %s" % (i, patterns[i]))

desired_pattern = input("Choose a Pattern number - ")

##Choose Trials


### lay out the plants

master_layout = createLayout(desired_pattern)

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

