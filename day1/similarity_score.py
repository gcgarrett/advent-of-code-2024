import logging

# configure the logging level
logging.basicConfig(level=logging.INFO)

# open the puzzle input file
f = open('./puzzle_input')

# store left location IDs in a list
leftList = []
# store right location IDs in a map of location ID to how many times it
# occurs in the input list
rightMap = {}

# helper method to make a location ID as seen
#
# parameters
#   locationId (int): The location ID to mark as seen
def seen(locationId):
    # get the current seen count for the location ID, defaulting to 0
    count = rightMap.get(locationId, 0)
    # increment and store back into the map
    rightMap[locationId] = count + 1

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
    # append left location IDs into list
    leftList.append(left)
    # mark right location ID as seen
    seen(right)

similarityScore = 0

# loop through the left list
for left in leftList:
    # get the count of how many times that location ID appeared in the right
    # list
    rightCount = rightMap.get(left, 0)
    # similarity score is the sum of each left list number multiplied by the
    # number of times it appears in the right list
    similarityScore += (left * rightCount)

logging.info(f'Similarity Score: {similarityScore}')
