def list_lister(listOlists):
    for list in listOlists:
        print(list)


def acter(play):
    acts = []
    act_starts = []
    for i in range(len(play)):
        if play[i:i+4] == "<H3>":
            act_starts.append(i)
    for a_s in range(len(act_starts)-1):
        acts.append(play[act_starts[a_s]:act_starts[a_s+1]])
    acts.append(play[act_starts[-1]:len(play)])
    return acts


def scener(act):
    scenes = []
    scene_starts = []
    for i in range(len(act)):
        if act[i:i+4] == "<h3>":
            scene_starts.append(i)
    for s_s in range(len(scene_starts)-1):
        scenes.append(act[scene_starts[s_s]:scene_starts[s_s+1]])
    scenes.append(act[scene_starts[-1]:len(act)])
    return scenes


def speecher(scene):
    character_name_starts = []
    character_name_ends = []
    for i in range(len(scene)):
        if scene[i:i+3] == "<b>":
            character_name_starts.append(i+3)
        elif scene[i:i+4] == "</b>":
            character_name_ends.append(i)
    speeches = []
    character_name_starts.append(len(scene)+1)
    for c_n_e in range(len(character_name_ends)):
        speeches.append([scene[character_name_starts[c_n_e]:character_name_ends[c_n_e]], scene[character_name_ends[c_n_e]+9:character_name_starts[c_n_e+1]-21]])
    return speeches


def liner(speeches):
    lines = []
    for s in speeches:
        line_starts = []
        line_ends = []
        for i in range(len(s[1])):
            if s[1][i:i+8] == "<A NAME=":
                line_starts.append(i+8)
            elif s[1][i:i+8] == "</A><br>":
                line_ends.append(i)
        for l_s in range(len(line_starts)):
            lines.append([s[0], s[1][line_starts[l_s]:line_ends[l_s]]])
    return lines
