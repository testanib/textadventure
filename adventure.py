from random import randint
import random
"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

"""
__author__ = ""
__version__ = 2

class World:

    """
    Attributes:
        player (Player): The player character's information
        game_status (str): The current state of the game: either
                           "playing", "won", or "lost".
        weather (Weather): The world weather information
    """
    def __init__(self):
        self.player = Player("Field", False, False, [])
        self.game_status = "playing"
        self.weather = Weather(bool(random.getrandbits(1)), randint(0, 100))
        
    def is_done(self):
        '''
        Consumes nothing and produces a boolean indicating whether the game should end.
        '''
        if self.game_status != "playing":
            return True
        else:
            return False
    
    def is_good(self):
        '''
        Consumes nothing and produces a boolean indicating whether the
        World state is currently valid.
        '''
        return True
    
    def update_loc_list(self, loc):
        '''
        Consumes a location and adds it to the players visited locations list
        Args:
            loc (str): The location
        '''
        self.player.places_visited.append(loc)
    
    
    def has_protection(self):
        '''
        Consumes nothing and produces a string based on if the player has protection
        '''
        if self.player.has_protection == False:
            return "\nYou do not Have protection"
        else:
            return "\nYou have protection"
        
    def has_key(self):
        '''
        Consumes nothing and produces a string based on if the player has the key
        '''
        if self.player.has_key == False:
            return "\nYou do not have the key"
        else:
            return "\nYou have the key"
    
    def is_weather_deadly(self):
        '''
        Consumes nothing and produces a string based on if the weather is deadly
        '''
        if self.weather.is_deadly:
            return "\nCareful, the weather is deadly"
        else:
            return "\nThe weather is not deadly"
        
    def print_list(self):
        s = "\nYou've visited:\n"
        for x in self.player.places_visited:
            s += x + "\n"
        return s
    
    #loc = "\nYour location is: "
    #options = "\nYou can go to these places:\n "
    #instr = "\nType 'Enter' and your choice: "
    #temp = "The Tempurature is " + str(world.weather.temp) + " degrees"
        
    def render(self):
        '''
        Consumes nothing and produces a string of the text to print to the
        console. 
        '''
        
        field_list = ["Maze, ", "House, ", "Woods"]
        house_list = ["Woods, ", "Field"]
        woods_list = ["Cave, ", "House, ", "Field"]
        cave_list = ["Woods, ", "Room, ", "Bunker, ", "Continue in cave"]
        room_list = ["Room, ", "Cave"]
        bunker_list = ["Cave"]
    
        loc = "\nYour location is: "
        options = "\nYou can go to these places:\n "
        instr = "\nType 'Enter' and your choice: "
        temp = "The Tempurature is " + str(self.weather.temp) + " degrees"
    
        if self.player.location == "Field":
            return temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Field" + options + self.next_choice(field_list) + instr
        elif self.player.location == "Maze":
            return loc + "Maze" + self.print_list()
        elif self.player.location == "House":
            return temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "House" + options + self.next_choice(house_list) + instr
        elif self.player.location == "Woods":
            return self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Woods" + options + self.next_choice(woods_list) + instr
        elif self.player.location == "Cave":
            return temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Cave" + options + self.next_choice(cave_list) + instr
        elif self.player.location == "Room":
            return temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Room" + options + self.next_choice(room_list) + instr
        elif self.player.location == "Bunker" and self.player.has_key == False:
            return temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Bunker" + options + self.next_choice(bunker_list) + instr
        else:
            return temp + loc + self.player.location
    
    
    def next_choice(self, lst):
        '''
        Consumes a list and returns each element of the list individually
        Args:
            lst (list): list of elements
        Returns:
            each element individually (or print)
        '''
        s = ""
        for x in lst:
            s += x + "\n"
        return s
        
    def good_strings(self, loc, command):
        '''
        Consumes a location string and a command string and returns a boolean
        based on if it is considered a valid command
        Args:
            loc (str): location
            command (str): user entered command
        Returns:
            boolean based on if a valid command was entered
        '''
        
        if command == "quit":
            self.game_status = "quit"
            return True
        if loc == "Field":
            if command[6:] == "Maze":
                return True
            elif command[6:] == "House":
                return True
            elif command[6:] == "Woods":
                return True
            else:
                return False
        if loc == "House":
            if command[6:] == "Woods":
                return True
            elif command[6:] == "Field":
                return True
            else:
                return False
        if loc == "Woods":
            if command[6:] == "Cave":
                return True
            elif command[6:] == "House":
                return True
            elif command[6:] == "Field":
                return True
            else:
                return False
        if loc == "Cave":
            if command[6:] == "Room":
                return True
            elif command[6:] == "Bunker":
                return True
            elif command[6:] == "Woods":
                return True
            elif command[6:] == "Continue in cave":
                return True
            else:
                return False
        if loc == "Room":
            if command[6:] == "Room":
                return True
            elif command[6:] == "Cave":
                return True
            else:
                return False
        if loc == "Bunker":
            if command[6:] == "Cave":
                return True
            else:
                return False
    
    def is_input_good(self, command):
        '''
         Consumes a string (representing the user's input)
         and produces a boolean indicating whether it was a valid choice.
         Args:
             command (str): user inputted command
         Returns:
             boolean based on if it was a valid command
        '''
        loc = self.player.location
        return self.good_strings(loc, command)
    
    def process_field(self, command):
        '''
        Consumes a command string and updates the players location
        '''
        self.player.location = command[6:]
        self.update_loc_list(command[6:])
    
    def process_maze(self):
        '''
        Consumes nothing and sets the game status to lost
        '''
        self.update_loc_list("Maze")
        self.game_status = "lost"
    
    def process_woods(self, command):
        '''
        Consumes a command and updates the game status or player location
        '''
        self.update_loc_list(command[6:])
        if self.weather.is_deadly and self.player.has_protection == False:
            self.game_status = "lost"
        else:
            self.player.location = command[6:]
    
    def process_cave(self, command):
        '''
        Consumes a command and updates the game status or player location
        '''
        self.update_loc_list(command[6:])
        if command[6:] == "Continue in cave":
            self.game_status = "lost"
        else:
            self.player.location = command[6:]
    
    def process_house(self, command):
        '''
        Consumes a command and updates the player location and
        sets has_protection to True
        '''
        self.update_loc_list(command[6:])
        self.player.has_protection = True
        self.player.location = command[6:]
    
    def process_room(self, command):
        '''
        Consumes a command and updates the player location and
        sets has_key to True
        '''
        self.update_loc_list(command[6:])
        self.player.has_key = True
        self.player.location = command[6:]
    
    def process_bunker(self, command):
        '''
        Consumes a command and sets game status to won or updates
        player location
        '''
        self.player.location = "Bunker"
        self.update_loc_list("Bunker")
        if self.player.has_key:
            self.game_status = "won"
            
        else:
            self.player.location = command[6:]
    
    def process(self, command):
        '''
        Consumes a string and produces nothing.  Updates world state
        Args:
            command (str): user inputted command
        '''
        
        if self.player.location == "Field":
            self.process_field(command)
        elif self.player.location == "House":
            self.process_house(command)
        elif self.player.location == "Maze":
            self.process_maze()
        elif self.player.location == "Woods":
            self.process_woods(command)
        elif self.player.location == "Cave":
            self.process_cave(command)
        elif self.player.location == "Room":
            self.process_room(command)
        elif self.player.location == "Bunker":
            self.process_bunker(command)
    
    def tick(self):
        '''
        Consumes nothing and produces nothing.
        This function should have side effects that update the world's state.
        '''
        pass
    
    def render_start(self):
        '''
        Consumes nothing and produces a string that introduces the game to the user.
        '''
        
        return """Welcome to Dangerous Roaming\n\nBy Ben Testani\n\n\n\n
                    You are in an empty field.\nYou can enter a house, enter the woods,
                    or enter a corn maze\n
                    Type 'Enter' and your choice (Maze, House or Woods)"""
    
    def render_ending(self):
        '''
        Consumes nothing and produces a different string depending on whether
        the user has "won", "lost", or "quit" the game
        '''
        if self.game_status == "won":
            return "Congrats! You Won!"
        elif self.game_status == "lost":
            return "Sorry, You've Lost"
        elif self.game_status == "quit":
            return "You have chosen to quit the game."
        else:
            return "Invalid status"
        

class Player:
    """
    Attributes:
        location (str): The current location of the player
                        within the world.
        has_key (bool): Whether the player has found the key.
        has_protection (bool): Whether the player has protection
                               from the deadly weather.
        places_visted (list): places in the world that the player has
                              visited

    """
        
    def __init__(self, location, has_key, has_protection, places_visited):
        self.location = location
        self.has_key = has_key
        self.has_protection = has_protection
        self.places_visited = places_visited
class Weather:
    """
    Attributes:
        is_deadly (bool): Whether the weather is deadly.
        temp (int): Weather's tempurature.
    """
    
    def __init__(self, is_deadly, temp):
        self.is_deadly = is_deadly
        self.temp = temp
# Command Paths to give to the unit tester
WIN_PATH = ["Enter House", "Enter Woods", "Enter Cave", "Enter Room", "Enter Cave", "Enter Bunker"]
LOSE_PATH = ["Enter Maze"]


def main():
    '''
    #This is the Main game function. When executed, it begins a run of the game.
    #Read over it to understand the engine that you are using and the order
    #that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())
    
    
  
# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
#world = World()
    #world.is_done()
    #print(world.render())
    # ...
    
world = World()
assert world.player.location == "Field"
assert world.player.has_key == False
assert world.player.has_protection == False
assert world.player.places_visited == []
assert world.game_status == "playing"
assert world.is_good()
assert world.render_start() == """Welcome to Dangerous Roaming\n\nBy Ben Testani\n\n\n\n
                    You are in an empty field.\nYou can enter a house, enter the woods,
                    or enter a corn maze\n
                    Type 'Enter' and your choice (Maze, House or Woods)"""
assert not world.is_done()
assert world.update_loc_list("House") == world.player.places_visited.append("House")
assert world.has_protection() == "\nYou do not Have protection"
assert world.has_key() == "\nYou do not have the key"
#assert world.is_weather_deadly() == "\nThe weather is not deadly"
world.player.places_visited.append("House")
#assert world.print_list() == "\nYou've visited:\n" + "House"
world.player.location = "Field"
#assert world.render() == temp + self.is_weather_deadly() + self.has_protection() + self.has_key() + self.print_list() + loc + "Field" + options + self.next_choice(field_list) + instr
assert world.next_choice(["Field"]) == "Field\n"

assert world.good_strings("Field", "quit") == True
assert world.good_strings("Field", "Enter Maze") == True
assert world.good_strings("Field", "Enter House") == True
assert world.good_strings("Field", "Enter Woods") == True
assert world.good_strings("Field", "safd") == False
assert world.good_strings("House", "Enter Woods") == True
assert world.good_strings("House", "Enter Field") == True
assert world.good_strings("House", "Enter Wosdfsdods") == False
assert world.good_strings("Woods", "Enter Cave") == True
assert world.good_strings("Woods", "Enter House") == True
assert world.good_strings("Woods", "Enter Field") == True
assert world.good_strings("Woods", "Enter sdf") == False
assert world.good_strings("Cave", "Enter Room") == True
assert world.good_strings("Cave", "Enter Woods") == True
assert world.good_strings("Cave", "Enter Bunker") == True
assert world.good_strings("Cave", "Enter Continue in cave") == True
assert world.good_strings("Cave", "Enter sd") == False
assert world.good_strings("Room", "Enter Cave") == True
assert world.good_strings("Room", "Enter sd") == False

assert world.is_input_good("quit") == True
world.player.location = "Field"
assert world.is_input_good("Enter House")
assert world.is_input_good("Enter Woods")
world.process_field("Enter House")
assert world.player.location == "House"
#assert world.player.places_visited == ["House"]
#assert world.player.places_visited.append("House")
world.process_house("Enter Woods")
assert world.player.location == "Woods"
world.player.location = "Woods"
assert world.is_input_good("Enter Field")
assert world.is_input_good("Enter Cave")
world.process_woods("Enter Cave")
assert world.player.location == "Cave"
world.player.location = "Cave"
assert world.is_input_good("Enter Room")
assert world.is_input_good("Enter Bunker")
assert world.is_input_good("Enter Continue in cave")
world.process_cave("Enter Room")
assert world.player.location == "Room"
world.player.location = "Room"
assert world.is_input_good("Enter Cave")
world.process_room("Enter Cave")
assert world.player.location == "Cave"
world.player.location = "Cave"
world.process_cave("Enter Bunker")
assert world.player.location == "Bunker"
world.player.location = "Cave"
world.process_cave("Enter Continue in cave")
assert world.game_status == "lost"
world.game_status = "playing"
world.player.location = "Field"
world.process("Enter House")
assert world.player.location == "House"
world.player.location = "House"
world.process("Enter Woods")
assert world.player.location == "Woods"
world.player.location = "Woods"
world.process("Enter Cave")
assert world.player.location == "Cave"
world.player.location = "Cave"
world.process("Enter Room")
assert world.player.location == "Room"
world.player.location = "Cave"
world.player.has_key = True
world.process("Enter Bunker")
assert world.player.location == "Bunker"
#assert world.game_status == "won"
world.player.location = "Room"
world.process("Enter Cave")
assert world.player.location == "Cave"

world.game_status = "won"
assert world.render_ending() == "Congrats! You Won!"
world.game_status = "lost"
assert world.render_ending() == "Sorry, You've Lost"
world.game_status = "quit"
assert world.render_ending() == "You have chosen to quit the game."
