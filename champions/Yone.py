from champion_base import Champion
class Yone(Champion):
    def __init__(self):
        super().__init__("Yone", "Dao kiem sanh tu")

    def cast_skill_q(self):
        q = 'switcheroo'
        return q
    def cast_skill_w(self):
        w = 'ZAP !'
        return w
    def cast_skill_e(self):
        e = 'flame chompers !'
        return e
    def cast_skill_r(self):
        r = 'super mega death'
        return r