# button_module_for_pygame
this module contains one class; Button()

Button(self, text, window, x = 100, y = 100, width = 500, height = 50, colour = (255, 255, 255))
it creates a button, given the aforementioned characteristics

this class has the following methods: show(self) and click(self, function)

show(self): it displays the button on the window

click(self, function): it checks whether the button has been clicked
NOTE: it has to be entered this way in order to work:
  for i in event.get():
    self.click(function)
