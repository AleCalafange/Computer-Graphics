import cairo
import cairosvg  

WIDTH, HEIGHT = 300, 300

#  imagem vetorial SVG
surface = cairo.SVGSurface("cgpi1.svg", WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Círculo azul
ctx.set_source_rgb(0, 0, 1)
ctx.arc(80, 80, 40, 0, 2 * 3.14)
ctx.fill()

# Triângulo verde
ctx.set_source_rgb(0, 1, 0)
ctx.move_to(180, 50)
ctx.line_to(230, 130)
ctx.line_to(130, 130)
ctx.close_path()
ctx.fill()

# Quadrado vermelho
ctx.set_source_rgb(1, 0, 0)
ctx.rectangle(100, 180, 60, 60)
ctx.fill()

surface.finish()

# Exportar para PNG
cairosvg.svg2png(url="cgpi1.svg", write_to="cgpi1.png")
