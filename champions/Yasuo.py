from champion_base import Champion
class Yasuo(Champion): # Void kế thừa từ Champion
    def __init__(self):
        super().__init__("Yasuo", "Say Bye")

    def cast_skill_q(self):
        Q = 'Stell Tempest'
        return Q
    def cast_skill_w(self):
        W = 'Wind Wall'
        return W
    def cast_skill_r(self):
        return self.skill
    def cast_skill_e(self):
        E = 'Sweeping Blade'
        return E