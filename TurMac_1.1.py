'''
File name: TurMacEm_1.1
Project name: Compact Python Universal Turing Machine Emulator
Author: David Hartkop
Date Created: 2024/11/22
Date last modified: 2024/11/22
Python version: 3.13.0
'''


#Name: Number Counting Zig-Zag
#Description: Writes increasing numbers back and forth between a pair of 8s. When it reaches 4, the program halts.

#TAPE MEMORY is linear list, playheadPosition is the index of that list element.
TapeMem = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
playheadPosition = 1

#CONTROL MEMORY is a 3 dimensional tuple array with instructions to direct the turing machine.
ControlMem = (\
((0, 1, 1, 0), (8, 8, 0, 1), (2, 3, 1, 0), (4, 4, 0, 2)), \
((1, 2, 0, 1), (8, 8, 1, 0), (3, 4, 0, 1)), \
((),)\
)

currentState = 0#Set the start state here. The first state is zero.
cycles = 100 #forces simulator to time-out after this many cycles
cyclecount = 0
while cyclecount < cycles: #CONTROL SYSTEM is handled with this loop. Loop cycles through steps 01-04, which are 01:Read, 02:Write, 03:Move, 04:State.     
        print(TapeMem,"state:", currentState, "cycle:", cyclecount)#print out the list of values on the 'tape' with a cycle count at the end
        print((playheadPosition)*"   ", "^")#playhead position indicator below tape mem line  
#STEP 01:READ playhead into currentPlayheadRead
        currentPlayheadRead = TapeMem[playheadPosition]     
#STEP 02:WRITE new value to playhead according to control memory
        stateRuleCount=(len(ControlMem[currentState]))#determine how many rules are in the given state    
        ruleNumber=0#initialize rule number to 0
        for ruleNumber in range (0,stateRuleCount):#iterate over rules in state
                if ((len(ControlMem[currentState]))==1):
                        break
                if ControlMem[currentState][ruleNumber][0] == currentPlayheadRead:#if the control memory instruction number [0] matches the play head...
                        TapeMem[playheadPosition]=ControlMem[currentState][ruleNumber][1]#...then overwrite current tape position with control memory instruction number [1]
                        break
#STEP 03: MOVE the playhead (L or R)
        if ((len(ControlMem[currentState]))==1):#This only applies to the special case where you land in a state with no rules; This is treated as 'halt condition.'
                break       
        if ControlMem[currentState][ruleNumber][2]==0:#if control memory instruction number [2] is a 0, then move tapehead LEFT.
               playheadPosition=playheadPosition-1
        elif ControlMem[currentState][ruleNumber][2]==1:#if control memory instruction number [2] is a 1, then move tapehead RIGHT.
             playheadPosition=playheadPosition+1   
#STEP 04: change the STATE according to the control memory
        currentState = ControlMem[currentState][ruleNumber][3]#look into control memory instruction number [3] and change the curentState to that.   
        cyclecount = cyclecount+1
print("HALT CONDITION REACHED")
