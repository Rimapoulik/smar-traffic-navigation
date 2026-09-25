from src.astar import astar

def find_route(grid, start, goal):
    return astar(grid, start, goal)


grid = [
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0]
]

start = (0,0)
goal = (3,3)

path = find_route(grid, start, goal)

print("Shortest Path:", path)
