
class titForTat():
    def __init__(self):
        self.name = "TitForTat"
    def decision(self, myHistory, opponentHistory):

        # history will be a list of what each player has done in a match
        if len(opponentHistory) == 0:
            return 1

        # if opponent rejected
            # then reject        
        elif opponentHistory[-1] == 0:
            return 0
        # else
            # then accept
        else:
            return 1

class alwaysCooporate():
    def __init__(self):
        self.name = "AlwaysCooporate"
    def decision(self, myHistory, opponentHistory):
        return 1
    
class alwaysDefect():
    def __init__(self):
        self.name = "AlwaysDefect"
    def decision(self, myHistory, opponentHistory):
        return 0
    
    

# 1 for accept 
# 0 for reject

class tournament():
    def __init__(self, policies):
        self.policies = policies
        self.scores = [0 for i in range(len(self.policies))]
        
    def names(self):
        for policy in self.policies:
            print(policy.name)
            
    def match(self, p1, p2):
        # Simulate 1 game where p1 and p2 will end with a score
        # If Defect, Defect... both p1 and p2 get 1 point
        # If Defect, Cooporate ... p1 gets 5 points only
        # If Cooporate, Defect ... p2 gets 5 points only
        # If Cooporate, Cooporate ... p1 and p3 get 3 points each
        
        p1History = []
        p2History = []
        
        p1Score = 0
        p2Score = 0
        
        for i in range(10):
            
            x = p1.decision(p1History, p2History)
            y = p2. decision(p2History, p1History)
            
            if (x == 1 and y == 1):
                p1Score += 3
                p2Score += 3
                p1History.append(1)
                p2History.append(1)
            elif (x == 1 and y == 0):
                p1Score += 0
                p2Score += 5
                p1History.append(1)
                p2History.append(0)
            elif (x == 0 and y == 1):
                p1Score += 0
                p2Score += 5
                p1History.append(0)
                p2History.append(1)
            else:
                p1Score += 1
                p2Score += 1
                p1History.append(0)
                p2History.append(0)
                
        return [p1Score, p2Score]
                
    def run(self):
        
        # need to create a loop where a policy is matched against every other policy, and scores are added
        for i in range(len(self.policies)):  # PLAYER
            for y in range(i, len(self.policies)): # OPPONENT
                
                #Simulate the Match
                score = self.match(self.policies[i], self.policies[y])
                self.scores[i] += score[0]
                self.scores[y] += score[1]
                
                
        return zip(self.policies, self.scores)

titfortat = titForTat()   # creating a titfortat policy
alwaysAccept = alwaysCooporate() # creating a alwaysaccept policy
alwaysDefect = alwaysDefect()
t = tournament( [titfortat, alwaysAccept, alwaysDefect] )  #create the tournament.
results = t.run()
print(list(results))