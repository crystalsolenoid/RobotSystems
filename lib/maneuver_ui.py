import picarx_improved as picarx

help_page = ''' Commands are case sensitive.

Exit            closes program
Help            displays command reference
Forward         drives forward
Backward        drives backward
Parallel Left   parallel parks to the left
Parallel Right  parallel parks to the right
KTurn Left      three-point turn to the left
KTurn Right     three-point turn to the right

'''

unrecognized_message = "Unrecognized command. Enter 'help' for help."

if __name__ == "__main__":
    px = picarx.Picarx()
    end_program = False
    while not end_program:
        raw = input("Enter command: ")
        command = raw.lower()
        if command == "exit":
            end_program = True
        elif command == "help":
            print(help_page)
        elif command == "forward":
            px.drive_distance(1, 0)
        elif command == "backward":
            px.drive_distance(-1, 0)
        elif command == "parallel left":
            px.parallel_park(-1)
        elif command == "parallel right":
            px.parallel_park(1)
        elif command == "kturn left":
            px.k_turn(-1)
        elif command == "kturn right":
            px.k_turn(1)
        else:
            print(unrecognized_message)
