import matplotlib.pyplot as plt

def combined():
    x = [3, 5, 7, 3]
    y = [3, 5, 3, 3]
    #we are assigning the point give by the text. use 4th point to #make sure triangles connect back to starting point: we need 4 #points to draw 3 lines. where the third one has the same #coordinate as the starting point
    x2 = [3, 5, 7, 3]
    y2 = [5, 3, 5, 5]
    ##same mechanism as above
    x3 = [3, 3, 7, 3]
    y3 = [3, 5, 4, 3]
    #same mechanism as above
    x4 = [7, 7, 3, 7]
    y4 = [3, 5, 4, 3]
    #same mechanism as above
    plt.plot(x, y, "r--o") #We can control various aspects of the #plot including the shape, size and colour:thus we use the #letters and symbols (predefined ones) to follow the test #request
    plt.plot(x2, y2, "b:s")#same mechanism as above
    plt.plot(x3, y3, "g-.*")#as above.
    plt.plot(x4, y4, "y-p")#as above.
    plt.show()#starts an event loop, looks for all currently active #figure objects, and opens one or more interactive windows that #display your figure or figures

#combined()

def seperated():


  fig, ax = plt.subplots(2, 2, sharex="all", sharey="all")
  #sharex and sharey share subplot column and rows

  x = [3, 5, 7, 3]
  y = [3, 5, 3, 3] #we are assigning the point give by the text. #use 4th point to make sure triangles connect back to starting #point: we need 4 points to draw 3 lines. where the third one #has the same coordinate as the starting point
  

  x2 = [3, 5, 7, 3]
  y2 = [5, 3, 5, 5]#same as above
  

  x3 = [3, 3, 7, 3]
  y3 = [3, 5, 4, 3]#same as above

  x4 = [7, 7, 3, 7]
  y4 = [3, 5, 4, 3]
  #same mechanism as above
  

  ax[0,0].plot(x, y, "r--o") #We can control various aspects of the #plot including the shape, size and colour:thus we use the #letters and symbols (predefined ones) to follow the test request
  ax[0,1].plot(x2, y2, "b:s")#same as above
  ax[1,0].plot(x3, y3, "g-.*")#same as above
  ax[1,1].plot(x4, y4, "y-p")#same as above
  plt.show()#starts an event loop, looks for all currently active #figure objects, and opens one or more interactive windows that #display your figure or figures

#seperated()

def data():
  dictionu = {"tr1": [[3, 5, 7, 3], [3, 5, 3, 3], format],
             "tr2": [[3, 5, 7, 3], [5, 3, 5, 5], format],
             "tr3": [[3, 3, 7, 3], [3, 5, 4, 3], format],
              "tr4": [[7, 7, 3, 7], [3, 5, 4, 3], format]
  }
  #we are creating dictionary named dictionu as text suggested with 
  #same indexes as individual
  return dictionu


def improve_seperated():
  fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
  ##sharex and sharey share subplot column and rows
  dictionu = data()#calling dictionu
  x = dictionu.get("tr1")[0]
  y = dictionu.get("tr1")[1]#assigning left figure x and y labels

  x2 = dictionu.get("tr2")[0]
  y2 = dictionu.get("tr2")[1]##assigning middle figure x and y #labels

  x3 = dictionu.get("tr3")[0]
  y3 = dictionu.get("tr3")[1]#assigning right figure x and y labels

  
  x4 = dictionu.get("tr4")[0]
  y4 = dictionu.get("tr4")[1]#assigning right figure x and y labels

  ax[0,0].plot(x, y, "r--o") #We can control various aspects of the #plot including the shape, size and colour:thus we use the #letters and symbols (predefined ones) to follow the test request
  ax[0,1].plot(x2, y2, "b:s")#same as above
  ax[1,0].plot(x3, y3, "g-.*")#same as above
  ax[1,1].plot(x4, y4, "y-p")#same as above
  plt.show()#starts an event loop, looks for all currently active #figure objects, and opens one or more interactive windows that #display your figure or figures

#improve_seperated()