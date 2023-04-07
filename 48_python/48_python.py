lines = 'hi(hi)()'


def index_comparison(l1, l2):
    if len(l1) == 0 and len(l2) == 0:
        return True
    for x, y in zip(l1, l2):
        if x > y:
            return False
    return True


def brekt(text):
    cl = 0
    cr = 0
    indexcl = []
    indexcr = []
    br =  list(text)
    print(br)
    if 0 >= len(br) >= 100:
        return True
    else:
        for i in br:
            if '(' in i:
                cl += 1
                if len(indexcl) == 0:
                    indexcl.append(br.index(i))
                else:
                    if indexcl[-1] == br.index(i):
                        indexcl.append(br[indexcl[-1] + 1:].index(i) + len(br)-len(br[indexcl[-1] + 1:]))

            elif ')' in i:
                cr += 1
                if len(indexcr) == 0:
                    indexcr.append(br.index(i))
                else:
                    if indexcr[-1] == br.index(i):
                        indexcr.append(br[indexcr[-1] + 1:].index(i) + len(br)-len(br[indexcr[-1] + 1:]))

        print(f'(: {indexcl}')
        print(f'): {indexcr}')
        if cl == cr and index_comparison(indexcl, indexcr):
            return True
        else:
            return False


print(brekt(lines))