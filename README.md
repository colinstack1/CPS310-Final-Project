# CPS 310 Final Project
## Recipe & Meal Planner

This repository contains the Recipe & Meal Planner application for the CPS 310 final project.

The application currently supports:

- Loading recipe data from JSON
- Listing all recipes
- Searching recipes by name
- Filtering recipes by category
- Viewing recipe details
- Loading basic configuration from `config.json`
- Searching recipes by ingredient
- Random meal suggestions

Two of the three selected final project features have been completed for Checkpoint 1.

## Setup

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

## Run Tests

### Windows

```powershell
python -m pytest -v
```

### macOS

```bash
python3 -m pytest -v
```

## Selected Final Project Features

### 1. Search by Ingredient — Completed

- Search for recipes containing a specific ingredient.
- Supports partial matches and case-insensitive searches.
- Handles empty searches and searches with no results.
- Available through menu option 5.
- GitHub Issue #1 and Pull Request #4.

### 2. Random Meal Suggestion — Completed

- Randomly selects a recipe from the available collection.
- Displays the complete recipe details.
- Handles empty recipe collections.
- Available through menu option 6.
- GitHub Issue #2 and Pull Request #5.

### 3. Scale Recipes by Servings — Planned

- Adjust ingredient quantities based on the desired number of servings.
- Planned for the final submission.
- GitHub Issue #3.

## Current Application Menu

1. List all recipes
2. Search recipes by name
3. Filter recipes by category
4. View recipe details
5. Search recipes by ingredient
6. Random meal suggestion
7. Exit

## Checkpoint 1 Testing

All 17 pytest tests are currently passing:

- 7 original starter tests
- 6 ingredient search tests
- 4 random meal suggestion tests

Run all tests using:

```bash
python -m pytest -v
```

## Development Workflow

All three features were planned using GitHub Issues. The two completed features were developed on separate feature branches, tested using pytest, and merged into main through pull requests.

Implementation and testing changes were committed separately to maintain a clear development history.

## Remaining Work

- Implement recipe scaling by servings.
- Add automated tests for recipe scaling.
- Configure Docker.
- Set up continuous integration using GitHub Actions.
- Review security and privacy practices.
- Complete final documentation and reflection.