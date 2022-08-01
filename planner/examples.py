import datetime as dt
from math import pi as PI

import cairo
import numpy as np


# Helper function
def day_of_month(d):
    """
    d: Datetime object
    """

    def suffix(d):
        return "th" if 10 < d < 14 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")

    def custom_strftime(format, t):
        return t.strftime(format).replace("{S}", str(t.day) + suffix(t.day))

    return custom_strftime("{S}", d)


def my_example(cr):

    # weekly info
    year = "2022"
    month = "July"
    week_of = dt.datetime(2022, 7, 25)
    days_of_month = [day_of_month(week_of + dt.timedelta(days=d)) for d in range(6)]

    # Colors
    GRAY = (0.3, 0.3, 0.3, 1)
    BLACK = (0, 0, 0, 1)
    LIGHTGRAY = (0.5, 0.5, 0.5, 1)

    # Shape Parameters
    GRID_HEIGHT, GRID_WIDTH = 4, 4
    DOT_RADIUS = 0.2

    # Data Parameters
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    HOURS = [
        " 8:00",
        " 9:00",
        "10:00",
        "11:00",
        "12:00",
        " 1:00",
        " 2:00",
        " 3:00",
        " 4:00",
        " 5:00",
        " 6:00",
        " 7:00",
    ]
    DAYS_INIT = ["M", "T", "W", "H", "F", "S", "U"]

    # Anchor coordinates
    X, Y = 0, 0

    # Font Selection
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # Left Side
    cr.move_to(5 * GRID_WIDTH, 3 * GRID_HEIGHT)
    cr.set_font_size(9)
    cr.set_source_rgba(*BLACK)
    cr.show_text(month)
    cr.set_source_rgba(*GRAY)
    cr.show_text(" " + year)

    cr.set_font_size(3)
    cr.set_line_width(0.1)
    for line in range(42):
        x, y = X + GRID_WIDTH, Y + (5 + line) * GRID_HEIGHT

        if line % 14:
            # Day Lines
            cr.move_to(x, y)
            cr.set_source_rgba(*LIGHTGRAY)
            cr.rel_line_to(21 * GRID_WIDTH, 0)
            cr.stroke()

            # Goals
            for dot in range(12):
                cr.arc(x + (22 + dot) * GRID_WIDTH, y, DOT_RADIUS, 0, 2 * PI)
                cr.fill()
                cr.stroke()

        else:
            # Day
            cr.move_to((x + 1), y + 0.5 * GRID_HEIGHT)
            cr.set_source_rgba(*BLACK)
            cr.show_text(DAYS[line // 14] + f" {days_of_month[line//14]}")

            # Goals
            cr.move_to((x + 1) + 26 * GRID_WIDTH, y + 0.5 * GRID_HEIGHT)
            cr.set_source_rgba(*GRAY)
            cr.show_text("Goals")

    # Vertical Lines
    x, y = X + 8 * GRID_WIDTH, Y + 5 * GRID_HEIGHT
    cr.set_line_width(0.2)
    cr.select_font_face("Consolas", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    for _ in range(3):
        cr.move_to(x, y + GRID_HEIGHT / 2)
        cr.set_source_rgba(*GRAY)
        cr.rel_line_to(0, 12.5 * GRID_HEIGHT)
        cr.stroke()

        # Meeting Hours
        for hour in range(12):
            cr.move_to(x - 5, y + (hour + 1.45) * GRID_HEIGHT)
            cr.set_font_size(1.5)
            cr.set_source_rgba(*GRAY)
            cr.show_text(HOURS[hour])

        y += 14 * GRID_HEIGHT

    # Exercise boxes
    cr.set_line_width(0.17)
    x, y = X + 23 * GRID_WIDTH, Y + 15 * GRID_HEIGHT
    for _ in range(3):
        cr.move_to(x, y)
        cr.set_source_rgba(*BLACK)

        for i in np.arange(0, 6 * GRID_WIDTH, GRID_WIDTH):
            for j in np.arange(0, 3 * GRID_HEIGHT, GRID_HEIGHT):

                if not i:
                    cr.set_source_rgba(*LIGHTGRAY)
                    cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                    cr.fill()
                    cr.stroke()

                cr.set_source_rgba(*BLACK)
                cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                cr.stroke()

        y += 14 * GRID_HEIGHT

    # Right Side

    # Font Selection
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # Anchor coordinates
    X, Y = 34 * GRID_WIDTH + 1, 0

    # Days
    cr.set_font_size(3)
    cr.set_line_width(0.1)
    for line in range(42):
        x, y = X + GRID_WIDTH, Y + (5 + line) * GRID_HEIGHT

        if line % 14:
            # Day Lines
            cr.move_to(x, y)
            cr.set_source_rgba(*LIGHTGRAY)
            cr.rel_line_to(21 * GRID_WIDTH, 0)
            cr.stroke()

            # Goals
            for dot in range(12):
                cr.arc(x + (22 + dot) * GRID_WIDTH, y, DOT_RADIUS, 0, 2 * PI)
                cr.fill()
                cr.stroke()

        else:
            # Day
            cr.move_to((x + 1), y + 0.5 * GRID_HEIGHT)
            cr.set_source_rgba(*BLACK)
            cr.show_text(DAYS[3 + line // 14] + f" {days_of_month[3+line//14]}")

            # Goals
            cr.move_to((x + 1) + 26 * GRID_WIDTH, y + 0.5 * GRID_HEIGHT)
            cr.set_source_rgba(*GRAY)
            cr.show_text("Goals")

    # Vertical Lines
    x, y = X + 8 * GRID_WIDTH, Y + 5 * GRID_HEIGHT
    cr.set_line_width(0.2)
    cr.select_font_face("Consolas", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    for _ in range(3):
        cr.move_to(x, y + GRID_HEIGHT / 2)
        cr.set_source_rgba(*GRAY)
        cr.rel_line_to(0, 12.5 * GRID_HEIGHT)
        cr.stroke()

        # Meeting Hours
        for hour in range(12):
            cr.move_to(x - 5, y + (hour + 1.45) * GRID_HEIGHT)
            cr.set_font_size(1.5)
            cr.set_source_rgba(*GRAY)
            cr.show_text(HOURS[hour])

        y += 14 * GRID_HEIGHT

    # Exercise boxes
    cr.set_line_width(0.17)
    x, y = X + 23 * GRID_WIDTH, Y + 15 * GRID_HEIGHT

    for _ in range(2):
        cr.move_to(x, y)
        cr.set_source_rgba(*BLACK)

        for i in np.arange(0, 6 * GRID_WIDTH, GRID_WIDTH):
            for j in np.arange(0, 3 * GRID_HEIGHT, GRID_HEIGHT):

                if not i:
                    cr.set_source_rgba(*LIGHTGRAY)
                    cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                    cr.fill()
                    cr.stroke()

                cr.set_source_rgba(*BLACK)
                cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                cr.stroke()

        y += 14 * GRID_HEIGHT

    # Weekly Goals
    x, y = X + 23 * GRID_WIDTH, Y + 35 * GRID_HEIGHT

    # Job Searching
    for i in np.arange(0, 11 * GRID_WIDTH, GRID_WIDTH):
        for j in np.arange(0, 3 * GRID_HEIGHT, GRID_HEIGHT):

            if not i:
                cr.set_source_rgba(*LIGHTGRAY)
                cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                cr.fill()
                cr.stroke()

            cr.set_source_rgba(*BLACK)
            cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
            cr.stroke()

    # Daily Goals

    x, y = X + 23 * GRID_WIDTH, Y + 39 * GRID_HEIGHT
    # Font Selection
    cr.select_font_face("Courier New", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(3)

    for i in np.arange(0, 8 * GRID_WIDTH, GRID_WIDTH):
        # Hash marks separating goals
        cr.set_source_rgba(*BLACK)
        cr.move_to(x + i + GRID_WIDTH, y)
        cr.rel_line_to(0, -GRID_HEIGHT / 2)
        cr.stroke()

        for j in np.arange(0, 7 * GRID_HEIGHT, GRID_HEIGHT):

            # Identify first column
            if not i:
                # Shade box
                cr.set_source_rgba(*LIGHTGRAY)
                cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
                cr.fill()
                cr.stroke()

                # Daily initials
                text = DAYS_INIT[j // GRID_HEIGHT]
                cr.move_to(x + 1, y + j + GRID_HEIGHT - 1)
                cr.set_source_rgba(*BLACK)
                cr.show_text(text)

            cr.set_source_rgba(*BLACK)
            cr.rectangle(x + i, y + j, GRID_WIDTH, GRID_HEIGHT)
            cr.stroke()


def draw(cr):

    cr.set_line_width(0.04)

    utf8 = "cairo"

    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    cr.set_font_size(0.2)
    x_bearing, y_bearing, width, height, x_advance, y_advance = cr.text_extents(utf8)
    x = 0.5 - (width / 2 + x_bearing)
    y = 0.5 - (height / 2 + y_bearing)

    cr.move_to(x, y)
    cr.show_text(utf8)

    # draw helping lines
    cr.set_source_rgba(1, 0.2, 0.2, 0.6)
    cr.arc(x, y, 0.05, 0, 2 * PI)
    cr.fill()
    cr.move_to(0.5, 0)
    cr.rel_line_to(0, 1)
    cr.move_to(0, 0.5)
    cr.rel_line_to(1, 0)
    cr.stroke()
