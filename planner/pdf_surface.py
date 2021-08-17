import os

import cairo

FILE_NAME = os.path.basename(__file__)
WIDTH = 287
HEIGHT = 195

fp = open(f"./exports/{FILE_NAME[:-3]}.pdf", 'wb')
ps = cairo.PDFSurface(fp, WIDTH, HEIGHT)
cr = cairo.Context(ps)

cr.set_source_rgb(1, 0, 0)
cr.select_font_face(
    "Arial",
    cairo.FONT_SLANT_NORMAL,
    cairo.FONT_WEIGHT_NORMAL
)
cr.set_font_size(50)
cr.move_to(30, 50)
cr.show_text("Hello")

# cr.show_page()

ps.finish()
