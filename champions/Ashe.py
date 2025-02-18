from champion_base import Champion
class Ashe(Champion):
    def __init__(self):
        super().__init__("Ashe", " Cung Băng ")
        
    def cast_skill_q(self):
        q = 'Băng tiễn'
        return q

    def cast_skill_w(self):
        w = 'Chú tâm tiễn'
        return w

    def cast_skill_r(self):
        self.skill = 'Tán xạ tiễn'
        return r

    def cast_skill_e(self):
        e = 'Ưng tiễn'
        return e