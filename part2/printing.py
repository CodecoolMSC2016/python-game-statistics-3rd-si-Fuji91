import reports

from reports import get_most_played
from reports import sum_sold
from reports import count_longest_title
from reports import get_selling_avg
from reports import get_date_avg
from reports import get_game
from reports import count_grouped_by_genre

print(get_most_played("game_stat.txt"))
print(sum_sold("game_stat.txt"))
print(count_longest_title("game_stat.txt"))
print(get_selling_avg("game_stat.txt"))
print(get_date_avg("game_stat.txt"))
print(get_game("game_stat.txt", "Counter-Strike"))
print(count_grouped_by_genre("game_stat.txt"))