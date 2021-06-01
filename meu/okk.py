import matplotlib.pyplot as plt

def overlapped():
    x = [1, 1, 3, 3, 1]
    y = [1, 3, 3, 1, 1]
    #we are assigning the point give by the text. use 5th point to #make sure squares connect back to starting point: we need 5 #points to draw 4 lines. where the fifth one has the same #coordinate as the starting point
    x2 = [2, 2, 4, 4, 2]
    y2 = [2, 4, 4, 2, 2]
    ##same mechanism as above
    x3 = [3, 3, 5, 5, 3]
    y3 = [3, 5, 5, 3, 3]
    #same mechanism as above
    plt.plot(x, y, "m:p") #We can control various aspects of the #plot including the shape, size and colour:thus we use the #letters and symbols (predefined ones) to follow the test #request
    plt.plot(x2, y2, "c--h")#same mechanism as above
    plt.plot(x3, y3, "y-.d")#as above.
    plt.show()

#overlapped()

def individual():


  fig, ax = plt.subplots(1, 3)
  x = [1, 1, 3, 3, 1]
  y = [1, 3, 3, 1, 1] #we are assigning the point give by the text. #use 5th point to make sure squares connect back to starting point: #we need 5 points to draw 4 lines. where the fifth one has the same #coordinate as the starting point
  ax[0].set_xlim(0.2,5.2)
  ax[0].set_ylim(0.2,5.3)

  x2 = [2, 2, 4, 4, 2]
  y2 = [2, 4, 4, 2, 2]#same as above
  ax[1].set_xlim(0.2, 5.2)
  ax[1].set_ylim(0.2, 5.3)

  x3 = [3, 3, 5, 5, 3]
  y3 = [3, 5, 5, 3, 3]#same as above
  ax[2].set_xlim(0.2, 5.2)
  ax[2].set_ylim(0.2, 5.3)

  ax[0].plot(x, y, "m:p") #We can control various aspects of the plot #including the shape, size and colour:thus we use the letters and #symbols (predefined ones) to follow the test #request
  ax[1].plot(x2, y2, "c--h")#same as above
  ax[2].plot(x3, y3, "y-.d")#same as above

  plt.show()

individual()

