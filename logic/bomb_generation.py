import random
import logic.case

def generate_bombs(case,dificulty):
    
    if dificulty == 'easy':
        max_bombs = 10
        min_bombs = 5
    elif dificulty == 'medium':
        max_bombs = 20
        min_bombs = 10

    elif dificulty == 'hard':
        max_bombs = 30
        min_bombs = 20
    else:
        raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")

    num_bombs = random.randint(min_bombs, max_bombs)
    for _ in range(num_bombs):
        x = random.randint(0, len(case)-1)
        y = random.randint(0, len(case[0])-1)
        if not case[x][y].is_bombe:
            case[x][y].is_bombe = True
        

    
    