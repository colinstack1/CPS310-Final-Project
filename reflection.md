# CPS 310 Final Project — Checkpoint 1 Reflection

## 1. Feature Selection

**Recipe Management:** Search by Ingredient

**Meal Planning:** Random Meal Suggestion

**Grocery / Calculations:** Scale Recipes by Servings

**Response:**

I chose these three features because they would make the Recipe & Meal Planner more useful. Searching by ingredient allows users to find recipes based on ingredients they already have. Random meal suggestions help users decide what to make when they are unsure. Scaling recipes by servings will allow users to adjust ingredient amounts based on how many people they are cooking for.

I also chose these features because they can be developed and tested separately.

## 2. Current Progress

**Response:**

I have completed Search by Ingredient and Random Meal Suggestion.

The ingredient search allows users to enter an ingredient and find matching recipes. It supports partial matches, different capitalization, and extra spaces. It also handles empty searches and searches with no matching recipes.

The random meal suggestion selects a recipe from the available collection and displays its details, including ingredients, servings, and cooking times. It also handles an empty recipe collection.

Both features are available through the application menu and have been merged into the main branch.

## 3. Most Difficult Feature

**Response:**

Search by Ingredient was the more challenging of the two features implemented so far. Unlike searching by recipe name, searching by ingredient requires looking through a list of ingredients inside each recipe.

I also needed to consider partial matches, capitalization, extra spaces, and empty searches. Connecting the function to the application menu and testing these different situations required more work than the random meal suggestion feature.

## 4. GitHub Issues

**Response:**

I created the following GitHub Issues:

- Issue #1: Implement Search by Ingredient
- Issue #2: Implement Random Meal Suggestion
- Issue #3: Implement Recipe Scaling by Servings

The Issues helped me organize the project by separating the three features into individual tasks. Issues #1 and #2 were linked to their pull requests. Issue #3 represents the remaining feature that I plan to complete before the final submission.

## 5. Branch / Pull Request

**Response:**

The branch feature/ingredient-search and Pull Request #4 best represent my development process so far.

On this branch, I implemented the ingredient search function, connected it to the application menu, and added six automated tests. I committed the implementation and tests separately before pushing the branch to GitHub.

This work belonged outside main because I wanted to develop and test the feature without affecting the stable version of the application. After all 13 tests passed and I manually verified the feature, I merged the pull request into main.

## 6. Meaningful Commit

**Response:**

One meaningful commit was 176aa3d, titled "Implement ingredient search and integrate menu option."

This commit added the ingredient search function to recipe_utils.py and connected it to the application menu in app.py.

It was useful to keep these changes together because they represent the complete implementation of one feature. The automated tests were added in a separate commit, 7ef771e, which makes the development history easier to understand.

## 7. Testing

**Response:**

I started with seven existing pytest tests and added ten new tests.

The six ingredient search tests verify:

- Finding recipes containing a specific ingredient
- Partial ingredient matching
- Case-insensitive matching
- Searches with no matching recipes
- Empty searches
- Searches containing extra spaces

The four random meal suggestion tests verify:

- Returning a valid recipe from the collection
- Handling an empty recipe collection
- Handling a collection with only one recipe
- Preserving the original recipe collection

All 17 tests passed during my final verification on the main branch. I also manually tested both features through the application menu.

## 8. Bug or Mistake

**Response:**

One mistake I encountered was using the wrong GitHub username when connecting my local repository to GitHub.

I discovered the problem when I attempted to push my initial commit and received a "Repository not found" error.

I checked the correct repository URL and used git remote set-url origin to update the connection. After correcting the URL, I successfully pushed my code.

This taught me to verify repository URLs when troubleshooting Git connection errors.

## 9. Current Code Quality

**Response:**

One part of the code I would improve is input validation in the ingredient search function.

The current function assumes that each recipe contains an ingredients list and that every ingredient contains a valid name. If recipe data is missing or incorrectly formatted, the application could encounter an error.

I would improve this by adding validation and additional tests for incomplete or invalid recipe data. This would make the application more reliable.

## 10. Remaining Plan

**Response:**

Before the final submission, I still need to:

- Implement Scale Recipes by Servings using GitHub Issue #3.
- Develop the feature on a separate branch.
- Add automated tests for recipe scaling and invalid serving inputs.
- Create and test a Dockerfile.
- Create an appropriate .dockerignore file.
- Configure GitHub Actions for continuous integration.
- Verify that automated tests pass through CI.
- Review the project for security and privacy concerns.
- Update the README with final setup and Docker instructions.
- Complete the final reflection.

My next step will be implementing recipe scaling. After that, I will focus on Docker, continuous integration, security, and final verification.