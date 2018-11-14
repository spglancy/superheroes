import random
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for x in range(len(self.abilities)):
            total += self.abilities[x].attack()
        return total

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health >= 0:
            return True
        elif self.current_health < 0:
            print(self.name + " died")
            return False

    def fight(self, opponent):
        while(self.is_alive() and opponent.is_alive()):
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage/2, self.max_damage)

class Team:
    def __init__(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        removed = False
        for x in range(len(self.heroes)):
            if self.heroes[x].name == name:
                self.heroes.pop(x)
                removed == True
        if not removed:
            return 0

    def view_all_heroes(self):
        output = list()
        for x in self.heroes:
            output.append(x.name)
        print(output)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    team = Team("meme")
    team.add_hero(hero)
    team.view_all_heroes()
    team.remove_hero(hero.name)
    team.view_all_heroes()
