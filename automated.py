import random
numlist=[]
copyforx = []
def createmap():
  global size_y, size_x
  size_x=int(input())
  size_y=int(input())
  for i in range(size_y):
    numlist.append(size_x*".".split())
createmap()
def printmap():
  for i in range(size_y): #print of all field
    print(numlist[i])
numlist[2][2]="@"
printmap()
