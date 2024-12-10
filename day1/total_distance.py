import logging

# configure the logging level
logging.basicConfig(level=logging.INFO)

# open the puzzle input file
f = open('./puzzle_input')

# store left location IDs in a list
leftList = []
# store right location IDs in a list
rightList = []

# parse the puzzle input
while(True):
    line = f.readline()

    # EOF, break out of loop
    if line == '':
        break

    # remove whitespace from ends of the line
    line = line.strip()
    # split the line on 3 spaces
    values = line.split('   ')
    # convert location IDs from strings to integers
    left = int(values[0])
    right = int(values[1])
    # store location IDs in respective lists
    leftList.append(left)
    rightList.append(right)

# sort the lists to compare smallest to smallest, second smallest to second
# smallest, etc.
leftList.sort()
rightList.sort()

totalDistance = 0

# loop through the lists to compare values
for index, left in enumerate(leftList):
    right = rightList[index]
    # distance is difference between left and right list values
    totalDistance += abs(left - right)

logging.info(f'Total distance: {totalDistance}')
