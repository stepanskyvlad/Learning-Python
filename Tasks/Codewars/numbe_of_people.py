def number(bus_stops):
    return sum(x-y for x, y in bus_stops)


print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
