import random
import copy

class Board:
## class with all the board characteristic functions   
    def __init__(self,n):
        ## initializing board with random values
        self.n = n
        self.square = []
        self.h_score = 0
        for i in range(0,n):
            temp = []    
            for j in range(0,n):
                temp.append("-")
            self.square.append(temp)
        for i in range(0,n):
            random_row = random.randint(0,n-1)
            random_col = i
            if self.square[random_row][random_col] == "-":
                self.square[random_row][random_col] = "Q"
    
    def print_curr_state(self):
        ## function to print current board state
        rows = [" ".join(self.square[i]) for i in range(0, self.n)]
        print( "\n".join(rows))
        print(" ")
    
    def get_q_col_pos(self, row_no):
        ## funtion which gives column number of queen w.r.t row 
        for i in range(0, self.n):
            if self.square[row_no][i] == "Q":
                return i
        return -1
    def get_q_row_pos(self, col_no):
        ## function which gives row number of queen w.r.t column
        for i in range(0, self.n):
            if self.square[i][col_no] == "Q":
                return i
        return -1
    def get_h_score(self):
        ## function to calculate heuristic value of given board
        h_score = 0
        for col in range(0,self.n-1):
            q_row_pos = self.get_q_row_pos(col)
            for row in range(col+1,self.n):
                i = self.get_q_row_pos(row)
                j = self.get_q_row_pos(col)
                if self.square[q_row_pos][row] == "Q":
                    h_score+=1
                offset = abs(col - row)
                if i!=-1 and j!=-1:
                    if abs(i-j)==offset:
                        h_score+=1
        return h_score
    
    def get_min_list(self):
        ## function to calculate minimum heuristic value list
        min_h_score = self.get_h_score()
        min_list = []
        for col in range(0,self.n):
            q_row_pos = self.get_q_row_pos(col)
            for row in range(0,self.n):
                if self.square[row][col] != "Q":
                    new_board = copy.deepcopy(self)
                    new_board.square[q_row_pos][col] = "-"
                    new_board.square[row][col] = "Q"
                    cost = new_board.get_h_score()
                    if cost < min_h_score:
                        min_list=[]
                        min_h_score = cost
                        min_list.append([row,col])
                    elif cost == min_h_score:
                        min_list.append([row,col])
        return min_h_score,min_list
    
class Solve:
## class which solves nqueen using Hill Climbing and its variants
    def __init__(self, n):
        self.n = n
    
    def hill_climbing_Steepest_Ascent(self):
    ## function to calculate hill climbing steepest ascent
        no_of_success = no_of_failure = success_steps = failure_steps = 0
        
        for i in range(0,500):
            
            random_board = Board(self.n)
            h_score = random_board.get_h_score()
            moves = 0
            if (i<4):
                print("Random Configuration: ",i+1)
                steps = 0
            
            while True:
                
                if (i<4):
                    random_board.print_curr_state()
                    steps+=1
                if (h_score == 0):
                    break
                else:
                    moves+=1
                    min_h_score,min_list = random_board.get_min_list()
                    if (min_h_score >= h_score) or (len(min_list)==0):
                        break
                    else:
                        random_select = random.randint(0,len(min_list)-1)
                        rand_row, rand_col = min_list[random_select]
                        h_score = min_h_score
                        for j in range(0,self.n):
                            random_board.square[j][rand_col]= "-"
                        random_board.square[rand_row][rand_col]="Q"
                
            if(h_score==0):
                no_of_success+=1
                success_steps+=moves
                if(i<4):
                    print("================SUCCESS==================")
            else:
                no_of_failure+=1
                failure_steps+=moves
                if(i<4):
                    print("================FAILURE==================")
        total = no_of_success + no_of_failure
        rate_of_success = (no_of_success/total)*100
        rate_of_failure = (no_of_failure/total)*100
        print("Rate of success: ",round(rate_of_success,2),"% and Rate of failure is:",round(rate_of_failure,2),"%")

        if(no_of_success !=0):
            print("Average success rate: ",round(success_steps/no_of_success,2))
        if(no_of_failure!=0):
            print("Average failure rate: ",round(failure_steps/no_of_failure,2))

    def hill_climbing_sideway_moves(self):
     ## function to calculate hill climbing with sideways   
        no_of_success = no_of_failure = success_steps = failure_steps = sideways_counter = 0

        for i in range(0,500):

            random_board = Board(self.n)
            h_score = random_board.get_h_score()
            moves = 0
            if(i<4):
                print("Random configuration: ",i+1)
                steps = 0
            while moves<100:
                            
                if(i<4):
                    random_board.print_curr_state()
                    steps+=1
                if h_score==0:
                    break
                else:
                    moves+=1
                    min_h_score,min_list = random_board.get_min_list()
                    
                    if (min_h_score > h_score) or (len(min_list)==0):
                        break
                    else:
                        if h_score == min_h_score:
                            sideways_counter+=1
                        else:
                            sideways_counter=0
                        
                        random_select = random.randint(0,len(min_list)-1)
                        rand_value = min_list[random_select]
                        h_score = min_h_score
                        for j in range(0,self.n):
                            random_board.square[j][rand_value[1]]= "-"
                        random_board.square[rand_value[0]][rand_value[1]]="Q"
            if(h_score==0):
                no_of_success+=1
                success_steps+=moves
                if(i<4):
                    print("================SUCCESS==================")
            else:
                no_of_failure+=1
                failure_steps+=moves
                if(i<4):
                    print("================FAILURE==================")
            
        total = no_of_success + no_of_failure
        rate_of_success = (no_of_success/total)*100
        rate_of_failure = (no_of_failure/total)*100

        print("Rate of success: ",round(rate_of_success,2),"% and Rate of failure is:",round(rate_of_failure,2),"%")

        if(no_of_success !=0):
            print("Average success rate: ",round(success_steps/no_of_success,2))
        if(no_of_failure!=0):
            print("Average failure rate: ",round(failure_steps/no_of_failure,2))
        
    def hill_climbing_random_restart_no_sideways(self):
    ## function to calculate hill climbing with restarts randomly  
        no_of_success = no_of_failure = success_steps = failure_steps = final_restart_counter = 0

        for i in range(0,100):

            random_board = Board(self.n)
            h_score = random_board.get_h_score()
            restart_counter = moves = 0

            while True:
                            
                if h_score == 0:
                    break
                else:
                    moves+=1
                    min_h_score,min_list = random_board.get_min_list()
                    if h_score <= min_h_score or len(min_list)==0:
                        restart_counter+=1
                        random_board = Board(self.n)
                        h_score = random_board.get_h_score()
                        continue
                    random_select = random.randint(0,len(min_list)-1)
                    rand_value = min_list[random_select]
                    h_score = min_h_score
                    for j in range(0,self.n):
                        random_board.square[j][rand_value[1]] = "-"
                    random_board.square[rand_value[0]][rand_value[1]] = "Q"
            if h_score == 0:            
                no_of_success+=1
                success_steps+=moves
                
            else:            
                no_of_failure +=1
                failure_steps+=moves
                
            final_restart_counter+=restart_counter
        total = no_of_success + no_of_failure
        print("Average random restarts without sideways",final_restart_counter/total)
        print("Average moves without sideways",success_steps/total)

    def hill_climbing_random_restart_with_sideways(self):
    ## function to calculate hill climbing with restarts randomly and sideways 
        no_of_success = no_of_failure = success_steps = failure_steps = final_restart_counter = sideways_counter = 0

        for i in range(0,100):
                    
            
            random_board = Board(self.n)
            h_score = random_board.get_h_score()
            moves =0
            restart_counter = 0
            
            while True:
                
                if h_score==0:
                    break
                else:
                    moves+=1
                    min_h_score,min_list = random_board.get_min_list()
                    if h_score < min_h_score or len(min_list)==0:
                        random_board = Board(self.n)
                        h_score = random_board.get_h_score()
                        restart_counter+=1
                        sideways_counter = 0
                        continue
                    
                    if h_score == min_h_score:
                        sideways_counter +=1
                        if moves>=100:
                            random_board = Board(self.n)
                            h_score = random_board.get_h_score()
                            restart_counter+=1
                            sideways_counter = 0
                    else:
                        sideways_counter = 0
                    random_select = random.randint(0,len(min_list)-1)
                    rand_value = min_list[random_select]
                    h_score = min_h_score
                    for j in range(0,self.n):
                        random_board.square[j][rand_value[1]] = "-"
                    random_board.square[rand_value[0]][rand_value[1]] = "Q"
                    
            if h_score==0:
                no_of_success +=1
                success_steps+=moves
            else:
                no_of_failure +=1
                failure_steps +=moves
                
            final_restart_counter+=restart_counter
        total = no_of_success + no_of_failure
        print("Average random restarts with sideways",final_restart_counter/total)
        print("Average moves with sideways",success_steps/total)
            

n = int(input("Enter the value of n:"))
## n value for nqueens taken as user input
solver = Solve(n)
print("Hill climbing steepest ascent")
solver.hill_climbing_Steepest_Ascent()
print("Hill Climbing with sideway moves")
solver.hill_climbing_sideway_moves()
print("Random Restart Hill Climbing without sideway moves")
solver.hill_climbing_random_restart_no_sideways()
print("Random Restart Hill Climbing with Sideway moves")
solver.hill_climbing_random_restart_with_sideways()


