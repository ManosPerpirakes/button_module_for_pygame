class Button(rect.Rect):
    def __init__(self, text, window, x = 100, y = 100, width = 500, height = 50, colour = (255, 255, 255)):
        super().__init__(x, y, width, height)
        self.colour = colour
        self.window = window
        self.text = font.Font(None, height).render(text, True, (0, 0, 0))
    def show(self):
        draw.rect(self.window, self.colour, self)
        self.window.blit(self.text, (self.x, self.y))
    def click(self, function):
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos
        try:
            if self.collidepoint(x, y):
                function()
        except:
            pass