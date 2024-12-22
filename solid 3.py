class Bird:
    def fly(self):
        return "Flying!"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying!"


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich can't fly.")


def let_bird_fly(bird):
    try:
        print(bird.fly())
    except NotImplementedError as e:
        print(e)


# استخدام الكلاسات
sparrow = Sparrow()
let_bird_fly(sparrow)

ostrich = Ostrich()
let_bird_fly(ostrich)
