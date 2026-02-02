from abc import ABC, abstractmethod

class Policy():
    '''
    Handles the decision logic of policies and 
    embodies how political players might act at the tournament.

    This is an abstract class, which just defines how other 
    Policies should be implemented.

    Attributes:
        name: The name of the policy.
    '''

    @abstractmethod
    def decision(self, my_history, opponent_history) -> int:
        '''
        Handles what a policy will return based on previous actions 
        in the match.

        Parameters:
            my_history: All of this Policy's previous actions.
            opponent_history: All of the opponent Policy's 
            previous actions.

        Returns:
            (int): 1 symbolises Cooporation, 0 symbolises Defection.
        '''
        pass


class TitForTat(Policy):
    def __init__(self):
        self.name = "Tit For Tat"
        
    def decision(self, my_history, opponent_history) -> int:

        # First action of the game.  
        if len(opponent_history) == 0:
            return 1

        # All other actions.  
        if opponent_history[-1] == 0:
            return 0
        else:
            return 1

class AlwaysCooporate(Policy):
    def __init__(self):
        self.name = "Always Cooporate"
    def decision(self, my_history, opponent_history) -> int:
        return 1
    
class AlwaysDefect(Policy):
    def __init__(self):
        self.name = "Always Defect"
    def decision(self, my_history, opponent_history) -> int:
        return 0

class TitFor2Tat(Policy):
    def __init__(self):
        self.name = "Tit For 2 Tat"
        
    def decision(self, my_history, opponent_history) -> int:

        # First action of the game.  
        if len(opponent_history) <2:
            return 1

        # All other actions.  
        if opponent_history[-1] and opponent_history[-2] == 0:
            return 0
        else:
            return 1
    
class Tournament():
    '''Handles the main logic of the tournament.     

    Attributes:
        policies ([Policy]): A list of Policy objects which play 
        matches against eachother.  
        scores ([int]): A list of scores matching the index of each 
        Policy from the policies list.
    '''

    def __init__(self, policies):
        '''Initialises the tournament's policies and scores lists to 
        hold data.'''
        self.policies = policies
        self.scores = [0 for i in range(len(self.policies))]
        self.ROUNDS = 10
        
    def names(self):
        '''A method to print the names of all competing Policy 
        objects.'''
        for policy in self.policies:
            print(policy.name)
            
    def match(self, p1, p2) -> list[int, int]:
        ''' A method to simulate 1 game where p1 and p2 will end with a score

        If Defect, Defect... both p1 and p2 get 1 point
        If Defect, Cooporate ... p1 gets 5 points only
        If Cooporate, Defect ... p2 gets 5 points only
        If Cooporate, Cooporate ... p1 and p3 get 3 points each

        Parameters:
            p1 (Policy): A policy player.
            p2 (Policy): Another policy player.

        Returns:
            ([Int, Int]): A size 2 list of the p1 score and p2 score.
        '''
        
        p1_history = []
        p2_history = []
        
        p1_score = 0
        p2_score = 0
        
        for i in range(self.ROUNDS):
            
            p1_action = p1.decision(p1_history, p2_history)
            p2_action = p2.decision(p2_history, p1_history)
            actions = (p1_action, p2_action)

            match actions:
                case(1,1):
                    p1_score += 3
                    p2_score += 3
                    p1_history.append(1)
                    p2_history.append(1)
                case(1,0):
                    p1_score += 0
                    p2_score += 5
                    p1_history.append(1)
                    p2_history.append(0)
                case(0,1):
                    p1_score += 5
                    p2_score += 0
                    p1_history.append(0)
                    p2_history.append(1)
                case(0,0):    
                    p1_score += 1
                    p2_score += 1
                    p1_history.append(0)
                    p2_history.append(0)
                    
        return [p1_score, p2_score]
                
    def run(self) -> list[(Policy, int)]:
        '''Method defining the tournament setup and the ordering of matches
        
        Returns:
            ([(Policy, int)]): a list of tuples where the tuple is the zipped Policy and its score.
        '''

        for i in range(len(self.policies)):   # PLAYER index
            for y in range(i, len(self.policies)):   # OPPONENT index
                
                #Simulate the Match
                score = self.match(self.policies[i], self.policies[y])
                self.scores[i] += score[0]
                self.scores[y] += score[1]
                
                
        return list(zip(self.policies, self.scores))

tit_for_tat = TitForTat()   # creating a TitForTat policy
always_accept = AlwaysCooporate() 
always_defect = AlwaysDefect()
always_defect2 = AlwaysDefect()
always_defect3 = AlwaysDefect()
tit_for_tat2 = TitForTat()  
tit_for_tat3 = TitForTat()   

tournament = Tournament([tit_for_tat, 
                          always_accept, 
                          always_defect,
                          tit_for_tat2,
                          tit_for_tat3,
                          always_defect2,
                          always_defect3])  

policies_with_results = tournament.run()
print(policies_with_results)