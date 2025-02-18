from champion_base import Champion
class Jhin(Champion): # Jhin kế thừa từ Champion
    def __init__(self):
        super().__init__("Jhin", "Dark Matter")
    def cast_skill_q(self):
        q = 'Lời thì thầm'
        return q
    def cast_skill_w(self):
        w = 'Lựu đạn nhảy múa'
        return w
    def cast_skill_e(self):
        e = 'Nét vẽ chết chóc'
        return e
    def cast_skill_r(self):
        r = 'Cạm bẫy nghệ thuật'
        return r