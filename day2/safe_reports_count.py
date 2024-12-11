import logging

# configure the logging level
logging.basicConfig(level=logging.INFO)

# open the puzzle input file
f = open('./puzzle_input')

# number of safe reports
safeCount = 0

def isSafe(levels):
    # initalize level increasing/decreasing to None so we can set it on the
    # first comparison between levels
    # if True then levels are increasing, if False then levels are decreasing
    increasing = None

    # iterate through the levels except the last one, since we will compare
    # that level to the second-to-last level
    for i in range(len(levels) - 1):
        j = i + 1
        # get the two adjacent levels to compare
        iLevel = levels[i]
        jLevel = levels[j]
        # calculate their difference
        diff = jLevel - iLevel

        # if the difference is 0 then the report is unsafe
        if diff == 0:
            return False

        # set if levels are increasing/decreasing if not already set
        if increasing is None:
            if diff > 0:
                increasing = True
            else:
                increasing = False

        # if the difference between the levels increases but previous levels
        # were decreasing then the report is unsafe
        if diff > 0 and not increasing:
            return False
        # if the difference between the levels decreases but previous levels
        # were increasing then the report is unsafe
        elif diff < 0 and increasing:
            return False
        
        # get the absolute value of the difference to determine if difference
        # is within the safe range
        diff = abs(diff)

        # if the change in levels is outside of the safe range the report is
        # unsafe
        if diff < 1 or diff > 3:
            return False

    # if the loop completes the report is safe
    return True

# parse the puzzle input
while(True):
    line = f.readline()

    # EOF, break out of loop
    if line == '':
        break

    # remove whitespace from ends of the line
    line = line.strip()
    # split the line on 1 space
    levelStrs = line.split(' ')
    # convert strings to integers
    levels = [int(i) for i in levelStrs]

    # if the report is safe then increase the count of safe reports
    if isSafe(levels):
        safeCount += 1

logging.info(f'Safe reports: {safeCount}')
