import abc

class User(object):
    def __init__(self):
        self.id = None
        self.name = None

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

class Group(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.members = []

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getMembers(self):
        return self.members
    def setMembers(self, members):
        self.members = members

class Bill(object):
    def __init__(self):
        self.desc = None
        self.amount = None
        self.groupId = None
        self.contribution = {}
        self.paidBy = {}

    def getDesc(self):
        return self.desc
    def setDesc(self, desc):
        self.desc = desc
    def getAmount(self):
        return self.amount
    def setAmount(self, amount):
        self.amount = amount
    def getGroupId(self):
        return self.groupId
    def setGroupId(self, groupId):
        self.groupId = groupId
    def getContribution(self):
        return self.contribution
    def setContribution(self, contribution):
        self.contribution = contribution
    def getPaidBy(self):
        return self.paidBy
    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

AllBills = {}
def addBill(desc, amount, groupId, contribution, paidBy):
    totalContributions = 0
    for user in contribution:
        totalContributions = totalContributions + contribution[user]
    totalPaid = 0
    for user in paidBy:
        totalPaid = totalPaid + paidBy[user]
    if(totalContributions != totalPaid):
        print("Invalid Bill")
    else:
        bill = Bill()
        bill.setDesc(desc)
        bill.setAmount(amount)
        bill.setGroupId(groupId)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        AllBills[desc] = bill

class Bill_Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBill(desc, amount, groupId, contribution, paidBy):
        pass
    def groupUserBalance(userId, groupId):
        pass
    def FinalUserBalance(self, userId):
        pass

class Bill_Service(Bill_Interface):
    AllBills = {}

    def addBill(self, desc, amount, groupId, contribution, paidBy):
        totalContributions = 0
        for user in contribution:
            totalContributions = totalContributions + contribution[user]
        totalPaid = 0
        for user in paidBy:
            totalPaid = totalPaid + paidBy[user]
        if(totalContributions != totalPaid):
            print("Invalid Bill")
            return None
        else:
            bill = Bill()
            bill.setDesc(desc)
            bill.setAmount(amount)
            bill.setGroupId(groupId)
            bill.setContribution(contribution)
            bill.setPaidBy(paidBy)
            self.__class__.AllBills[desc] = bill
            return bill

    def groupUserBalance(self, userId, groupId):
        balance = 0
        for billDesc in self.__class__.AllBills:
            bill = self.__class__.AllBills[billDesc]
            if(bill.getGroupId() == groupId):
                if userId in bill.getContribution():
                    balance = balance - bill.getContribution().get(userId)
                if userId in bill.getPaidBy():
                    balance = balance + bill.getPaidBy().get(userId)
        return str(groupId) +  " balance for user " + str(userId) + " is " + str(balance)

    def FinalUserBalance(self, userId):
        balance = 0
        for billDesc in self.__class__.AllBills:
            bill = self.__class__.AllBills[billDesc]
            if userId in bill.getContribution():
                balance = balance - bill.getContribution().get(userId)
            if userId in bill.getPaidBy():
                balance = balance + bill.getPaidBy().get(userId)
        return "Overall balance for " + str(userId) + " is " + str(balance)

AllGroups = {}
def addGroup(id, name, members):
    group = Group()
    group.setId(id)
    group.setName(name)
    group.setMembers(members)
    AllGroups[id] = group
    return group

AllUsers = {}
def addUser(id, name):
    user = User()
    user.setId(id)
    user.setName(name)
    AllUsers[id] = user
    return user

addUser("person1@xyz.com","person1")
addUser("person2@xyz.com","person2")
addUser("person3@xyz.com","person3")

addGroup("group1", "Group 1", ["person1@xyz.com", "person2@xyz.com"])
addGroup("group2", "Group 2", ["person2@xyz.com", "person3@xyz.com"])

bill_service = Bill_Service()
#bill_service.addBill("Bill 1", 300, "group1",{"person1@xyz.com" : 100, "person2@xyz.com" : 200}, {"person1@xyz.com" : 300})
#bill_service.addBill("Bill 2",500,"group1",{"person1@xyz.com" : 250, "person2@xyz.com" : 250}, {"person2@xyz.com" : 500})
#bill_service.addBill("Bill 3",100,"group2",{"person2@xyz.com" : 10, "person3@xyz.com" : 90}, {"person3@xyz.com" : 100})
#bill_service.addBill("Bill 4",300,"group2",{"person2@xyz.com" : 150, "person3@xyz.com" : 150}, {"person3@xyz.com" : 400, "person2@xyz.com" : -100})
#bill_service.addBill("Bill 5",300,"group2",{"person2@xyz.com" : 150, "person3@xyz.com" : 150}, {"person3@xyz.com" : 100, "person2@xyz.com" : 100})

print(bill_service.FinalUserBalance("person1@xyz.com"))
print(bill_service.FinalUserBalance("person2@xyz.com"))
print(bill_service.FinalUserBalance("person3@xyz.com"))

# print(bill_service.groupUserBalance("person1@xyz.com", "group1"))
# print(bill_service.groupUserBalance("person2@xyz.com", "group1"))
# print(bill_service.groupUserBalance("person2@xyz.com", "group2"))
# print(bill_service.groupUserBalance("person3@xyz.com", "group2"))







