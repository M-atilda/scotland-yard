#file      : parse_input.py
#date      : 17/02/12
#author    : mi-na
#rational  : parser for polices' program output


#public module


#input string is like [:4],[STATION:7],[:6],[:9]
#implementation
def parse(input_str):
    result = []
    args = input_str.split(',')
    for arg in args:
        dest = arg[arg.find(':')+1:arg.find(']')]
        dest = int(dest)
        if arg[1] == ':':
            result.append({"command": "", "destination": dest})
        elif arg[1] == 'S':
            result.append({"command": "STATION", "destination": dest})
        elif arg[1] == 'A':
            result.append({"command": "AIRPORT", "destination": dest})
        else:
            print("ERROR[PARSE]")
            raise
    return result
