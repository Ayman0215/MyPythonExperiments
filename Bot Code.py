def bot_movement():
    x, y = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    facing = 0
    reps = int(input("Enter number of turns: "))

    for i in range(reps):
        turn = input("Enter direction (L, R, F, B): ").upper()
        
        if turn == "L":
            facing = (facing - 1) % 4
        elif turn == "R":
            facing = (facing + 1) % 4
        elif turn == "F":
            distance = int(input("Enter distance:"))
            dx, dy = directions[facing]
            x += dx * distance
            y += dy * distance
        elif turn == "B":
            distance = int(input("Enter distance: "))
            dx, dy = directions[facing]
            x -= dx * distance
            y -= dy * distance
        else:
            print("Invalid")
    print("Final point:", (x, y))

bot_movement()
