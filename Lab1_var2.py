print("Введите данные сотрудников:")
employees = []
while True:
    employee = input()
    if not employee:
        break
    employees.append(tuple(employee.split()))

name_dict = {}
for name in set(name for name, surname in employees):
    name_dict[name] = [employee for employee in employees if employee[0] == name]

surname_dict = {}
for surname in set(surname for name, surname in employees):
    surname_dict[surname] = [employee for employee in employees if employee[1] == surname]

teams = []
visited = set()
for employee in employees:
    if employee not in visited:
        team = []
        queue = [employee]
        while queue:
            cur_employee = queue.pop(0)
            if cur_employee in visited:
                continue
            visited.add(cur_employee)
            team.append(cur_employee)
            for e in name_dict[cur_employee[0]]:
                if e not in visited:
                    queue.append(e)
            for e in surname_dict[cur_employee[1]]:
                if e not in visited:
                    queue.append(e)
        teams.append(team)

print("Количество команд:", len(teams))
for i, team in enumerate(teams):
    print("Команда", i+1, ":", ", ".join(name + " " + surname for name, surname in team))
