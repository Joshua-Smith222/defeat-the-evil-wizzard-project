import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 20
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}! Current health: {self.health}")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.evade_next = False

    def special_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} performs a special attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def quick_shot(self, opponent):
        damage = self.attack_power + random.randint(10, 20)
        opponent.health -= damage
        print(f"{self.name} fires a Quick Shot at {opponent.name} for {damage} damage!")

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_active = False

    def heal(self):
        heal_amount = 20
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def holy_strike(self, opponent):
        damage = self.attack_power + random.randint(10, 15)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        self.shield_active = True
        print(f"{self.name} activates Divine Shield!")


# Shadow Warrior class (inherits from Character)
class ShadowWarrior(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=28)

    def stealth_attack(self, opponent):
        damage = round(self.attack_power * 1.5)
        opponent.health -= damage
        print(f"{self.name} performs a stealth attack on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

 # Shadow Mage class (inherits from Character)
class ShadowMage(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=32)

    def shadow_bolt(self, opponent):
        damage = round(self.attack_power * 1.8)
        opponent.health -= damage
        print(f"{self.name} casts Shadow Bolt on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# shape-shifting class (inherits from Character)
class ShapeShifter(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)
        self.defense = 5
        self.form = "Human"

    def transform(self, form):
        if self.form.lower() == form:
            print(f"{self.name} is already in {self.form} form!")
            return

        forms = {
            "wolf": {"attack": 35, "defense": 10, "health": 100},
            "bear": {"attack": 25, "defense": 20, "health": 140},
            "eagle": {"attack": 30, "defense": 5, "health": 90}
        }

        form = form.lower()
        if form in forms:
            stats = forms[form]
            self.attack_power = stats["attack"]
            self.defense = stats["defense"]
            self.health = stats["health"]
            self.max_health = stats["health"]
            self.form = form.capitalize()
            print(f"{self.name} transforms into a {self.form}!")
            print(f"Stats → Attack: {self.attack_power}, Defense: {self.defense}, Health: {self.health}")
        else:
            print("Invalid form. Choose: Wolf, Bear, or Eagle.")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.shield_block_active = False

    def power_strike(self, opponent):
        damage = self.attack_power + random.randint(15, 25)
        opponent.health -= damage
        print(f"{self.name} performs a Power Strike on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_block(self):
        self.shield_block_active = True
        self.health += 10
        print(f"{self.name} uses Shield Block and gains 10 health! Current health: {self.health}")
        if self.health > self.max_health:
            self.health = self.max_health

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.ice_shield_active = False

    def fireball(self, opponent):
        damage = self.attack_power + random.randint(20, 30)
        opponent.health -= damage
        print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def ice_shield(self):
        self.ice_shield_active = True
        self.health += 15
        print(f"{self.name} casts Ice Shield and gains 15 health! Current health: {self.health}")
        if self.health > self.max_health:
            self.health = self.max_health

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class

# Create Paladin class


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    print("5. Shadow Warrior")
    print("6. Shadow Mage")
    print("7. Shape Shifter")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return ShadowWarrior(name)
    elif class_choice == '6':
        return ShadowMage(name)
    elif class_choice == '7':
        return ShapeShifter(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("1. Quick Shot\n2. Evade")
                sub_choice = input("Choose ability: ")
                if sub_choice == '1':
                    player.quick_shot(wizard)
                else:
                    player.evade()

            elif isinstance(player, Paladin):
                print("1. Holy Strike\n2. Divine Shield")
                sub_choice = input("Choose ability: ")
                if sub_choice == '1':
                    player.holy_strike(wizard)
                else:
                    player.divine_shield()
            elif isinstance(player, ShadowWarrior):
                player.stealth_attack(wizard)
            elif isinstance(player, ShadowMage):
                player.shadow_bolt(wizard)
            elif isinstance(player, ShapeShifter):
                form = input("Choose form (wolf/bear/eagle): ")
                player.transform(form)

            elif isinstance(player, Warrior):
                print("1. Power Strike\n2. Shield Block")
                sub_choice = input("Choose ability: ")
                if sub_choice == '1':
                    player.power_strike(wizard)
                else:
                    player.shield_block()

            elif isinstance(player, Mage):
                print("1. Fireball\n2. Ice Shield")
                sub_choice = input("Choose ability: ")
                if sub_choice == '1':
                    player.fireball(wizard)
                else:
                    player.ice_shield()


        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            if hasattr(player, 'evade_next') and player.evade_next:
                print(f"{player.name} evaded the attack!")
                player.evade_next = False
            elif hasattr(player, 'shield_active') and player.shield_active:
                 print(f"{player.name}'s Divine Shield blocks the attack!")
                 player.shield_active = False
            elif isinstance(player, ShapeShifter) and player.form.lower() == "bear":
                 print(f"{player.name} in Bear form takes reduced damage!")
                 damage = random.randint(0, wizard.attack_power // 6)
                 player.health -= damage
                 print(f"{wizard.name} attacks {player.name} for {damage} damage!")
            elif isinstance(player, ShapeShifter) and player.form.lower() == "wolf":
                 print(f"{player.name} in Wolf form takes reduced damage!")
                 damage = random.randint(0, wizard.attack_power // 3)
                 player.health -= damage
                 print(f"{wizard.name} attacks {player.name} for {damage} damage!")
            elif isinstance(player, ShapeShifter) and player.form.lower() == "eagle":
                 print(f"{player.name} in Eagle form takes reduced damage!")
                 damage = random.randint(0, wizard.attack_power // 2)
                 player.health -= damage
                 print(f"{wizard.name} attacks {player.name} for {damage} damage!")
            elif isinstance(player, ShapeShifter):
                 print(f"{player.name} in Human form takes normal damage!")
                 wizard.attack(player)
            elif isinstance(player, Warrior) and player.shield_block_active:
                 print(f"{player.name}'s Shield Block absorbs the attack!")
                 player.shield_block_active = False
            elif isinstance(player, Mage) and player.ice_shield_active:
                 print(f"{player.name}'s Ice Shield absorbs the attack!")
                 player.ice_shield_active = False
            else:
                 wizard.attack(player)

            print(f"{player.name}'s health: {player.health}/{player.max_health}")
            print(f"{wizard.name}'s health: {wizard.health}/{wizard.max_health}")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
