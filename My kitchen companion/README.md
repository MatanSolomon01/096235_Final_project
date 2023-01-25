# My kitchen companion

## Independent data structures
* Everything in `raw`
* `verbs.txt`

## Produced by ChatGPT:
* `hot_words.txt`
* `cold_words.txt`

## Pipeline
1. `data_preparation.py` --> `data_df.pkl`
2. `data_exploration.ipynb` --> `first_ingredients.pkl`
### Initial representation
3. `flavors_from_gpt.ipynb` --> `temp_dict_i`, `ingredients_flavor.pkl`
4. `rep_flavors.ipynb` --> `rep_flavors.pkl`
5. `rep_temperature.ipynb` --> `rep_temp.pkl`
6. `rep_time.ipynb` --> `rep_times.pkl`
7. `rep_healthiness.ipynb` --> `rep_health.pkl`
8. `total_representation.ipynb` --> `initial_features_dict.pkl`, `data_df_filtered.pkl`
## Similarities
9. `tf_idf_calculator.ipynb` --> `tf_idf_similarities.pkl`
10. `comb_recipe_similarity.ipynb` --> `comb_recipe_similarities.pkl`