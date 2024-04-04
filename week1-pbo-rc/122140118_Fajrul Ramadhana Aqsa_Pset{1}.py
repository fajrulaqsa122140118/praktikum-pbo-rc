import random

class Character:
    def __init__(self, name, hp, attack, accuracy, heal_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.accuracy = accuracy
        self.heal_power = heal_power

    def take_damage(self, damage):
        self.hp -= damage

    def heal(self):
        heal_amount = random.randint(7, self.heal_power)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        print(f"{self.name} heals for {heal_amount} HP.")

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        if random.random() < self.accuracy:
            damage = random.randint(10, self.attack)
            enemy.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        else:
            print(f"{self.name} MISSES the attack on {enemy.name}!")


character1 = Character("OPTIMUS", 100, 20, 0.7, 15)  
character2 = Character("MEGATRON", 80, 25, 0.75, 10)     


turn = 1
while character1.is_alive() and character2.is_alive():
    print(f"TURN {turn}")
    print(f"{character1.name}'s turn!")
    print("pilih aksi yang akan diberikan:")
    print("1. serang")
    print("2. heal")
    choice = input("pilih opsi (1 or 2): ")

    if choice == '1':
        character1.attack_enemy(character2)
    elif choice == '2':
        character1.heal()
    else:
        print("ERROR. Silahkan pilih opsi 1 for serang or 2 for Heal.")

    print("--------------------------------------")
    print(f"{character1.name} HP: {character1.hp}")
    print(f"{character2.name} HP: {character2.hp}")
    print("")

    if character2.is_alive():
        print(f"{character2.name}'s turn!")
        print("pilih aksi yang akan diberikan:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            character2.attack_enemy(character1)
        elif choice == '2' and character2.is_alive():
            character2.heal()
        else:
            print("ERROR. Silahkan pilih opsi 1 for serang or 2 for Heal.")

    print("--------------------------------------")
    print(f"{character1.name} HP: {character1.hp}")
    print(f"{character2.name} HP: {character2.hp}")
    print("")
    turn += 1
    print("\n")


if character1.is_alive():
    print(f"{character1.name}  Menang!")
else:
    print(f"{character2.name}  Kalah!")
