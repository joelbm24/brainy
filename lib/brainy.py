import sys

class Brainy():
    def __init__(self):
        self.tape = [0 for i in xrange(30000)]
        self.cur_cell = 0
        self.place = 0
        self.__output = ''


    def control_head(self, char):
        if char == "+": self.tape[self.cur_cell] += 1
        elif char == "-": self.tape[self.cur_cell] -= 1
        elif char == ">": self.cur_cell += 1
        elif char == "<": self.cur_cell -= 1
        elif char == ".":
            sys.stdout.write(chr(self.tape[self.cur_cell]))
            self.__output += chr(self.tape[self.cur_cell])
        else: return False

    def eval(self, code):
        while self.place != len(code):
            if code[self.place] == "[":
                hold_place = self.place

            if code[self.place] == "]":
                if self.tape[self.cur_cell] != 0:
                    self.place = hold_place

            self.control_head(code[self.place])
            self.place += 1
        self.place = 0

    def get_output(self): return self.__output

    def get_tape(self, start=0, end=10):
        '''Pretty prints the tape values'''
        tmp = '\n'
        for i in xrange(len(self.tape[start:end])):
            if i == self.cur_cell:
                tmp += "[" + str(self.tape[i]) + "] "
            else: tmp += ":" + str(self.tape[i]) + ": "
        return tmp

