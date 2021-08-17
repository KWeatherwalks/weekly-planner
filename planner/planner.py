import math

import cairo

# Set Dimensions (in μm)
WIDTH, HEIGHT = 2870, 1950

# create a SVG surface to draw on
with cairo.SVGSurface("example.svg", WIDTH, HEIGHT) as surface:
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)  # Normalize the canvas

    # Day Sections
    ctx.move_to(0, 0)  # Move pencil
    ctx.line_to(1, 1)

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(0.001)
    ctx.stroke()

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(50)

    ctx.set_font_size(50)
    ctx.move_to(30, 50)
    ctx.show_text("Hello")

    # Goals Sections
