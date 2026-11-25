"""Tests for the starter Recipe & Meal Planner."""

import json

from recipe_utils import filter_by_category, load_config, load_recipes, search_by_name, search_by_ingredient, suggest_random_meal


def test_search_by_name_finds_partial_match():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "chicken")
    assert result == [{"name": "Chicken Alfredo", "category": "Dinner"}]


def test_search_by_name_is_case_insensitive():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
    ]
    result = search_by_name(recipes, "SMOOTHIE")
    assert result == [{"name": "Berry Smoothie", "category": "Snack"}]


def test_search_by_name_returns_empty_list_when_no_match():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert search_by_name(recipes, "pizza") == []


def test_filter_by_category_returns_matching_recipes():
    recipes = [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Berry Smoothie", "category": "Snack"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]
    result = filter_by_category(recipes, "Dinner")
    assert result == [
        {"name": "Chicken Alfredo", "category": "Dinner"},
        {"name": "Tomato Pasta", "category": "Dinner"},
    ]


def test_filter_by_category_is_case_insensitive():
    recipes = [{"name": "Chicken Alfredo", "category": "Dinner"}]
    assert filter_by_category(recipes, "dinner") == [
        {"name": "Chicken Alfredo", "category": "Dinner"}
    ]


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "app_title": "Test Planner",
                "recipe_file": "recipes.json",
                "default_servings": 2,
            }
        ),
        encoding="utf-8",
    )
    result = load_config(config_file)
    assert result["app_title"] == "Test Planner"
    assert result["default_servings"] == 2


def test_load_recipes_reads_json(tmp_path):
    recipe_file = tmp_path / "recipes.json"
    sample = [
        {
            "name": "Test Recipe",
            "category": "Lunch",
            "servings": 2,
            "prep_time": 5,
            "cook_time": 10,
            "ingredients": [],
        }
    ]
    recipe_file.write_text(json.dumps(sample), encoding="utf-8")
    assert load_recipes(recipe_file) == sample



INGREDIENT_TEST_RECIPES = [
    {
        "name": "Veggie Omelet",
        "ingredients": [{"name": "Eggs"}, {"name": "Spinach"}],
    },
    {
        "name": "Chicken Pasta",
        "ingredients": [{"name": "Chicken Breast"}, {"name": "Pasta"}],
    },
]


def test_search_by_ingredient_finds_match():
    results = search_by_ingredient(INGREDIENT_TEST_RECIPES, "Eggs")
    assert len(results) == 1
    assert results[0]["name"] == "Veggie Omelet"


def test_search_by_ingredient_partial_match():
    results = search_by_ingredient(INGREDIENT_TEST_RECIPES, "chick")
    assert len(results) == 1
    assert results[0]["name"] == "Chicken Pasta"


def test_search_by_ingredient_case_insensitive():
    results = search_by_ingredient(INGREDIENT_TEST_RECIPES, "EGGS")
    assert len(results) == 1


def test_search_by_ingredient_no_match():
    assert search_by_ingredient(INGREDIENT_TEST_RECIPES, "banana") == []


def test_search_by_ingredient_empty_search():
    assert search_by_ingredient(INGREDIENT_TEST_RECIPES, "") == []


def test_search_by_ingredient_whitespace():
    results = search_by_ingredient(INGREDIENT_TEST_RECIPES, "  eggs  ")
    assert len(results) == 1

def test_random_meal_returns_valid_recipe():
    result = suggest_random_meal(INGREDIENT_TEST_RECIPES)
    assert result in INGREDIENT_TEST_RECIPES


def test_random_meal_empty_collection():
    assert suggest_random_meal([]) is None


def test_random_meal_single_recipe():
    recipes = [{"name": "Chicken Pasta"}]
    assert suggest_random_meal(recipes) == recipes[0]


def test_random_meal_does_not_modify_collection():
    recipes = [{"name": "Pasta"}, {"name": "Salad"}]
    original = [{"name": "Pasta"}, {"name": "Salad"}]

    suggest_random_meal(recipes)

    assert recipes == original