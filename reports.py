def count_games(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    return(len(all_info))


def decide(file_name, year):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    in_list = False
    for sublist in all_info:
        for elem in sublist:
            if elem == str(year):
                in_list = True
    return in_list


def get_latest(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    years = []
    for sublist in all_info:
        years.append(int(sublist[2]))
    latest_game = (max(years))
    for sublist in all_info:
        if str(latest_game) in sublist:
            return(sublist[0])


def count_by_genre(file_name, genre):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    value_of_genre = 0
    for sublist in all_info:
        for elem in sublist:
            if elem == str(genre):
                value_of_genre += 1
    return value_of_genre


def get_line_number_by_title(file_name, title):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    for sublist in all_info:
        for elem in sublist:
            if elem == str(title):
                searched_title = sublist
    try:
        lines = []
        for sublist in all_info:
            if sublist != searched_title:
                lines.append(1)
            else:
                lines.append(1)
                break
        return len(lines)
    except:
        print("No Game Found!")


def sort_abc(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    game_names = []
    for sublist in all_info:
        game_names.append(sublist[0])
    return sorted(game_names)


def get_genres(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    game_genres = []
    for sublist in all_info:
        if sublist[3] not in game_genres:
            game_genres.append(sublist[3])
        else:
            pass
    return(sorted(game_genres, key=str.lower))


def when_was_top_sold_fps(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    fps_games = []
    for sublist in all_info:
        if "First-person shooter" in sublist:
                fps_games.append(sublist[:])
    try:
        most_sell = max(fps_games, key=lambda x: float(x[1]))
        for i in all_info:
            if most_sell == i:
                return int(i[2])
    except ValueError:
        print("No genre found !")