def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.
    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]
    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    n = len(cols)
    listu = []
    if n == 0:
      print(entity)
    else:
      for i in range (0, n):
        k = cols[i]
        listu.append(entity[k])
      print(listu)
    
    


<<<<<<< HEAD
list_entity(['Earth', 'TRUE', 9.8], cols=[0,2])
=======
list_entity(['Earth', "TRUE", 9.8], cols=[0,2])
>>>>>>> 2b9ed70cfc533c749c9085e5b27face93129f965
