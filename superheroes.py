import random

def verifyInt(arg):
    if not arg.isnumeric():
        return verifyInt(input("Invalid Input, Please enter an integer: "))
    return int(arg)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = int(starting_health)
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def defend(self):
        total = 0
        if self.current_health == 0:
            self.deaths += 1
            return total
        for x in self.armors:
            total += x.block()
        return total

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for x in range(len(self.abilities)):
            total += self.abilities[x].attack()
        return total

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def is_alive(self):
        if int(self.current_health) > 0:
            return True
        elif int(self.current_health) <= 0:
            self.current_health = 0
            return False

    def fight(self, opponent):
        while(self.is_alive() and opponent.is_alive()):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if not self.is_alive():
            opponent.add_kill(1)
            print(self.name + " died")
            self.deaths += 1
            return self
        elif not opponent.is_alive():
            self.add_kill(1)
            print(opponent.name + " died")
            opponent.deaths += 1
            return opponent



class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, int(self.max_damage))



class Weapon(Ability):
    def attack(self):
        return random.randint(int(self.max_damage)/2, int(self.max_damage))


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.copy = list()

    def healthCheck(self):
        total = 0
        for x in self.heroes:
            total += x.current_health
        return total

    def add_hero(self, Hero):
        self.heroes.append(Hero)
        self.copy.append(Hero)

    def remove_hero(self, name):
        removed = False
        for x in self.heroes:
            if x.name == name:
                self.heroes.pop(self.heroes.index(x))
                removed == True
        if not removed:
            return 0

    def find_hero(self, hero):
        for x in self.heroes:
            if x == hero:
                return True
        return False

    def attack(self, other_team):
         while self.healthCheck() > 0 and other_team.healthCheck() > 0:
            other_hero = other_team.heroes[random.randint(0, len(other_team.heroes)-1)]
            main_hero = self.heroes[random.randint(0, len(self.heroes)-1)]
            loser = main_hero.fight(other_hero)
            if self.find_hero(loser):
                self.remove_hero(loser.name)
            elif other_team.find_hero(loser):
                other_team.remove_hero(loser.name)

    def revive_heroes(self):
        if len(self.heroes) > 0:
            for x in range(len(self.heroes)):
                self.heroes.pop(x)
        for x in self.copy:
            x.current_health = x.starting_health
            self.heroes.append(x)


    def stats(self):
        totalDeaths = 0
        totalKills = 0
        for x in self.heroes:
            totalDeaths += x.deaths
            totalKills += x.kills
        if(totalDeaths > 0):
            print ("{}: {}".format(self.name, (totalKills/totalDeaths)))
        else:
            print ("{}: {}".format(self.name, float(totalKills)))

    def view_all_heroes(self):
        output = ""
        for x in self.heroes:
            output += x.name + " "
        print(output)



class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength.'''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, int(self.max_block))


class Arena:
    def __init__(self):
        '''
        Declare variables
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Create a name for this hero's ability: ")
        damage = verifyInt(input("What is the maximum damage for this ability: "))
        ability = Ability(name, damage)
        return ability

    def create_weapon(self):
        name = input("Create a name for this hero's weapon: ")
        damage = verifyInt(input("What is the maximum damage for this weapon: "))
        weapon = Weapon(name, damage)
        return weapon

    def create_armor(self):
        name = input("Create a name for this armor piece: ")
        block = verifyInt(input("What is this armor's power: "))
        armor = Armor(name, block)
        return armor

    def create_hero(self):
        name = input("What is this hero's name: ")
        health = verifyInt(input("How much health does this hero have: "))
        hero = Hero(name, health)
        abilities = verifyInt(input("How many abilities does this hero have: "))
        weapon = verifyInt(input("How many weapons does this hero have: "))
        armor = verifyInt(input("How many armors does this hero have: "))

        for x in range(abilities):
            hero.add_ability(self.create_ability())

        for y in range(weapon):
            hero.add_weapon(self.create_weapon())

        for z in range(armor):
            hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        name = input("Choose a name for this team: ")
        self.team_one = Team(name)
        heroes = verifyInt(input("How many heroes on this team: "))

        for x in range(heroes):
            self.team_one.add_hero(self.create_hero())

    def build_team_two(self):
        name = input("Choose a name for this team: ")
        self.team_two = Team(name)
        heroes = verifyInt(input("How many heroes on this team: "))

        for x in range(heroes):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        if self.team_one.healthCheck() < 1:
            print(self.team_two.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_two.heroes:
                if x.current_health > 0:
                    print(x.name)
        elif self.team_two.healthCheck() < 1:
            print(self.team_one.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_one.heroes:
                if x.current_health > 0:
                    print(x.name)
        print("Team Kill/Death Ratios:")
        self.team_one.stats()
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        elif play_again.lower() == "y":
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
        else:
            print("Invalid Input, terminating")
            game_is_running = False
