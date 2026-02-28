# 🐢 Turtle Crossing Game
A vibrant, multi-lane crossing game built with Python's Turtle library. Navigate your turtle across a busy road filled with randomized traffic to reach the safety of the green zone!

## 🎮 How to Play
1. Run `main.py`.
2. Use the **Up Arrow** key to move the turtle.
3. Reach the top green safe zone to level up.
4. Avoid the cars! The game ends if you are hit.

## 🛠️ Project Structure
* `main.py`: The main game loop and collision logic.
* `player.py`: Controls the turtle's movement and starting position.
* `car_manager.py`: Manages randomized car spawning and lane logic.
* `roads.py`: Draws the gray asphalt, lane dividers, and green safe zones.
* `scoreboard.py`: Tracks your score and displays "Game Over."
* `assets/cars/`: Contains the .gif sprites used for the car shapes.

## ⚙️ Custom Features
- **Lane Logic**: Cars are snapped to specific horizontal lanes to prevent messy overlapping.
- **Smart Collision**: Uses a custom "box" hitbox to account for the rectangular shape of the car sprites.
- **Anti-Overlap Spawning**: Includes a "dead zone" check to ensure cars don't spawn on top of each other in the same lane.


------------------------------------------------------------------------------------------⚙️ Customization Guide-------------------------------------------------------------------------------------------------------------------
If you want to modify the game's difficulty or appearance, here are the key variables you can change:

1. Changing Screen Size
To change the dimensions of the game window, look at the top of main.py:

Python

# In main.py
screen.setup(width=800, height=800) # Increase or decrease these values
Note: If you change the screen size, you will also need to update the ROAD_START_Y and ROAD_END_Y in road_env.py and the LANES in car_manager.py to ensure the road still covers the visible area.

2. Adjusting Traffic Density
If the game is too easy or too hard, you can change how frequently cars spawn in car_manager.py:

Python

# In car_manager.py, inside create_cars()
if random.randint(1, 6) == 1: # Lower the 6 to make it harder, raise it to make it easier
3. Changing Level Difficulty
To change how much the speed increases each time you level up:

Python

# In car_manager.py
MOVE_INCREMENT = 3 # Increase this for a much steeper difficulty curve
4. Modifying the Road Layout
You can add or remove lanes by editing the LANES list in car_manager.py. Just ensure they are spaced consistently (e.g., 50 pixels apart) to match the road_env.py divider logic:

Python

# In car_manager.py
LANES = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
5. Adding New Car Assets
To add more car varieties:

Place a new .gif file in assets/cars/.

Add the filename to the CAR_IMAGES list in car_manager.py.

Register the new shape in main.py using screen.register_shape().

🛠️ Requirements
Python 3.x

Standard Turtle Library (Included with Python)

Assets: Rotated .gif files located in the assets/cars/ directory.
