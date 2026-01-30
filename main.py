
class titForTat():
    def __init__(self):
        self.name = "TitForTat"
    def decision(self, history):

        # history will be a list of what 

        # if opponent rejected
            # then reject
        # else
            # then accept
            
        return 0

class alwaysAccept():
    def __init__(self):
        self.name = "AlwaysAccept"
    def decision():
        return 1

# 1 for accept 
# 0 for reject

class match():
    def __init__(self, p1, p2):
        p1 = p1
        p2 = p2
    def play():
        return 0
    

class tournament():
    def __init__(self, policies):
        self.policies = policies

    def run(self):
        for policy in self.policies:
            print(policy.name)


titfortat = titForTat()   # creating a titfortat policy
alwaysAccept = alwaysAccept() # creating a alwaysaccept policy
t = tournament( [titfortat, alwaysAccept] )  #create the tournament.
t.run()
