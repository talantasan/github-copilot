import random
import curses

# Initialize the screen
s = curses.initscr()
# Set cursor to 0 for visibility
curses.curs_set(0)
# Get the height and width of the window
sh, sw = s.getmaxyx()
# Create a new window using screen height and width
w = curses.newwin(sh, sw, 0, 0)
# Accept keypad input
w.keypad(1)
# Refresh screen every 100 milliseconds
w.timeout(100)

# Create the snake initial position
snk_x = sw//4
snk_y = sh//2
# Initial snake body parts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Food position
food = [sh//2, sw//2]
# Add the food to the screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Initial direction the snake moves towards
key = curses.KEY_RIGHT

# Infinite loop for game movement
while True:
    # Get the next key
    next_key = w.getch()
    # If no key is pressed then use the previous key
    key = key if next_key == -1 else next_key

    # Check if game over [snake runs over itself or hits border of screen]
    if snake[0][0] in [0, sh] or \
        snake[0][1]  in [0, sw] or \
        snake[0] in snake[1:]:
        # End the window
        curses.endwin()
        quit()

    # Determine the new head based on the direction
    new_head = [snake[0][0], snake[0][1]]

    # Update the head based on the direction
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head to the snake's body
    snake.insert(0, new_head)

    # If snake runs over the food
    if snake[0] == food:
        food = None
        while food is None:
            # Create new food
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            # If food is not part of snake body, place it on screen
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # If no food eaten, keep moving the snake
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Add the new head of the snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)