

import Person
import Group

list = []                      # list for person objects.
listGroup = []                 # list for  group objects.

prompt = input("Choose an option: \n")
userInput = int(prompt)

print(userInput)

# Loop to run the application.
while userInput != -1:
    if userInput == 0:
        print("On -1, end the loop.")
        print("On 0, output what each number does")
        print("On 1, create a new Person.  Ask for the first and last name.")
        print("On 2, create a new group, populated by existing Person objects.  Loop while outputting the names of people")
        print("who have not been assigned to a group and ask for the ids of the people to add.")
        print("On 3, allow the user to modify an existing group.  Ask the user which group they wish to modify.  Then ask")
        print("whether they are trying to add or remove members to/from the group.  Then, interactively allow the user to add")
        print("or remove as many users as they want by offering a list of available choices and having the user select which")
        print("member to interact with.")
        print("On 4, validate all existing groups, as well as all people to check that they have a group.")
        print("On 5, output each group’s number and members.\n")

    elif userInput == 1:
        # Create a new Person
        fn = input("What is the person's first name?\n" )
        ln =  input ("What is the person's last name?\n" )
        D = dict ()
        D = { "First Name": fn,   "Last Name": ln, "ID": None, "GroupNum": None  }
        p1 = Person.Personn(first_name=fn, last_name=ln, attributes=D)
        list.append(p1)
        # D = {"First Name": None, "Last Name": None, "ID": None, "GroupNum": None}
        #  p1 = Person.Personn()                     # Test for all type of constructors....
        #  p1 = Person.Personn( first_name= fn, last_name= ln)
        #  P1 = Person.Personn( attributes)
        # p1  = Person.Personn( attributes = D )
        # checklist = [ "ID", "First Name", "Last Name" , "GroupNum"]
        #p2.validate( checklist)

    elif userInput == 2:
        # Create a group
        g1 = Group.Groupp()

        # Populate all existing person objects.
        for person in list:
            if (person.attributes["GroupNum"] is None):
                print ( person.attributes["ID"] ,end="")
                print( " " +person.attributes["First Name"] + " " +person.attributes["Last Name"] )

        # Loop to add person to the groups.
        prompt = input("Which person would you like to add to the new group? (-1 to finish adding people) : \n")
        add = int(prompt)

        while  add != -1:
            p =list[add-1]
            g1.addPerson(p)
            p.attributes ["GroupNum"] = g1.id     # Assigning a person with group id.

            for person in list:
                if( person.attributes["GroupNum"] is None):
                    print (person.attributes["ID"], end="")
                    print(" " + person.attributes["First Name"] + " " + person.attributes["Last Name"])

            prompt = input("Which person would you like to add to the new group? (-1 to finish adding people) : \n")
            add = int(prompt)

        listGroup.append (g1)

    elif userInput == 3:
        prompt = input("Which group would you like to modify?\n")
        groupnumber = int (prompt)
        g = listGroup[groupnumber - 1]  # Add or remove from this group

        prompt = input ("Would you like to ADD or REMOVE members? \n")

        if prompt == "REMOVE":
            g.iteratePeople(1)                     # Avaialalbe choices to remove people from this group.
            choose = input ("Which person would you like to remove from the group? (-1 to finish remove people)\n")
            number = int ( choose)

            while  number!= -1:
                p = g.remove ( number-1)
                p.attributes["GroupNum"] = None   # Set to None again. since it can be used again now.

                g.iteratePeople(1)  # Avaialalbe choices to remove people from this group.
                choose = input("Which person would you like to remove from the group? (-1 to finish remove people)\n")
                number = int(choose)

        if prompt == "ADD":
            # Add only those people who are not assigned to the group
            for person in list:
                if( person.attributes["GroupNum"] is None):
                    print (person.attributes["ID"], end="")
                    print(" " + person.attributes["First Name"] + " " + person.attributes["Last Name"])

            choose = input("Which person would you like to add to the new group? (-1 to finish adding people)\n")
            number = int(choose)

            while number!= -1:
                p = list [ number-1]
                g.add ( number-1, p)
                p.attributes["GroupNum"] = g1.id  # Assigning a person with group id.

                # Add only those people who are not assigned to the group
                for person in list:
                    if (person.attributes["GroupNum"] is None):
                        print (person.attributes["ID"], end="")
                        print(" " + person.attributes["First Name"] + " " + person.attributes["Last Name"])

                choose = input("Which person would you like to add to the new group? (-1 to finish adding people)\n")
                number = int(choose)


    elif userInput == 4:

        # Validate for each person object to see if they have a valid group or not.
        for person in list:
            if (person.attributes["GroupNum"] is None):
                print( person.attributes["First Name"] + " " + person.attributes["Last Name"] + " does not have an assigned group")

        # Validate the group.
        for group in listGroup:
            group.validate()

    elif userInput == 5:

        for group in listGroup:
            print ( "Group is %d" % group.id)
            group.iteratePeople(0)
    else:
        print("This is not a valid choice. Press 0 and please see the options again.")

    prompt = input("Choose an option: \n")
    userInput = int(prompt)

print ("Goodbye!")

