def next_version(version: str):
    version_list = [int(num) for num in version.split('.')]
    version_list[2] += 1

    if version_list[2] > 9:
        version_list[2] = 0
        version_list[1] += 1

    if version_list[1] > 9:
        version_list[1] = 0
        version_list[0] += 1

    return '.'.join(map(str, version_list))


version = input()
print(next_version(version))