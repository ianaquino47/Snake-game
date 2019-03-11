import random
import curses

screen  = curses.initscr()  # using curses to initialise the screen
curses.curs_set(0)  # set cursor to 0 so it doesn't show up on the screen
screenHeight, screenWidth = screen.getmaxyx()  # get height and width
window = curses.newwin(screenHeight, screenWidth, 0, 0)  # start at top left hand corner of screen
window.keypad(1)
window.timeout(100)  # refresh screen every 100ms

snk_x = screenWidth / 4
snk_y = screenHeight / 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

food = [screenHeight / 2, screenWidth / 2]
window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screenHeight] or snake[0][1] in [0, screenWidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, screenHeight - 1),
                random.randint(1, screenWidth - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
#go to terminal
#cd to right directory
#type "python snakegame.py"
