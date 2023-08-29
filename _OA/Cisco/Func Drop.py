def funcDrop(xCoordinate, yCoordinate):
    xCount = {}
    yCount = {}
    uniquePoints = set()

    for i in range(len(xCoordinate)):
        xCount[xCoordinate[i]] = xCount.get(xCoordinate[i], 0) + 1
        yCount[yCoordinate[i]] = yCount.get(yCoordinate[i], 0) + 1
        uniquePoints.add(str(xCoordinate[i]) + "," + str(yCoordinate[i]))

    maxDrops = max(max(xCount.values()), max(yCount.values()))

    # Check if the maxDrops count doesn't exceed the unique points
    if maxDrops > len(uniquePoints):
        maxDrops = len(uniquePoints)

    print(maxDrops)

def funcDrop2(xCoordinates, yCoordinates):
    coordinate_pairs = set(zip(xCoordinates, yCoordinates))
    first_element_counts = {}
    second_element_counts = {}

    for pair in coordinate_pairs:
        first_element, second_element = pair
        first_element_counts[first_element] = first_element_counts.get(first_element, 0) + 1
        second_element_counts[second_element] = second_element_counts.get(second_element, 0) + 1

    max_first_element = max(first_element_counts.values())
    max_second_element = max(second_element_counts.values())

    return max(max_first_element,max_second_element)

xCoordinates = [2, 2, 2, 4, 2]
yCoordinates = [2, 2, 6, 5, 8]
funcDrop2(xCoordinates, yCoordinates)
