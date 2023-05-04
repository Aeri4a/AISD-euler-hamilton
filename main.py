import time
import json
import xlsxwriter
from createGraph import *
from eulerianCycle import *
from hamiltonianCycleW import *
from hamiltonianCyclesW import *

# -- DATA PART --
# -- GENERATE RANGES --
# - I part
p1_startNumber = 3
p1_n = 11
p1_step = 1
p1_dataRange = [x for x in range(
    p1_startNumber, p1_startNumber + (p1_n - 1) * p1_step + 1, p1_step)]

# - II part
p2_startNumber = 15
p2_n = 10
p2_step = 10
p2_dataRange = [x for x in range(
    p2_startNumber, p2_startNumber + (p2_n - 1) * p2_step + 1, p2_step)]


# -- TEMPLATES --
# - Density 20%
tempDensity02 = [{
    "name": "elements",
    "data": []
},
    {
    "name": "density",
    "data": []
},
    {
    "name": "timeEuler",
    "data": []
},
    {
    "name": "timeHamilton1",
    "data": []
},
    {
    "name": "timeHamiltonA",
    "data": []
},
    {
    "name": "cyclesNumber",
    "data": []
}]

# - Density 60%
tempDensity06 = [{
    "name": "elements",
    "data": []
},
    {
    "name": "density",
    "data": []
},
    {
    "name": "timeEuler",
    "data": []
},
    {
    "name": "timeHamilton1",
    "data": []
},
    {
    "name": "timeHamiltonA",
    "data": []
},
    {
    "name": "cyclesNumber",
    "data": []
}]

# -- DENSITY: 20% and 60% --
d02 = 0.2
d06 = 0.6
densities = [d02, d06]

for d in densities:
    if d == 0.2:
        p2_dataRange = [15, 25, 35]
    print(f'---- d={d} ----')
    # -- TEST P1 (SMALL)
    for r in p1_dataRange:
        # Generate graph
        graph, d_approx = createGraph(r, d)
        if r == 5 and d == 0.6:
            graph = {1: {2: 0, 5: 0}, 2: {3: 0, 1: 0}, 3: {
                4: 0, 2: 0}, 4: {5: 0, 3: 0}, 5: {4: 0, 1: 0}}
        elif r == 12 and d == 0.2:
            graph = {1: {3: 0, 4: 0}, 2: {6: 0, 4: 0, 10: 0, 7: 0}, 3: {5: 0, 1: 0}, 4: {1: 0, 2: 0}, 5: {8: 0, 3: 0}, 6: {9: 0, 10: 0, 2: 0, 11: 0}, 7: {
                9: 0, 10: 0, 2: 0, 8: 0}, 8: {5: 0, 7: 0}, 9: {6: 0, 10: 0, 12: 0, 7: 0}, 10: {9: 0, 6: 0, 7: 0, 2: 0}, 11: {6: 0, 12: 0}, 12: {11: 0, 9: 0}}
        elif r == 13 and d == 0.2:
            graph = {1: {9: 0, 7: 0}, 2: {12: 0, 13: 0}, 3: {11: 0, 9: 0}, 4: {7: 0, 8: 0, 10: 0, 13: 0}, 5: {6: 0, 8: 0}, 6: {12: 0, 5: 0}, 7: {1: 0, 4: 0}, 8: {4: 0, 5: 0, 10: 0, 13: 0}, 9:
                     {1: 0, 3: 0}, 10: {4: 0, 8: 0}, 11: {13: 0, 3: 0}, 12: {2: 0, 6: 0}, 13: {11: 0, 4: 0, 8: 0, 2: 0}}

        # Hamilton TRY
        # tH1
        startHamilton1 = time.time_ns()
        path = findHamiltonianCycle(graph)
        resultHamilton1 = time.time_ns() - startHamilton1
        # tHA
        startHamiltonA = time.time_ns()
        counter = findHamiltonianCycles(graph)
        resultHamiltonA = time.time_ns() - startHamiltonA
        # TRY v2
        while not findHamiltonianCycle(graph):
            graph, d_approx = createGraph(r, d)
            # tH1
            startHamilton1 = time.time_ns()
            path = findHamiltonianCycle(graph)
            resultHamilton1 = time.time_ns() - startHamilton1
            # tHA
            startHamiltonA = time.time_ns()
            counter = findHamiltonianCycles(graph)
            resultHamiltonA = time.time_ns() - startHamiltonA
        # tE
        startEuler = time.time_ns()
        tmp = eulerianCycle(graph)
        resultEuler = time.time_ns() - startEuler

        # Add results
        if d == 0.2:
            tempDensity02[0]["data"].append(r)
            tempDensity02[1]["data"].append(d_approx)
            tempDensity02[2]["data"].append(resultEuler)
            tempDensity02[3]["data"].append(resultHamilton1)
            tempDensity02[4]["data"].append(resultHamiltonA)
            tempDensity02[5]["data"].append(counter)
        else:
            tempDensity06[0]["data"].append(r)
            tempDensity06[1]["data"].append(d_approx)
            tempDensity06[2]["data"].append(resultEuler)
            tempDensity06[3]["data"].append(resultHamilton1)
            tempDensity06[4]["data"].append(resultHamiltonA)
            tempDensity06[5]["data"].append(counter)

        print(f'n={r} done')

    # -- TEST P2 (BIG)
    for r in p2_dataRange:
        # Generate graph
        graph, d_approx = createGraph(r, d)

        # Hamilton TRY
        # tH1
        startHamilton1 = time.time_ns()
        path = findHamiltonianCycle(graph)
        resultHamilton1 = time.time_ns() - startHamilton1
        # TRY v2
        while not findHamiltonianCycle(graph):
            print(f'Gen new: n={r}')
            graph, d_approx = createGraph(r, d)
            # tH1
            startHamilton1 = time.time_ns()
            path = findHamiltonianCycle(graph)
            resultHamilton1 = time.time_ns() - startHamilton1
        # tE
        startEuler = time.time_ns()
        tmp = eulerianCycle(graph)
        resultEuler = time.time_ns() - startEuler

        # Add results
        if d == 0.2:
            tempDensity02[0]["data"].append(r)
            tempDensity02[1]["data"].append(d_approx)
            tempDensity02[2]["data"].append(resultEuler)
            tempDensity02[3]["data"].append(resultHamilton1)
        else:
            tempDensity06[0]["data"].append(r)
            tempDensity06[1]["data"].append(d_approx)
            tempDensity06[2]["data"].append(resultEuler)
            tempDensity06[3]["data"].append(resultHamilton1)

        print(f'n={r} done')

# -------------------------
# --- JSON DATA ---
with open("resultsDensity02.json", "w", encoding="utf-8") as file:
    json.dump(tempDensity02, file, indent=2)

with open("resultsDensity06.json", "w", encoding="utf-8") as file:
    json.dump(tempDensity06, file, indent=2)

# --- EXCEL DATA ---
workbook = xlsxwriter.Workbook("results-excel.xlsx")

# - Density 20%
wsDensity02 = workbook.add_worksheet("density02")
for idx, t in enumerate(tempDensity02):
    wsDensity02.write(0, idx, t["name"])
    for i in range(len(t["data"])):
        wsDensity02.write(i+1, idx, t["data"][i])

# - Density 60%
wsDensity06 = workbook.add_worksheet("density06")
for idx, t in enumerate(tempDensity06):
    wsDensity06.write(0, idx, t["name"])
    for i in range(len(t["data"])):
        wsDensity06.write(i+1, idx, t["data"][i])

workbook.close()
