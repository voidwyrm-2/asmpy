; stack example
; Armpy Assembly syntax

mov 0 1 ; set reg0 to 1
mov 1 2 ; set reg1 to 2
mov 2 3 ; set reg2 to 3
mov 3 4 ; set reg3 to 4


push 0 ; add reg0 to the stack
add 0 0 1 ; add together the values of reg0 and reg1 and set reg0 to the result

prn 0 ; print reg0 to console


push 2 ; add reg2 to the stack
add 2 2 3 ; add together the values of reg2 and reg3 and set reg2 to the result

prn 2 ; print reg2 to console


pop 4 ; remove the stack's top value and set reg4 to that value
pop 5 ; remove the stack's top value and set reg5 to that value

prn 4 ; print reg4 to console

prn 5 ; print reg5 to console