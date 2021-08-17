import cairo 
import os 

FILENAME = "example"
PDF_PATH = os.getcwd()


def create_txt():
    print('---- in create_txt() ----')
    print('Current directory: ', os.getcwd())
    with open(f"{FILENAME}.txt", "w+") as f:
        f.write("Adding new line")
    print(f'---- {FILENAME}.txt CREATED! ----')

def create_pdf():

    # Set Dimensions (in μm)
    WIDTH, HEIGHT = 2870, 1950
    print("---- In create_pdf() ----")
    print("Current working directory: ", os.getcwd())
    with open(FILENAME+'.pdf', "w+") as f:
        # create a SVG surface to draw on
        with cairo.PDFSurface(FILENAME+'.pdf', WIDTH, HEIGHT) as surface:
            ctx = cairo.Context(surface)

            ctx.scale(WIDTH, HEIGHT)  # Normalize the canvas

            # Day Sections
            ctx.move_to(0, 0)  # Move pencil
            ctx.line_to(1, 1)

            ctx.set_source_rgb(0, 0, 0)
            ctx.set_line_width(0.001)
            ctx.stroke()

            ctx.select_font_face(
                "Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL
            )
            ctx.set_font_size(50)

            ctx.set_font_size(50)
            ctx.move_to(30, 50)
            ctx.show_text("Hello")

            # Goals Sections

            surface.finish()
    print('---- PDF CREATED! ----')
