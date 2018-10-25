from gurobipy import *

# list of coordinates for dropoff destinations, count starts on 0
dropoff = [[3, 1], [1, 2], [1, 3], [8, 3], [5, 5], [5, 6], [0, 9], [6, 8], [8, 7], [9, 6]]
# list of coordinates for pickup destinations
pickup = [[1, 0], [7, 1], [8, 1], [4, 3], [3, 4], [7, 4], [2, 6], [3, 7], [2, 9], [7, 9]]

# number of dropoff destinations
D = range(len(dropoff))
# number of pickup destinations
P = range(len(pickup))

# create two dimensional array with distance between pickup and dropoff
dist = [[math.sqrt((dropoff[d][0]-pickup[p][0])**2 + (dropoff[d][1]-pickup[p][1])**2) for p in P] for d in D]

# define model name
m = Model("Project2PartB")

# define decision variable, Xdp
X = [[m.addVar(vtype=GRB.INTEGER) for p in P] for d in D]

# add to model
m.update()

# set objective function for model
# quicksum() is an optimized gurobi version of sum()
m.setObjective(quicksum(X[d][p]*dist[d][p]*1.5 for p in P for d in D), GRB.MINIMIZE)

# add constraint: a person can only be dropped off once
for d in D:
    m.addConstr(quicksum(X[d]) <= 1)

# add constraint: all persons should be picked up
m.addConstr(quicksum(X[d][p] for p in P for d in D) == 9)

# add constraint: when car has driven a person, it can not go back to same pickup
m.addConstr(X[0][0] == 0)
m.addConstr(X[1][3] == 0)
m.addConstr(X[2][5] == 0)
m.addConstr(X[3][1] == 0)
m.addConstr(X[4][2] == 0)
m.addConstr(X[5][6] == 0)
m.addConstr(X[6][7] == 0)
m.addConstr(X[7][4] == 0)
m.addConstr(X[8][9] == 0)
m.addConstr(X[9][8] == 0)

m.optimize()

print([[X[d][p].x for p in P] for d in D])
