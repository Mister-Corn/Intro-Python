from room import Room

def importRoomsFromMyFile(fromObj, toObj):
    # for index, level in enumerate(fromObj):
    #     # index = str(i)
    #     for room in level:
    #         print(f"index: {index}")
    #         print('room:', str(room))
    #         if room not in toObj:
    #             toObj[room] = Room()
    #         print(f"toObj: {toObj}\n---")
    #         print(f"current fromObj: {fromObj[index][room]['name']}")
    #         toObj[room].name[index] = fromObj[index][room]['name']
    #         print(f"current toObj: {toObj[room].name[index]}\n")
    for index, level in enumerate(fromObj):
        for room in level:
            if room not in toObj:
                toObj[room] = Room()
            toObj[room].name[index] = fromObj[index][room]['name']
            toObj[room].description[index] = fromObj[index][room]['description']
            if 'level_up' in fromObj[index][room]:
                toObj[room].level_up[index] = fromObj[index][room]['level_up']
            if 'error' in fromObj[index][room]:
                toObj[room].error[index] = fromObj[index][room]['error']
        
        for room in level:
            if 'n_to' in fromObj[index][room]:
                toObj[room].direction[index]['n_to'] = toObj[fromObj[index][room]['n_to']]
            if 's_to' in fromObj[index][room]:
                toObj[room].direction[index]['s_to'] = toObj[fromObj[index][room]['s_to']]
            if 'e_to' in fromObj[index][room]:
                toObj[room].direction[index]['e_to'] = toObj[fromObj[index][room]['e_to']]
            if 'w_to' in fromObj[index][room]:
                toObj[room].direction[index]['w_to'] = toObj[fromObj[index][room]['w_to']]