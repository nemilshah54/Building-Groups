
class Groupp(object):
    total = 0  # class variable for total people

    def __init__(self, id = None):
        Groupp.total = Groupp.total + 1
        self.id = id
        if self.id is None:          # If id is not passed, then id is the number of Group objects.
            self.id = Groupp.total   # id instance

        self.listPerson = []            # List instance. List of person objects.

    def addPerson(self, person):
        self.listPerson.append ( person)

    def validate(self):

        for iter in self.listPerson:
            checklist = [ "ID", "First Name", "Last Name" ]
            iter.validate( checklist)
        length =  len( self.listPerson)
        if length  <3:
            print("Group %d has %d people, less than three" % ( self.id,   length ))
        elif length  >5:
            print("Group %d has %d people, more than five" % ( self.id,  length ))


    def iteratePeople (self, flag):
        x=0
        for p in self.listPerson:
            if flag ==1:
                x= x+1
                print ( x, end="")
                print( " " + p.attributes["First Name"] + " " + p.attributes["Last Name"])
            if flag ==0:
                print(" " + p.attributes["First Name"] + " " + p.attributes["Last Name"])


    def remove(self, i):
        return self.listPerson.pop(i)

    def add(self, p, i):
        self.listPerson.insert ( p,i)



