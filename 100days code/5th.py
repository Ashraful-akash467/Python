import curses
import random
import time

# Screen dimensions
SCREEN_HEIGHT = 26
SCREEN_WIDTH = 90
WIN_WIDTH = 70

# Initialize car shape
car = [
    " A A ",
    "AAAAA",
    " A A ",
    "AAAAA"
]

def draw_border(win):
    for i in range(SCREEN_HEIGHT):
        win.addstr(i, 0, "±")
        win.addstr(i, WIN_WIDTH, "±")
    win.refresh()

def draw_car(win, car_pos):
    for i, row in enumerate(car):
        win.addstr(SCREEN_HEIGHT - 5 + i, car_pos, row)

def erase_car(win, car_pos):
    for i in range(4):
        win.addstr(SCREEN_HEIGHT - 5 + i, car_pos, " " * len(car[0]))

def draw_enemy(win, enemy_x, enemy_y):
    enemy_shape = [
        "****",
        " ** ",
        "****",
        " ** "
    ]
    for i, row in enumerate(enemy_shape):
        win.addstr(enemy_y + i, enemy_x, row)

def erase_enemy(win, enemy_x, enemy_y):
    for i in range(4):
        win.addstr(enemy_y + i, enemy_x, " " * 4)

def collision(car_pos, enemy_x, enemy_y):
    if SCREEN_HEIGHT - 6 <= enemy_y + 3:
        if car_pos < enemy_x + 4 and car_pos + len(car[0]) > enemy_x:
            return True
    return False

def game_over(win):
    win.clear()
    win.addstr(SCREEN_HEIGHT // 2, WIN_WIDTH // 2 - 10, "GAME OVER!")
    win.addstr(SCREEN_HEIGHT // 2 + 1, WIN_WIDTH // 2 - 18, "Press any key to return to the menu.")
    win.refresh()
    win.getch()

def instructions(win):
    win.clear()
    win.addstr(5, 10, "Instructions")
    win.addstr(6, 10, "--------------------")
    win.addstr(7, 10, "Avoid cars by moving left or right.")
    win.addstr(8, 10, "Press 'a' to move left.")
    win.addstr(9, 10, "Press 'd' to move right.")
    win.addstr(10, 10, "Press 'ESC' to quit.")
    win.addstr(12, 10, "Press any key to go back to the menu.")
    win.refresh()
    win.getch()

def play(win):
    car_pos = WIN_WIDTH // 2
    enemy_y = [1, 1]
    enemy_x = [random.randint(17, WIN_WIDTH - 21), random.randint(17, WIN_WIDTH - 21)]
    enemy_flag = [1, 0]
    score = 0

    win.clear()
    draw_border(win)

    while True:
        win.timeout(50)
        key = win.getch()

        if key == ord('a') and car_pos > 18:
            erase_car(win, car_pos)
            car_pos -= 4
        elif key == ord('d') and car_pos < WIN_WIDTH - len(car[0]):
            erase_car(win, car_pos)
            car_pos += 4
        elif key == 27:  # ESC key
            break

        draw_car(win, car_pos)

        for i in range(2):
            if enemy_flag[i]:
                erase_enemy(win, enemy_x[i], enemy_y[i])
                enemy_y[i] += 1
                if enemy_y[i] > SCREEN_HEIGHT - 4:
                    enemy_y[i] = 1
                    enemy_x[i] = random.randint(17, WIN_WIDTH - 21)
                    score += 1
                draw_enemy(win, enemy_x[i], enemy_y[i])

        if collision(car_pos, enemy_x[0], enemy_y[0]) or collision(car_pos, enemy_x[1], enemy_y[1]):
            game_over(win)
            break

        win.addstr(2, WIN_WIDTH + 7, f"Score: {score}")
        win.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    while True:
        stdscr.clear()
        stdscr.addstr(5, 10, "----------------------------------")
        stdscr.addstr(6, 10, "|            Car Game            |")
        stdscr.addstr(7, 10, "----------------------------------")
        stdscr.addstr(9, 10, "1. Start Game")
        stdscr.addstr(10, 10, "2. Instructions")
        stdscr.addstr(11, 10, "3. Quit")
        stdscr.addstr(13, 10, "Select Option:")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            play(stdscr)
        elif key == ord('2'):
            instructions(stdscr)
        elif key == ord('3'):
            break

curses.wrapper(main)
