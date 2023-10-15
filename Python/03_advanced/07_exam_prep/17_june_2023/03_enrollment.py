def gather_credits(max_credits, *args):
    current_credits = 0
    courses_dict = {}
    for arg in args:
        if arg[0] in courses_dict:
            continue
        courses_dict[arg[0]] = arg[1]
        current_credits += arg[1]
        if current_credits >= max_credits:
            break

    result = ''
    if current_credits < max_credits:
        result += f'You need to enroll in more courses! You have to gather {max_credits - current_credits} credits more.'
    else:
        result += f'Enrollment finished! Maximum credits: {current_credits}.\n'
        result += f"Courses: {', '.join(sorted(courses_dict.keys()))}"

    return result


print(gather_credits(
    30,
    ("Basics", 27),
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
