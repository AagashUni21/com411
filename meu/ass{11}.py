def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.
    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []
    You will need to add these parameters to the function definition.
    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.
    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    """lista = []
    list_small = []

    n = len(cols)
    if n == 0:
      print(entities)
    else:
      for i in range (0,n):
        x = entities[i]
        for j in range (0,n):
          k = cols[j]
          list_small.append(entities[k])
      print(list_small)
      print(lista)

list_entities([['earth', 9 , 8], ['ok', 5, 6], ['hell', 2, 45]], cols = [0,2])
    """

"""def list_entities(entities, cols=[]):
# TODO: Your code here
  listu = []
  o=len(cols)
  for i in entities:
      for j in range(0,o):
        lista = []
        k = cols[j]
        lista.append(i[k])
        listu.append(lista)

  print(listu)
list_entities([['earth', 9 , 8], ['ok', 5, 6], ['hell', 2, 45]], cols = [0,2])
"""
"""
def list_entities(entities, cols=[]):
# TODO: Your code here
  lista = []
  o=len(cols)
  for i in entities:
      for j in range(0,o):
        k = cols[j]
        lista.append(i[k])
  print(lista)
list_entities([['earth', 9 , 8], ['ok', 5, 6], ['hell', 2, 45]], cols = [0,2])
"""