#file      : police_operate.py
#date      : 17/02/12
#author    : mi-na
#rational  : simple police operater for debug


def get_map():
    map_data = []
    map_str = ""
    with open("resource/map_data.txt", 'r') as f:
        map_str = f.read()
    map_lines = map_str.split('\n')[:-1]

    for (i, line) in enumerate(map_lines):
        target_sentense = line[line.find('[')+1:-1]
        edges = target_sentense.split('*')
        #just extract suitable edge
        flag = True
        for e in edges:
            if len(e) < 15:
                tips = e[2:-4].split(',')
                if int(tips[0]) == (i+1):
                    map_data.append(int(tips[1]))
                else:
                    map_data.append(int(tips[0]))
                flag = False
                break
        if flag:
            #all edges have some attribute
            map_data.append(0)
    return map_data

def get_status():
    polices_data = []
    polices_str = ""
    with open("resource/status.txt", 'r') as f:
        polices_str = f.read()
    turn_num = int(polices_str.split('\n')[0])
    polices_line = polices_str.split('\n')[1:-1]
    if turn_num in [3, 8, 14, 20, 24]:
        polices_line = polices_str.split('\n')[2:-1]
    for p in polices_line:
        polices_data.append(int(p[p.find("p]")+2:p.find("[c")]))
    return polices_data

def main():
    next_action = ""
    map_data = get_map()
    polices_data = get_status()
    for pos in polices_data:
        dest = map_data[pos-1]
        temp_str = "[:" + dest.__str__() + "],"
        next_action += temp_str
    with open("resource/nextAction.txt", 'w') as f:
        f.write(next_action[:-1])

#main process
if __name__ == '__main__':
    main()
