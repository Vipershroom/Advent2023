def parse_game_str(game: str) -> dict:
    game_arr = game.split(':')
    game_id = game_arr.pop(0)
    colors = ''.join(game_arr).strip().split('; ')
    return {
        "game_id": game_id.split(' ')[-1],
        "colors": colors
    }

def eval(game: str):
    game_obj = parse_game_str(game)
    max_vals = (12, 13, 14) #red,green,blue
    for color in game_obj['colors']:
        color_single = color.split(',')

file = 'input.txt'

print(parse_game_str("Game 1: 4 green, 2 blue; 1 red, 1 blue, 4 green; 3 green, 4 blue, 1 red; 7 green, 2 blue, 4 red; 3 red, 7 green; 3 red, 3 green"))