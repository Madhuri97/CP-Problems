"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
        self.c = 0
    
    def classiness(self):
        return self.c

    def addItem(self, s):
        if s == "tophat":
            self.c += 2
        elif s == "bowtie":
            self.c += 4
        elif s == "monocle":
            self.c += 5
        else:
            self.c += 0
        return self.c

