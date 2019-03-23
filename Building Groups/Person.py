
class Personn(object):
    total =0   # class variable for total people

    def __init__(self, id= None, first_name = None, last_name = None,  attributes = None):    # Fix me.
        Personn.total =  Personn.total + 1
        self.id = id
        if self.id is None:             # If id is not passed, then id is the number of Person objects.
            self.id = Personn.total
        self.firstName = first_name
        self.lastName = last_name
        self.attributes = attributes

        if self.attributes is None:
            self.attributes = {"First Name": self.firstName, "Last Name":  self.lastName, "ID": self.id, "GroupNum": None}

        self.attributes["ID"] = self.id

    def validate(self, checkList):
        for iter in checkList:
            if self.attributes [iter] is None:
                print ( "Person  %d does not have " % self.id + iter +"." )





