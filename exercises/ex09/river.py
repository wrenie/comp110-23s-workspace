"""File to define River class."""

__author__ = "730566370"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River as a class."""
    # river attrbutes
    day: int  # what day of the river lifecycle are we on
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Boomer fish and boomer bears die off from the river population."""
        survive_fish: list[Fish] = []
        survive_bears: list[Bear] = []
        for elem in range(0, len(self.fish)):
            fish: Fish = self.fish[elem]
            if fish.age <= 3:
                survive_fish.append(fish)
        for elem in range(0, len(self.bears)):
            bear: Bear = self.bears[elem]
            if bear.age <= 5:
                survive_bears.append(bear)
        self.bears = survive_bears
        self.fish = survive_fish
        return None

    def bears_eating(self):
        """Let them (bears) eat cake (fish)!"""
        if len(self.bears) == 0:
            return None
        for elem in range(0, len(self.bears)):
            if len(self.fish) > 5:
                self.remove_fish(3)
                self.bears[elem].eat(3)
        return None
    
    def check_hunger(self):
        """Kill off the starving bears."""
        survive_bear: list[Bear] = []
        for elem in range(0, len(self.bears)):
            if self.bears[elem].hunger_score >= 0:
                survive_bear.append(self.bears[elem])
        self.bears = survive_bear
        return None
        
    def repopulate_fish(self):
        """Fish are born, 4 babies for every pair of fish."""
        new_fish: int = (len(self.fish) // 2) * 4
        for elem in range(0, new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Bears are born, 1 baby for every pair of bears."""
        # for 2 bears, 1 bear will be born
        new_bears: int = len(self.bears) // 2
        for elem in range(0, new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View the value of the populations in the river."""
        fish_count: int = 0
        bear_count: int = 0
        for fish in range(0, len(self.fish)):
            fish_count += 1
        for bear in range(0, len(self.bears)):
            bear_count += 1
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {fish_count}")
        print(f"Bear population: {bear_count}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week of river life."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes a specific number of fish from the river."""
        for elem in range(0, amount):
            self.fish.pop(elem)  # removing that many fish from the river
        return None