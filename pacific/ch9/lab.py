
def main():
 

    notGreenCost = [0] * 12
    goneGreenCost = [0] * 12
    savings = [0] * 12
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    getNotGreen(notGreenCost, months)
    getGoneGreen(goneGreenCost, months)
    energySaved(notGreenCost, goneGreenCost, savings)
    displayInfo(notGreenCost, goneGreenCost, savings, months)

def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:
        print months[counter]
        notGreenCost[counter] = input("Enter NOT GREEN cost: ")
        counter = counter + 1
    return notGreenCost

def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 12:
        print months[counter]
        goneGreenCost[counter] = input("Enter GONE GREEN cost: ")
        counter = counter + 1
    return goneGreenCost

def energySaved(notGreenCost, goneGreenCost, savings):
    counter=0
    while counter < 12:
        savings[counter] = notGreenCost[counter]- goneGreenCost[counter]
        counter = counter + 1
    return savings

def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < 12:
        print "Information for: ", months[counter]
        print "Savings is $ ", savings[counter]
        print "Not green cost is $ ", notGreenCost[counter]
        print "Gone green cost is $ ", goneGreenCost[counter]
        counter = counter + 1

main()