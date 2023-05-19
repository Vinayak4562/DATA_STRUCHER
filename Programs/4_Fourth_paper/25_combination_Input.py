# department = ['Bakkt', 'Cisco']
# team = ['Red', 'Yellow', 'Black']

# for i in department:
#     for j in team:
#         print("{ 'Department': '" + i + "', 'Team': '" + j + "' }")


input_data = {'department': ['Bakkt', 'Cisco'], 'team': ['Red', 'Yellow', 'Black']}

for dept in input_data['department']:
    for team in input_data['team']:
        print({'Department': dept, 'Team': team})

# OutPut:
# {'Department': 'Bakkt', 'Team': 'Red'}
# {'Department': 'Bakkt', 'Team': 'Yellow'}
# {'Department': 'Bakkt', 'Team': 'Black'}
# {'Department': 'Cisco', 'Team': 'Red'}
# {'Department': 'Cisco', 'Team': 'Yellow'}
# {'Department': 'Cisco', 'Team': 'Black'}
