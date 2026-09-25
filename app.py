import streamlit as st
import matplotlib.pyplot as plt
from astar import astar

st.title("Smart Traffic Navigation System")
st.write("Find the shortest route using A* Search Algorithm")

grid = [
    [0,0,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,1,0,0]
]

st.subheader("City Map")
st.write(grid)

st.subheader("Select Start and Destination")

start_x = st.number_input("Start Row", 0, len(grid)-1, 0)
start_y = st.number_input("Start Column", 0, len(grid[0])-1, 0)

goal_x = st.number_input("Goal Row", 0, len(grid)-1, len(grid)-1)
goal_y = st.number_input("Goal Column", 0, len(grid[0])-1, len(grid[0])-1)

start = (start_x, start_y)
goal = (goal_x, goal_y)

if st.button("Find Shortest Path"):

    path = astar(grid, start, goal)

    st.write("Shortest Path:", path)

    fig, ax = plt.subplots()

    ax.imshow(grid, cmap="gray_r")

    x = [p[1] for p in path]
    y = [p[0] for p in path]

    ax.plot(x, y, marker="o", color="red")

    ax.scatter(start[1], start[0], color="green", s=100)
    ax.scatter(goal[1], goal[0], color="blue", s=100)

    st.pyplot(fig)
