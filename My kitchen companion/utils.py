import pickle as pkl

path2root = '.'
closest = pkl.load(open(f'{path2root}/data/closest_recipes.pkl', 'rb'))
data_filtered = pkl.load(open(f'{path2root}/data/data_df_filtered.pkl', 'rb'))
first_ingredients = pkl.load(open(f'{path2root}/data/initial_features/flavors/first_ingredients.pkl', 'rb'))

# Data
num_recipes = 10_000

# Graph
edge_amount = ['number', 'threshold'][1]
num_edges = 5_000
comb_degree = 1000  # out of num_recipes
threshold = 0.95

# interface
helps = {"sdb_myzone_btn": "Enter your personal zone",
         "sdb_tut_btn": "How to use My Kitchen Companion",
         "sdb_about_btn": "Read about us",
         "temperature": "Select the temperature of the recipe",
         "include": "Any specific ingredients you would like to include?",
         "exclude": "Any specific ingredients you would like to exclude?",
         "preparation_time": "Set the preparation time - Fast <--> Slow",
         "healthiness": "Set the healthiness - Less <--> More",
         "": ""}


def build_comb(sw, so, sa, sp, temp, prep, health):
    b2i = lambda x: 1 if x else 0
    comb = [0] * 7
    comb[0] = b2i(sw)
    comb[1] = b2i(so)
    comb[2] = b2i(sa)
    comb[3] = b2i(sp)
    comb[4] = {'Cold': 0, 'Natural': 1, 'Hot': 2}[temp]
    comb[5] = prep // 10
    comb[6] = health // 10
    return tuple(comb)


def get_recipe(comb, index=0, include=(), exclude=()):
    closest_recipes = closest.loc[[comb]]

    i = 0
    from_df = None
    good = False
    for t_recipe in closest_recipes[0]:
        good, from_df = good_recipe(t_recipe, include, exclude)
        if good:
            if i == index:
                break
            else:
                i += 1
    else:
        return (None,) * 3

    name = from_df['title_1']
    ingredients = "\n".join(from_df['ingredients_3'])
    instructions = "\n".join(from_df['instructions_3'])
    return name, ingredients, instructions


def good_recipe(recipe, include, exclude):
    from_df = data_filtered.loc[recipe]
    ingredients = from_df['ingredients_2']
    includes = [(to_inc in ingredients) for to_inc in include]
    excludes = [(to_exc not in ingredients) for to_exc in exclude]
    good = all(includes) and all(excludes)
    return good, from_df
