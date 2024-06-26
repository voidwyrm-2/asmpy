# Asmpy
Asmpy is a Assembly parser(although it's more of an emulator) written in Python<br>
(I'm sorry about how badly written this is)

## Syntax
Asmpy uses a slightly custom Assembly syntax<br>
It's a combination to what I learned from [this minecraft video](https://youtu.be/CW9N6kGbu2I?si=xz2PuppXG7cxwaIb) by mattbatwings(I'm pretty sure it's RISC-V) and [this repo](https://github.com/hackclub/some-assembly-required) by hackclub that explains X86-64 Assembly syntax

I highly recomend both of these, video is really cool(it's what inspired me to make this interpreter in the first place) and the repo is a really good resource for learning Assembly
<!--`destreg` and `reg[number]` are always a index that starts at 0-->

### Actions
I was going to give a list of actions, but then I was like "no" so screw you go learn Assembly<!--[learn Assembly](https://github.com/hackclub/some-assembly-required)--> yourself<br><br>
...<br><br>
Fine, here's the differences between Asmpy and X86-64 Assembly syntax(which is what I was learning to make this):<br>
* `jmp` is like `call`, but it jumps to a line number instead of a label(line number comes from a register), however, I recommend using `call` instead, as it's more reliable
* `jmpi` is like `jmp`, but it jumps to the given immediate
* All registers are referred to as a number from 0 to the amount of r-1, with r being the amount of registers(like RISC-V but without the "r")
* `prn` prints the given register's contents to console
* `log` prints the given message to console
* It has block comments, `:(` and `):` open and close them, respectively

<!--* `add [destreg] [reg1] [reg2]`: reads from reg1 and reg2, adds them together, then sets destrest to the result
* `sub [destreg] [reg1] [reg2]`: reads from reg1 and reg2, subtracts them, then sets destrest to the result
* `and [destreg] [reg1] [reg2]`: reads from reg1 and reg2, compares them with bitwise and, then sets destrest to the result
* `orr [destreg] [reg1] [reg2]`: reads from reg1 and reg2, compares them with bitwise or, then sets destrest to the result
* `nor [destreg] [reg1] [reg2]`: 
* `inc [destreg] [reg1]`: 
* `dec [destreg] [reg1]`: 
* `mov [destreg] [number]`: loads the 
* `jmp`: 
* `prn`: 
* `log`: 
* `call`: 
* `ret`: -->

## CLI
Asmpy uses a CLI to do stuff
* use `exit` or `quit` to quit the interpreter
* use `file [filepath, including extension]` to run a file
* use `run [code]` to run some code directly from the CLI
* use `path [filepath]` to store a path to autmatically append to the beginning of the path given for the `file` command
    * use `path --clear` to clear the stored path
    * the path is not stored when the interpreter is exited


## Installation
To install the Asmpy interpreter, either clone, download this repo, or download just the `asmpy.py` file and then run the `asmpy.py` file<br>
It's really not hard<br>
Because entire program is one python script<br>
Man I love Python



## Licensing
this repo(and, by extension, the Asmpy interpreter) is licensed under the [GNU General Public License Version 3](/LICENSE):

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