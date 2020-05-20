def optimal(units, hours, country):
    per_unit_cost = dict()
    for machLen in list(StaticData[country].keys()):
        val = StaticData[country][machLen] / StaticData['Units'][machLen]
        per_unit_cost.update({val: machLen})
    order = sorted(list(per_unit_cost.keys()))
    for i in range(len(order)):
        if int(units) % int(StaticData["Units"][per_unit_cost[order[i]]]) != 0 or i == len(order) - 1:
            if int(units) % int(StaticData["Units"][per_unit_cost[order[i]]]) < 0:
                i += 1
            if int(units) // int(StaticData["Units"][per_unit_cost[order[i]]]) != 0:
                machines.append((per_unit_cost[order[i]], int(units) // int(StaticData["Units"][per_unit_cost[order[i]]])))
            units = int(units) % int(StaticData["Units"][per_unit_cost[order[i]]])
    cost = 0
    for item in machines:
        cost += StaticData[country][item[0]]*item[1]*hours
    cost = "$" + str(cost)
    return cost


input_text = input("Enter the Input :")
if input_text.split()[0] != 'Capacity':
    unit, hour = input_text.split()[0], input_text.split()[3]
else:
    unit, hour = input_text.split()[2], input_text.split()[5]
StaticData = {
    'New York': {'Large': 120, 'XLarge': 230, '2XLarge': 450, '4XLarge': 774, '8XLarge': 1400, '10XLarge': 2820},
    'India': {'Large': 140, '2XLarge': 413, '4XLarge': 890, '8XLarge': 1300, '10XLarge': 2970},
    'China': {'Large': 110, 'XLarge': 200, '4XLarge': 670, '8XLarge': 1180},
    'Units': {'Large': 10, 'XLarge': 20, '2XLarge': 40, '4XLarge': 80, '8XLarge': 160, '10XLarge': 320}
}
Output = list()
for region in ["New York", "India", "China"]:
    machines = list()
    Cost = optimal(int(unit), int(hour), region)
    Output.append({'region': region, 'total_cost': Cost, 'machines': machines})
print({'Output': Output})