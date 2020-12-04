def move(current, direction, design):
    if design[direction].get(current) == None:
        return current

    return design[direction][current]

def crack(instructions, design, start = 5):
    current = start
    code = ''

    for instruction in instructions:
        for direction in list(instruction):
            current = move(current, direction, design)

        code = '{}{}'.format(code, current)

    return code
