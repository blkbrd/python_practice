from anytree import Node, RenderTree
import re

with open('data') as file:
    info = file.readlines()
    [re.sub('\(', ',') for i in info]
    print (info)
