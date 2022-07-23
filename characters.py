import random

#tworzę klasę postaci
class Character:
    def __init__(self, name, attack, damage, life=100):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.life = life

#metoda zawierająca technikę walki postaci oraz zadawany damage
    def fight(self, opponent):
        print(self.name + self.attack)
        opponent.life = opponent.life - self.damage

#klasa dzieciczącą z postaci - czarodziej
#czarodziej zadaje zawsze damage, ale nieznaczny
class Wizzard(Character):
    def __init__(self):
        super().__init__(name='Wizzard', attack=" casted a spell", damage=10)


#klasa dzieciczącą z postaci - rycerz
#rycerz zadaje znaczny damage albo nie zadaje wcale, bo czarodziej blokuje go zaklęciem
class Knight(Character):
    def __init__(self):
        super().__init__(name="Knight", attack= " stabbed with a sword", damage=20)
    def fight(self, opponent):
        print("Knight makes an attempt")
        x = random.randint(0,1)
        if x == 1:
            super().fight(opponent)
        else:
            print("Wizzard used protection spell")

#tworzę postaci
wizzard = Wizzard()
knight = Knight()

#tworzę walkę pomiędzy postaciami 
def battle():
    while wizzard.life>0 and knight.life>0:
        wizzard.fight(knight)
        knight.fight(wizzard)
    else:
        if wizzard.life == 0:
            print("Knight has killed wizzard. Long live the king!")
        else:
            print("Wizzard has killed the knight. Let there be anarchy")

battle()

