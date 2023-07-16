class Button():
    def __init__(self, text, window, x = 100, y = 100, width = 500, height = 50, colour = (255, 255, 255)):
        self.rect = rect.Rect(x, y, width, height)
        self.colour = colour
        self.window = window
        self.text = font.Font(None, height).render(text, True, (0, 0, 0))
    def show(self):
        draw.rect(self.window, self.colour, self.rect)
        self.window.blit(self.text, (self.rect.x, self.rect.y))
    def click(self, function):
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos
        try:
            if self.rect.collidepoint(x, y):
                function()
        except:
            pass