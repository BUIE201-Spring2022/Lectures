class House:
    def __init__(self):
        self._cat = Cat()
        self._mouse = Mouse()
        self._animals = []
        self._animals.append(self._cat)
        self._animals.append(self._mouse)

    def Play(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self._slow_down()
                    elif event.key == pygame.K_UP:
                        self._speed_up()

            self.TimeTick()

            self._clock.tick()


    def TimeTick(self):
        for animal in self._animals:
            animal.Move()
        b = self._cat.CheckIfYouCaught(self._mouse)
        if b:
            self._mouse.Die()
        



class Animal:
    def __init__(self):
        self._x = 0
        self._y = 0

    def Move():
        pass


class Mouse(Animal):
    def __init__(self):
         pass

    def Die(self):
        pass

    def AreYouThere(self, x, y):
        return self._x == x and self._y == y


class Cat(Animal):
    def __init__(self):
         pass
    
    def CheckIfYouCaught(self, mouse : Mouse):
        mouse.AreYouThere(self._x, self._y)


h = House()
h.Play()
