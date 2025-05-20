import pandas
from pandas import DataFrame

def get_count(data: DataFrame, color: str, col_name = "Primary Fur Color"):
    col_data = data[data[col_name] == color]
    return len(col_data)

data = pandas.read_csv('squirrel_data.csv')

# grey_squirrels = data[data['Primary Fur Color'] == 'Gray']
grey_squirrels_count = get_count(data, "Gray")

# cinammon_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
cinammon_squirrels_count = get_count(data, "Cinnamon")
# cinammon_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
# cinammon_squirrels_count = len(cinammon_squirrels)

black_squirrel_count = get_count(data, "Black")

compiled_data = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [grey_squirrels_count, cinammon_squirrels_count, black_squirrel_count]
}

dataframe = DataFrame(compiled_data)
dataframe.to_csv('squirrel_count.csv')