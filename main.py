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


  fig, ax = plt.subplots(1, 3, sharex="all", sharey="all")
  #sharex and sharey:When subplots have a shared x-axis along a #column, only the x tick labels of the bottom subplot are #created. Similarly, when subplots have a shared y-axis along a #row, only the y tick labels of the first column subplot are #created.

  x = [1, 1, 3, 3, 1]
  y = [1, 3, 3, 1, 1] #we are assigning the point give by the text. #use 5th point to make sure squares connect back to starting #point: we need 5 points to draw 4 lines. where the fifth one has # same coordinate as the starting point
  

  x2 = [2, 2, 4, 4, 2]
  y2 = [2, 4, 4, 2, 2]#same as above
  

  x3 = [3, 3, 5, 5, 3]
  y3 = [3, 5, 5, 3, 3]#same as above
  

  ax[0].plot(x, y, "m:p") #We can control various aspects of the #plot including the shape, size and colour:thus we use the #letters and symbols (predefined ones) to follow the test request
  ax[1].plot(x2, y2, "c--h")#same as above
  ax[2].plot(x3, y3, "y-.d")#same as above

  plt.show()

#individual()

def info():
  dictionu = {"left": [[1, 1, 3, 3, 1], [1, 3, 3, 1, 1], format],
            "middle": [[2, 2, 4, 4, 2], [2, 4, 4, 2, 2], format],
            "right": [[3, 3, 5, 5, 3], [3, 5, 5, 3, 3], format]
            }
  return dictionu


def individual_using_info():
    fig, ax = plt.subplots(1, 3, sharex=True, sharey=True)
    dictionu = info()
    x = dictionu.get("left")[0]
    y = dictionu.get("left")[1]

    x2 = dictionu.get("middle")[0]
    y2 = dictionu.get("middle")[1]

    x3 = dictionu.get("right")[0]
    y3 = dictionu.get("right")[1]

    ax[0].plot(x, y, ":mp")
    ax[1].plot(x2, y2, "--ch")
    ax[2].plot(x3, y3, "-.yd")

    plt.show()

individual_using_info()