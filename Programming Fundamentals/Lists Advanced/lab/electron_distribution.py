def electron_distribution(number_of_electrons):
    electron_list = list()
    counter = 1
    while True:
        current_shell = 2 * (counter ** 2)
        if number_of_electrons > current_shell:
            number_of_electrons -= current_shell
            electron_list.append(current_shell)
        else:
            electron_list.append(number_of_electrons)
            break

        counter += 1

    print(electron_list)


info = int(input())
electron_distribution(info)