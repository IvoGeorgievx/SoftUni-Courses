def company_users():

    companies = {}
    command = input()

    while command != 'End':
        data = command.split(" -> ")
        company_name = data[0]
        employee_id = data[1]

        if company_name not in companies:
            companies[company_name] = []
            companies[company_name].append(employee_id)
        else:
            if employee_id not in companies[company_name]:
                companies[company_name].append(employee_id)

        command = input()

    for key, value in companies.items():
        print(f"{key}")
        for x in range(len(value)):
            print(f"-- {value[x]}")


company_users()
