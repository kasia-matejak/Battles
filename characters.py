import random
import math

# klasy postaci zawierają atrybuty pozycji postaci
class Character:
    def __init__(
        self, name, fighting_technique, damage, position_x, position_y, life=100
    ):
        self.name = name
        self.fighting_technique = fighting_technique
        self.damage = damage
        self.life = life
        self.position_x = position_x
        self.position_y = position_y

    # metoda zawierania obrażeń
    def get_damage(self, damage):
        self.life = self.life - damage

    # metoda walki - zawiera w sobie zadawanie obrażeń
    def fight(self, opponent):
        print(self.name + self.fighting_technique)
        opponent.get_damage(self.damage)

    # metoda kalkulowania dystansu pomiędzy przeciwnikami
    def calculate_distance(self, opponent):
        distance = math.sqrt(
            (self.position_x - opponent.position_x) ** 2
            + (self.position_y - opponent.position_y) ** 2
        )
        return distance

    # metoda ataku - zawiera w sobie walkę i tym samym zadawanie obrażeń oraz kalkulację dystansu
    def attack(self, opponent):
        if self.calculate_distance(opponent) < 100:
            self.fight(opponent)
            print(opponent.name, "has ", opponent.life, " life left")
        else:
            print("Za daleko!")

    # metoda sprawdzania czy postać ma jeszcze punkty życia
    def check_if_alive(self):
        if self.life > 0:
            return True
        else:
            return False

    # def check_if_on_board(self, position):
    # if position >0 and position <500:
    # print("You can't go there")

    # metody poruszania się
    def move_up(self):
        self.position_y -= 1

    def move_down(self):
        self.position_y += 1

    def move_right(self):
        self.position_x += 1

    def move_left(self):
        self.position_x -= 1


# klasa dzieciczącą z postaci - czarodziej
# czarodziej zadaje zawsze obrażenia, ale nieduże
class Wizzard(Character):
    def __init__(self):
        super().__init__(
            name="Wizzard",
            fighting_technique=" casted a spell",
            damage=10,
            position_x=220,
            position_y=1,
        )


# klasa dzieciczącą z postaci - rycerz
# rycerz zadaje znaczne obrażenia albo nie zadaje wcale (czarodziej blokuje go zaklęciem)
class Knight(Character):
    def __init__(self):
        super().__init__(
            name="Knight",
            fighting_technique=" stabbed with a sword",
            damage=20,
            position_x=220,
            position_y=450,
        )

    def fight(self, opponent):
        print("Knight makes an attempt")
        x = random.randint(0, 1)
        if x == 1:
            super().fight(opponent)
        else:
            print("Wizzard used protection spell")
