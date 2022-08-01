import os

import cairo

from .examples import draw, my_example

FILENAME = "test"
PDF_PATH = "/planner/output"


def create_pdf():

    # Set Dimensions (in μm)
    SCALE_FACTOR = 1
    WIDTH, HEIGHT = 287 * SCALE_FACTOR, 195 * SCALE_FACTOR  # 2870, 1950

    file_path = f"{PDF_PATH}/{FILENAME}.pdf"
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w+") as f:
        # create a PDF surface to draw on
        with cairo.PDFSurface(file_path, WIDTH, HEIGHT) as surface:

            ctx = cairo.Context(surface)
            # ctx.scale(WIDTH, HEIGHT)  # Normalize the canvas

            my_example(ctx)
            # draw(ctx)

            surface.finish()
