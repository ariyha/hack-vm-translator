@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES1
D;JEQ
@SP
A=M-1
M=0
@END1
 0;JMP
(YES1)
@SP
A=M-1
M=-1
(END1)
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES2
D;JEQ
@SP
A=M-1
M=0
@END2
 0;JMP
(YES2)
@SP
A=M-1
M=-1
(END2)
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES3
D;JEQ
@SP
A=M-1
M=0
@END3
 0;JMP
(YES3)
@SP
A=M-1
M=-1
(END3)
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES4
D;JLT
@SP
A=M-1
M=0
@END4
 0;JMP
(YES4)
@SP
A=M-1
M=-1
(END4)
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES5
D;JLT
@SP
A=M-1
M=0
@END5
 0;JMP
(YES5)
@SP
A=M-1
M=-1
(END5)
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES6
D;JLT
@SP
A=M-1
M=0
@END6
 0;JMP
(YES6)
@SP
A=M-1
M=-1
(END6)
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES7
D;JGT
@SP
A=M-1
M=0
@END7
 0;JMP
(YES7)
@SP
A=M-1
M=-1
(END7)
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES8
D;JGT
@SP
A=M-1
M=0
@END8
 0;JMP
(YES8)
@SP
A=M-1
M=-1
(END8)
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@YES9
D;JGT
@SP
A=M-1
M=0
@END9
 0;JMP
(YES9)
@SP
A=M-1
M=-1
(END9)
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=D+M
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
A=M-1
M=M-1
M=!M
@SP
AM=M-1
D=M
A=A-1
M=D&M
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=D|M
@SP
A=M-1
M=!M
(THANOSWASRIGHT)
@THANOSWASRIGHT
0;JMP