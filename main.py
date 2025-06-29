# ModuleSixMilestone.py
# Author:Sharadiya Sarkar


# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}


def display_current_room(current_room):
    """
    Display the current room to the player
    Args:
        current_room (str): The name of the current room
    """
    print(f"\nYou are in the {current_room}")


def get_valid_directions(current_room):
    """
    Get list of valid directions from current room
    Args:
        current_room (str): The name of the current room
    Returns:
        list: List of valid directions from current room
    """
    if current_room in rooms:
        return list(rooms[current_room].keys())
    return []


def display_available_moves(current_room):
    """
    Display available moves to the player
    Args:
        current_room (str): The name of the current room
    """
    valid_directions = get_valid_directions(current_room)
    if valid_directions:
        print(f"You can go: {', '.join(valid_directions)}")
    else:
        print("No exits available from this room.")


def process_move_command(command, current_room):
    """
    Process a movement command and return new room
    Args:
        command (str): Player's movement command
        current_room (str): Current room name
    Returns:
        str: New room name or current room if invalid move
    """
    # Extract direction from command (remove 'go ' if present)
    if command.lower().startswith('go '):
        direction = command[3:].strip().title()  # Remove 'go ' and capitalize
    else:
        direction = command.strip().title()  # Just capitalize the direction

    # Check if the direction is valid from current room
    if current_room in rooms and direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        print(f"\nYou move {direction} to the {new_room}.")
        return new_room
    else:
        # Invalid move - display error and available options
        print(f"\nInvalid move! You cannot go {direction} from the {current_room}.")
        display_available_moves(current_room)
        return current_room


def main():
    """
    Main game loop function
    """
    # Initialize starting room
    current_room = 'Great Hall'

    # Welcome message
    print("=" * 50)
    print("Welcome to the Dragon Text Adventure Game!")
    print("=" * 50)
    print("Commands:")
    print("- To move: enter a direction (North, South, East, West)")
    print("- To move: enter 'go' followed by direction (go North)")
    print("- To quit: enter 'exit'")
    print("=" * 50)

    # Main gameplay loop
    while current_room != 'exit':
        # Display current room and available moves
        display_current_room(current_room)
        display_available_moves(current_room)

        # Get player input
        print("\nWhat would you like to do?")
        player_command = input("> ").strip()

        # Input validation - check for empty input
        if not player_command:
            print("\nPlease enter a command!")
            continue

        # Decision branching for different commands
        if player_command.lower() == 'exit':
            # Player wants to exit the game
            current_room = 'exit'
            print("\nThanks for playing! Goodbye!")

        elif (player_command.lower().startswith('go ') or
              player_command.lower() in ['north', 'south', 'east', 'west']):
            # Player wants to move
            current_room = process_move_command(player_command, current_room)

        else:
            # Invalid command - provide helpful error message
            print(f"\nInvalid command: '{player_command}'")
            print("Valid commands are:")
            print("- Direction names: North, South, East, West")
            print("- Move commands: go North, go South, etc.")
            print("- Exit command: exit")



if __name__ == "__main__":
    main()