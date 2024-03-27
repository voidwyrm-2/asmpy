; label calling example
; Armpy Assembly syntax

call .addNumbers ; call addNumbers
call .doSomethingElse ; call doSomethingElse
prn 0 # print reg0 to console

.addNumbers
 mov 0 3 ; set reg0 to 3
 inc 0 ; add 1 to reg0
 log addNumbers ; sanity check
 ret ; return

.doSomethingElse
 inc 0 ; add 1 to reg0
 log doSomethingElse ; sanity check
 ret ; return