from pathlib import Path



class linls:
    '''
    Simple linear list(or, a "stack")
    '''
    def __init__(self, value = []):
        self.value = list(value)
    
    def append(self, value):
        self.value.append(value)
    
    def pop(self):
        return self.value.pop()
    
    def extend(self, value):
        self.value.extend(value)



class asmpy:
    def __init__(self, registersize: int = 8):
        self.register = [0 for _ in range(8)]
        self.labels = {}
        self.stack = linls()

    def parseasm(self, asm: str | list[str] | tuple[str]):
        if type(asm) is tuple:
            asm = list(asm)
        elif type(asm) is str:
            asm = asm.split('\n')
        
        inlab = False
        labinfo = ()
        for ln in range(len(asm)):
            l = asm[ln].strip()
            if (not l.startswith('.') and not l.startswith('ret')) or len(l.removeprefix('.')) < 1:
                continue
            if ';' in l:
                l = l.split(';')[0]

            if l.startswith('.') and not inlab:
                labinfo = (l, ln)
                inlab = True
                continue
            elif l.startswith('ret') and inlab:
                self.labels[labinfo[0]] = (labinfo[1], ln)
                labinfo = ()
                inlab = False
        
        line = 0
        callnest = 0
        callls = linls()
        while line < len(asm):
            l = asm[line].strip()
            if l.startswith(';') or len(l.strip()) < 1:
                line += 1
                continue
            if ';' in l:
                l = l.split(';')[0].strip()
            if l.startswith('.'):
                if l in self.labels.keys():
                    #print('label found, jump to line', self.labels[l][1] + 1)
                    line = self.labels[l][1]
                    continue
            l = l.split(' ')

            if l[0] not in ('jmp', 'log', 'call'):
                ignore = False
                for i in range(len(l)):
                    if i == 0 or i in list(self.labels.values()): continue
                    check = False
                    if l[0] in ('mov', 'ldi', 'lod'):
                        check = l[i].replace('.', '').isdigit() and l[i].count('.') <= 1
                    else:
                        check = l[i].isdigit()
                    if not check:
                        print(f'(syntax checker) invalid syntax "{l[i]}" on line {i + 1}')
                        ignore = True
                        break
                if ignore:
                    line += 1
                    continue
            
            match l[0]:
                case 'add':
                    self.register[int(l[1])] = self.register[int(l[2])] + self.register[int(l[3])]
                case 'sub':
                    self.register[int(l[1])] = self.register[int(l[2])] - self.register[int(l[3])]
                #case 'mul':
                #    self.register[int(l[1])] = float(l[2]) * float(l[3])
                #case 'div':
                #    self.register[int(l[1])] = float(l[2]) / float(l[3])
                case 'and':
                    self.register[int(l[1])] = self.register[int(l[2])] & self.register[int(l[3])]
                case 'orr':
                    self.register[int(l[1])] = self.register[int(l[2])] | self.register[int(l[3])]
                case 'nor':
                    self.register[int(l[1])] = not (self.register[int(l[2])] | self.register[int(l[3])])
                case 'inc':
                    self.register[int(l[1])] = self.register[int(l[1])] + 1
                case 'dec':
                    self.register[int(l[1])] = self.register[int(l[1])] - 1
                case 'mov' | 'ldi' | 'lod':
                    self.register[int(l[1])] = float(l[2]) if '.' in l[2] else int(l[2])
                case 'jmp':
                    if l[1].startswith('.'):
                        if l[1] in list(self.labels.keys()):
                            line = self.labels[l[1]]
                    elif int(l[1]) < len(self.register):
                        line = int(l[1])
                case 'prn':
                    print(self.register[int(l[1])])
                case 'log':
                    print(l[1])
                case 'call':
                    if l[1] in list(self.labels.keys()):
                        callnest += 1
                        callls.append(line)
                        line = self.labels[l[1]][0]
                case 'ret':
                    if callnest > 0:
                        callnest -= 1
                        line = callls.pop()
                case 'goto':
                    line = int(l[1])
                case 'push':
                    self.stack.append(self.register[int(l[1])])
                case 'pop':
                    self.register[int(l[1])] = self.stack.pop()
                case x:
                    print(f'(parser) invalid syntax "{l[0]}" on line {line + 1}')
            line += 1



def cli():
    inst = asmpy()
    pathcache = ''
    running = True
    while running:
        inp = input('> ').strip()
        if inp in ('exit', 'quit'):
            running = False
            break
        elif inp.startswith('file '):
            inp = pathcache + inp.removeprefix('file ')
            if not Path(inp).exists():
                if not Path('../' + inp).exists():
                    print('file does not exist')
                    continue
                else:
                    inp = '../' + inp
            with open(inp, 'rt') as asmf:
                file = asmf.read()
            inst.parseasm(file)
        elif inp.startswith('run '):
            inp = inp.removeprefix('run ')
            inst.parseasm(inp)
        elif inp.startswith('path '):
            path = inp.removeprefix('path ')#.replace('\\ ', '<\\SPACE\\>').replace('\\', '/').replace('<\\SPACE\\>', '\\ ')
            if path == '--clear':
                pathcache = ''
                continue
            if not path.endswith('/') and not path.endswith('\\'):
                path += '/'
            if not Path(path).exists():
                if not Path('../' + path).exists():
                    print('path does not exist')
                    continue
            pathcache = path



if __name__ == '__main__':
    cli()