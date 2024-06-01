def tokenize(inp: str) -> list[str]:
    tokens = []
    cur_pos = 0
    while cur_pos < len(inp):
        if inp[cur_pos: min(cur_pos + 5, len(inp))] in ['begin']:
            tokens += [inp[cur_pos: min(cur_pos + 5, len(inp))]]
            cur_pos += 5
        elif inp[cur_pos: min(cur_pos + 3, len(inp))] in ['end']:
            tokens += [inp[cur_pos: min(cur_pos + 3, len(inp))]]
            cur_pos += 3
        elif inp[cur_pos: min(cur_pos + 2, len(inp))] in ['<>', '<=', '>=', ':=']:
            tokens += [inp[cur_pos: min(cur_pos + 2, len(inp))]]
            cur_pos += 2
        elif inp[cur_pos] in ['=', '<', '>', '+', '-', '*', '/', '(', ')', ';']:
            tokens += [inp[cur_pos]]
            cur_pos += 1
        elif inp[cur_pos] in [' ', '\t', '\n', '\r']:
            cur_pos += 1
        else:
            start_position = cur_pos
            while cur_pos < len(inp) and (inp[cur_pos].isalpha() or inp[cur_pos].isnumeric() or inp[cur_pos] in ["_", '.']):
                cur_pos += 1
            tokens += [inp[start_position: cur_pos]]
            if start_position == cur_pos:
                print("ERROR")
                break
    return tokens
