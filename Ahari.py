from abc import ABC, abstractmethod

class Champion(ABC):
    def __init__(self, name, skill):
        self.__name = name
        self.__skill = skill

    def attack(self):
        print(self.__name, 'thi triển', self.__skill)

    @abstractmethod
    def cast_skill_q(self):
        pass

    @abstractmethod
    def cast_skill_w(self):
        pass

    @abstractmethod
    def cast_skill_e(self):
        pass

    @abstractmethod
    def cast_skill_r(self):
        pass

    def get_name(self):
        return self.__name


class Ahri(Champion):
    def __init__(self):
        super().__init__("Ahri", "Quả cầu ma thuật")

    def cast_skill_q(self):
        print(f"{self.get_name()} sử dụng Quả cầu ma thuật (Q)")

    def cast_skill_w(self):
        print(f"{self.get_name()} sử dụng Lửa hồ ly (W)")

    def cast_skill_e(self):
        print(f"{self.get_name()} sử dụng Hôn gió (E)")

    def cast_skill_r(self):
        print(f"{self.get_name()} sử dụng Phi hồ (R)")


class ChampionMenu:
    def __init__(self, champion):
        self.champion = champion

    def show_menu(self):
        while True:
            print("\nChọn kỹ năng để sử dụng:")
            print("1. Kỹ năng Q")
            print("2. Kỹ năng W")
            print("3. Kỹ năng E")
            print("4. Kỹ năng R")
            print("5. Thoát")
            choice = input("Nhập lựa chọn: ")

            if choice == '1':
                self.champion.cast_skill_q()
            elif choice == '2':
                self.champion.cast_skill_w()
            elif choice == '3':
                self.champion.cast_skill_e()
            elif choice == '4':
                self.champion.cast_skill_r()
            elif choice == '5':
                print("Thoát khỏi menu.")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")


# Test thử class Ahri và ChampionMenu
ahri = Ahri()
menu = ChampionMenu(ahri)
menu.show_menu()
