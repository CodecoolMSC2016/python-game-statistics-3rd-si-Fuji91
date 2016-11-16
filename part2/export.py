import reports
from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def export_results(value):                                    
    input_file = open("results.txt", "a")
    print(value, file=input_file)
    input_file.close()


export_results(count_games("game_stat.txt"))
export_results(decide("game_stat.txt", 2000))
export_results(get_latest("game_stat.txt"))
export_results(count_by_genre("game_stat.txt", "First-person shooter"))
export_results(get_line_number_by_title("game_stat.txt", "Counter-Strike"))
export_results(sort_abc("game_stat.txt"))
export_results(get_genres("game_stat.txt"))
export_results(when_was_top_sold_fps("game_stat.txt"))