'''
    Copyright (C) 2024  Nuclear Pasta

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''



from pathlib import Path



class Linls:
    '''
    Simple linear list(or, a "stack")
    '''
    def __init__(self, value = []):
        self.__value = list(value)
    
    def append(self, value):
        self.__value.append(value)
    
    def pop(self):
        return self.__value.pop()
    
    def extend(self, value):
        self.__value.extend(value)



class Asmpy:
    def __init__(self, registersize: int = 16):
        # init register list, label dict, and stack linear list
        self.__register = [0 for _ in range(registersize)]
        self.__labels = {}
        self.__stack = Linls()
        self.__ZF = False

    def parseasm(self, asm: str | list[str] | tuple[str]):
        if type(asm) is tuple: # if asm is a tuple, make it a list
            asm = list(asm)
        elif type(asm) is str: # if asm is a str, split it by new lines
            asm = asm.split('\n')
        
        # preload all labels
        inlab = False
        labinfo = ()
        lpibc = False # label preloader isblockcomment
        for ln in range(len(asm)):
            l = asm[ln].strip()
            if '):' in l:
                l = l.split('):')[-1]
                lpibc = False

            if lpibc:
                continue
            
            if ':(' in l:
                l = l.split(':(')[0].strip()
                lpibc = True

            if (not l.startswith('.') and not l.startswith('ret')) or len(l.removeprefix('.')) < 1:
                continue # ignore the line if it's not a label, a return, or if it's empty

            if ';' in l: # check for line comment
                l = l.split(';')[0].strip() # remove commented out part
            
            

            if l.startswith('.') and not inlab:
                labinfo = (l, ln)
                inlab = True
                continue

            elif l.startswith('ret') and inlab:
                self.__labels[labinfo[0]] = (labinfo[1], ln)
                labinfo = ()
                inlab = False
        
        line = 0
        callnest = 0
        callls = Linls()
        isblockcomment = False
        gotzero = False
        while line < len(asm):
            l = asm[line].strip()

            if '):' in l:
                l = l.split('):')[-1]
                isblockcomment = False
            
            if isblockcomment:
                continue

            if ':(' in l:
                l = l.split(':(')[0].strip()
                isblockcomment = True

            if l.startswith(';') or len(l.strip()) < 1:
                line += 1
                continue

            if ';' in l:
                l = l.split(';')[0].strip()
            
            if l.startswith('.'):
                if l in self.__labels.keys():
                    #print('label found, jump to line', self.__labels[l][1] + 1)
                    line = self.__labels[l][1]
                    continue
            l = l.split(' ')

            if l[0] not in ('jmp', 'log', 'call'):
                ignore = False
                for i in range(len(l)):
                    if i == 0 or i in list(self.__labels.values()): continue
                    check = False
                    if l[0] in ('mov', 'ldi'):
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
                    res = self.__register[int(l[2])] + self.__register[int(l[3])]
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'sub':
                    res = self.__register[int(l[2])] - self.__register[int(l[3])]
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'addi':
                    res = self.__register[int(l[2])] + int(l[3])
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'subi':
                    res = self.__register[int(l[2])] - int(l[3])
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                #case 'mul':
                #    self.__register[int(l[1])] = float(l[2]) * float(l[3])
                #case 'div':
                #    self.__register[int(l[1])] = float(l[2]) / float(l[3])
                case 'and':
                    res = self.__register[int(l[2])] & self.__register[int(l[3])]
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'orr':
                    res = self.__register[int(l[2])] | self.__register[int(l[3])]
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'nor':
                    res = not (self.__register[int(l[2])] | self.__register[int(l[3])])
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'inc':
                    res = self.__register[int(l[1])] + 1
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'dec':
                    res = self.__register[int(l[1])] - 1
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'mov' | 'ldi':
                    res = float(l[2]) if '.' in l[2] else int(l[2])
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case 'jmp':
                    if l[1].startswith('.'):
                        if l[1] in list(self.__labels.keys()):
                            line = self.__labels[l[1]]
                    elif int(l[1]) < len(self.__register):
                        line = int(l[1])
                case 'prn':
                    print(self.__register[int(l[1])])
                case 'log':
                    print(l[1])
                case 'call':
                    if l[1] in list(self.__labels.keys()):
                        callnest += 1
                        callls.append(line)
                        line = self.__labels[l[1]][0]
                case 'ret':
                    if callnest > 0:
                        callnest -= 1
                        line = callls.pop()
                case 'jmpi':
                    line = int(l[1])
                case 'push':
                    self.__stack.append(self.__register[int(l[1])])
                case 'pop':
                    res = self.__stack.pop()
                    if not res: self.__ZF = True; gotzero = True
                    self.__register[int(l[1])] = res
                case x:
                    print(f'(parser) invalid syntax "{l[0]}" on line {line + 1}')
            if gotzero:
                gotzero = False
            else:
                self.__ZF = False
            line += 1



def cli():
    inst = Asmpy()
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