"""Functions to draw pdfs using the Cairo Python API"""
import os

import cairo

from .examples import my_example

FILENAME = "test"
PDF_PATH = "/planner/output"


def create_pdf(date):
    """
    Create PDF using Cairo drawing API
    date: dictionary
    e.g. {"year": 2022, "month": 3, "day": 27}
    """
    # Set Dimensions (in μm)
    scale_factor = 1
    width, height = 287 * scale_factor, 195 * scale_factor  # 2870, 1950

    file_path = f"{PDF_PATH}/{FILENAME}.pdf"
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w+", encoding="utf-8") as f:

        # create a PDF surface to draw on
        with cairo.PDFSurface(file_path, width, height) as surface:

            # Create cairo canvas to draw on
            ctx = cairo.Context(surface)

            # Draw my example
            my_example(ctx, **date)

            # Write to pdf
            surface.finish()
