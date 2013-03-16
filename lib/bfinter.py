'''
Brainy: A brainfuck interpreter/repl written in python
    Copyright (C) 2012  Joel Buchheim-Moore

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys

class Brainy():
    def __init__(self):
        self.tape = [0 for i in xrange(30000)]
        self.cur_cell = 0
        self.depth = 0
        self.place = 0
        self.loop_list = []
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
        while self.place < len(code):
            if code[self.place] == "[":
                self.depth += 1
                self.loop_list.append(self.place)
                self.place += 1

            elif code[self.place] == "]":
                if self.tape[self.cur_cell] > 0:
                    self.place = self.loop_list[self.depth-1]
                    self.loop_list.pop(-1)
                    self.depth -= 1

                elif self.tape[self.cur_cell] == 0:
                    self.loop_list.pop(-1)
                    self.depth -= 1
                    self.place += 1
            else:
                self.control_head(code[self.place])
                self.place += 1
        self.place = 0
        self.depth = 0

    def get_output(self): return self.__output

    def get_tape(self, start=0, end=10):
        '''Pretty prints the tape values'''
        tmp = '\n'
        for i in xrange(len(self.tape[start:end])):
            if i == self.cur_cell:
                tmp += "[" + str(self.tape[i]) + "] "
            else: tmp += ":" + str(self.tape[i]) + ": "
        return tmp

