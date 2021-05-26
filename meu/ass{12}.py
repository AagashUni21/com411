def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.
    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.
    You will need to add the parameter categories to the function definition.
    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    print(categories)

list_categories({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
})