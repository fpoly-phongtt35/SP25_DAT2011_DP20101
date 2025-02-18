from champion_base import Champion
class Yone(Champion):
    def __init__(self):
        super().__init__("Yone", "Dao kiem sanh tu")

    def cast_skill_q(self):
        Q = 'switcheroo'
        return Q
    def cast_skill_w(self):
        W = 'ZAP !'
        return W
    def cast_skill_e(self):
        E = 'flame chompers !'
        return E
    def cast_skill_r(self):
        R = 'super mega death'
        return R