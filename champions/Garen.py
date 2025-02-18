from champion_base import Champion
class Garen(Champion): # Garen kế thừa từ Champion
    def __init__(self):
        super().__init__("Garen", "Skill")

    def cast_skill_q(self):
        q = 'Đòn quyết định'
        return q

    def cast_skill_w(self):
        w = 'Lòng can đảm'
        return w

    def cast_skill_r(self):
        self.skill = 'Phán quyết'
        return r

    def cast_skill_e(self):
        e = 'Công Lý Demacia'
        return e