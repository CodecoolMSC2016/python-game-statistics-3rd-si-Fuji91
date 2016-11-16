def get_most_played(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    name_and_copies = []
    for sublist in all_info:
        name_and_copies.append(sublist[0:2])
    most_sell = max(name_and_copies, key=lambda x: float(x[1]))
    return most_sell[0]


def sum_sold(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    all_copies = []
    for sublist in all_info:
        all_copies.append(float(sublist[1]))
    return(sum(all_copies))


def get_selling_avg(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    sold_copies = []
    for sublist in all_info:
        sold_copies.append(float(sublist[1]))
    return sum(sold_copies) / float(len(sold_copies))


def count_longest_title(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    game_names = []
    for sublist in all_info:
        game_names.append(sublist[0])
    sorted_games = sorted(game_names, key=len, reverse=True)
    return len(sorted_games[0])


def get_date_avg(file_name):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    release_years = []
    for sublist in all_info:
        release_years.append(int(sublist[2]))
    return round(int(sum(release_years) / len(release_years))) + 1


def get_game(file_name, title):
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    for sublist in all_info:
        for elem in sublist:
            if elem == str(title):
                searched_title = sublist
    converted_list = []
    for i in searched_title:
        try:
            converted_list.append(float(i))
        except:
            converted_list.append(i)
    return converted_list


def count_grouped_by_genre(file_name):    
    all_info = []
    with open(file_name) as inputfile:
        for line in inputfile:
            all_info.append(line.strip().split("\t"))
    genres = []
    for sublist in all_info:
        genres.append(sublist[3])
    genre_count = {}
    for i in genres:
        if i not in genre_count:
           genre_count.expand(i)
        else:
            pass
    return genre_count

def count_grouped_by_genre(file_name):
    try:
        all_info = []
        with open(file_name) as inputfile:
            for line in inputfile:
                all_info.append(line.strip().split("\t"))
        genres = []
        for game in all_info:
            genres.append(game[3])
        genres = list(set(genres))  # so every genre appears only once
        grouped_genres = {}
        for genre in genres:
            count = sum(x.count(genre) for x in all_info)
            grouped_genres.update({genre: count})
        return grouped_genres
    except FileNotFoundError:
        return "File not found."""

def get_date_ordered(file_name):
    try:
        all_info = []
        with open(file_name) as inputfile:
            for line in inputfile:
                all_info.append(line.strip().split("\t"))
        titles = []
        for game in all_info:
            titles.append((game[2], game[0]))
        titles.sort(key=lambda x: x[1])  
        titles.sort(key=lambda x: x[0], reverse=True)  
        date_ordered_titles = []
        for title in titles:
            date_ordered_titles.append(title[1])  
        return date_ordered_titles
    except FileNotFoundError:
        return "File not found."