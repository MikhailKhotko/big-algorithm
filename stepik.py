import random
firstline = [0,0,0]
secondline = [0,0,0]
thirdline = [0,0,0]
positionx = random.randint(1,3)
positiony = random.randint(1,3)
positionx2 = random.randint(1,3)
positiony2 = random.randint(1,3)
def positions():
  if positiony == 1:
    firstline[positionx-1] = 1
  if positiony == 2:
    secondline[positionx-1] = 1
  if positiony == 3:
    thirdline[positionx-1] = 1
  if positiony2 == 1:
    firstline[positionx-1] = 2
  if positiony2 == 2:
    secondline[positionx-1] = 2
  if positiony2 == 3:
    thirdline[positionx-1] = 2
  if positiony == positiony2:
    positions()
positions()
while True:
  active = True
  print(firstline)
  print(secondline)
  print(thirdline)
  move = str(input(""))
  if move == "w" and active == True:
    if 1 in firstline and active == True:
      if 2 in firstline and active == True:
        firstindex = firstline.index(2)
        secondline[firstindex] = 2
        firstline[firstindex] = 0
        active = False
      if 2 in secondline and active == True:
        secondindex = secondline.index(2)
        thirdline[secondindex] = 2
        secondline[secondindex] = 0
        active = False
      if 2 in thirdline and active == True:
        for i in range(3):
          thirdline[i] = secondline[i]
        active = False
    if 1 in secondline and active == True:
      secondindex = secondline.index(1)
      firstline[secondindex] = 1
      secondline[secondindex] = 0
      active = False
    if 1 in thirdline and active == True:
      thirdindex = thirdline.index(1)
      secondline[thirdindex] = 1
      thirdline[thirdindex] = 0
      active = False
  if move == "s" and active == True:
    if 1 in firstline and active == True:
      firstindex = firstline.index(1)
      secondline[firstindex] = 1
      firstline[firstindex] = 0
      active = False
    if 1 in secondline and active == True:
      secondindex = secondline.index(1)
      thirdline[secondindex] = 1
      secondline[secondindex] = 0
      active = False
    if 1 in thirdline and active == True:
      if 2 in thirdline and active == True:
        thirdindex = thirdline.index(2)
        thirdline[thirdindex] = 0
        secondline[thirdindex] = 2
        active = False
      if 2 in secondline and active == True:
        secondindex = secondline.index(2)
        secondline[secondindex] = 0
        firstline[secondindex] = 2
        active = False
      if 2 in firstline and active == True:
        for i in range(3):
          firstline[i] = secondline[i]
        active = False
  if move == "d" and active == True:
    if 1 in firstline and active == True:
      firstindex = firstline.index(1)
      if firstindex != 2 and active == True:
        firstline[firstindex+1] = 1
        firstline[firstindex] = 0
        active = False
      if firstindex == 2 and active == True:
        if 2 in secondline:
          secondindex = secondline.index(2)
          if secondindex != 0:
            secondline[secondindex-1] = 2
            secondline[secondindex] = 0
          if secondindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        if 2 in thirdline:
          thirdindex = thirdline.index(2)
          if thirdindex != 0:
            thirdline[thirdindex-1] = 2
            thirdline[thirdindex] = 0
          if thirdindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        active = False
    if 1 in secondline and active == True:
      secondindex = secondline.index(1)
      if secondindex != 2 and active == True:
        secondline[secondindex+1] = 1
        secondline[secondindex] = 0
        active = False
      if secondindex == 2 and active == True:
        if 2 in firstline:
          firstindex = firstline.index(2)
          if firstindex != 0:
            firstline[firstindex-1] = 2
            firstline[firstindex] = 0
          if firstindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        if 2 in thirdline:
          thirdindex = thirdline.index(2)
          if thirdindex != 0:
            thirdline[thirdindex-1] = 2
            thirdline[thirdindex] = 0
          if thirdindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        active = False
    if 1 in thirdline and active == True:
      thirdindex = thirdline.index(1)
      if thirdindex != 2 and active == True:
        thirdline[thirdindex+1] = 1
        thirdline[thirdindex] = 0
        active = False
      if thirdindex == 2 and active == True:
        if 2 in firstline:
          firstindex = firstline.index(2)
          if firstindex != 0:
            firstline[firstindex-1] = 2
            firstline[firstindex] = 0
          if firstindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        if 2 in secondline:
          secondindex = secondline.index(2)
          if secondindex != 0:
            secondline[secondindex-1] = 2
            secondline[secondindex] = 0
          if secondindex == 0:
            firstline[0] = firstline[1]
            secondline[0] = secondline[1]
            thirdline[0] = thirdline[1]
        active = False
  if move == "a" and active == True:
    if 1 in firstline and active == True:
      firstindex = firstline.index(1)
      if firstindex != 0 and active == True:
        firstline[firstline.index(1)-1] = 1
        firstline[firstindex] = 0
        active = False
      if firstindex == 0 and active == True:
        if 2 in secondline and active == True:
          if secondline.index(2) == 0 or secondline.index(2) == 1:
            secondindex = secondline.index(2)
            secondline[secondindex] = 0
            secondline[secondindex+1] = 2
            active = False
        if 2 in thirdline and active == True:
          if thirdline.index(2) == 0 or thirdline.index(2) == 1:
            thirdindex = thirdline.index(2)
            thirdline[thirdindex] = 0
            thirdline[thirdindex+1] = 2
            active = False
    if 1 in secondline and active == True:
      secondindex = secondline.index(1)
      if secondindex != 0 and active == True:
        secondline[secondline.index(1)-1] = 1
        secondline[secondindex] = 0
        active = False
      #if secondindex == 0 and active == True:
        #if firstline.index(2) == 0 or
    if 1 in thirdline and active == True:
      thirdindex = thirdline.index(1)
      thirdline[thirdline.index(1)-1] = 1
      thirdline[thirdindex] = 0
      active = False
