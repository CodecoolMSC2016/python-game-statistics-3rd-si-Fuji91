import reports
from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


print(count_games("game_stat.txt"))
print(decide("game_stat.txt", 2000))
print(get_latest("game_stat.txt"))
print(count_by_genre("game_stat.txt", "First-person shooter"))
print(get_line_number_by_title("game_stat.txt", "Counter-Strike"))
print(sort_abc("game_stat.txt"))
print(get_genres("game_stat.txt"))
print(when_was_top_sold_fps("game_stat.txt"))