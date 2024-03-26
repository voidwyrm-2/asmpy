# Asmpy
Asmpy is a Assembly parser(although it's more of an emulator) written in Python<br>
(I'm sorry about how badly written this is)

## Syntax
Asmpy uses a slightly custom Assembly syntax<br>
It's a combination to what I learned from [this](https://youtu.be/CW9N6kGbu2I?si=xz2PuppXG7cxwaIb) minecraft video by mattbatwings and [this](https://github.com/hackclub/some-assembly-required) repo that explains X86-64 Assembly syntax

I highly recomend both of these, video is really cool(it's what inspired me to make this interpreter in the first place) and the repo is a really good resource for learning Assembly
<!--`destreg` and `reg[number]` are always a index that starts at 0-->

### Actions
I was going to give a list of actions, but then I was like "no" so screw you go learn Assembly<!--[learn Assembly](https://github.com/hackclub/some-assembly-required)--> yourself<br><br>
...<br><br>
Fine, here's the differences between Asmpy and X86-64 Assembly syntax(which is what I was learning to make this):<br>
* `jmp` is like `call`, but it can jump to a line number as well(line number comes from a register)
* `goto` is like `jmp` or `call`, but it jumps to the line number given in the code
* all registers are referred to as a number from 0 to the amount of registers minus 1(base register amount is 8, so it would be from 0-7 in that case)
* `prn` prints the given register's contents to console
* `log` prints the given message to console

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