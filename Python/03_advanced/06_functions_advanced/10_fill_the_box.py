def fill_the_box(*args):
    cube_size = 1
    number_of_cube_arg = 0
    all_cubes = 0
    for arg in args:
        if arg == 'Finish':
            break

        if number_of_cube_arg < 3:
            number_of_cube_arg += 1
            cube_size *= int(arg)
        else:
            all_cubes += int(arg)

    if cube_size - all_cubes > 0:
        return f'There is free space in the box. You could put {cube_size - all_cubes} more cubes.'
    elif cube_size - all_cubes < 0:
        return f'No more free space! You have {all_cubes - cube_size} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
