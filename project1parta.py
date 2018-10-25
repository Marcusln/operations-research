facilities = ["F1", "F2", "F3"]
pollutants = ['P1', 'P2']

# cost of processing fish at facility F
cost = {
    'F1': 30,
    'F2': 20,
    'F3': 40
}

# amount of pollutant P reduced per ton processed fish at facility F
amountReduced = {
    ('F1', 'P1'): 0.1,
    ('F1', 'P2'): 0.45,
    ('F2', 'P1'): 0.2,
    ('F2', 'P2'): 0.25,
    ('F3', 'P1'): 0.4,
    ('F3', 'P2'): 0.3
}

# govt reduction target of pollutant P
govtTarget = {
    'P1': 25,
    'P2': 35
}

# define model name
m = Model("Project1PartA")

# create decision variable
tonProcessed = {}

for f in facilities:
    tonProcessed[f] = m.addVar(name=f)

# add to model
m.update()

# set objective function for model
m.setObjective(sum(tonProcessed[f]*cost[f] for f in facilities), GRB.MINIMIZE)

m.addConstrs(
    (quicksum(
        amountReduced[f, p] * tonProcessed[f] for f in facilities) >= govtTarget[p] for p in pollutants),
    name="govtTarget")

# solve model
m.optimize()
