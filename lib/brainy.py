class Brainy():
    def __init__(self):
        self.tape = [0 for i in xrange(30000)]
        self.cur_cell = 0
        self.place = 0
        self.output = []


    def control_head(self, char):
        if char == "+": self.tape[self.cur_cell] += 1
        elif char == "-": self.tape[self.cur_cell] -= 1
        elif char == ">": self.cur_cell += 1
        elif char == "<": self.cur_cell -= 1
        elif char == ".": self.output.append(chr(self.tape[self.cur_cell]))
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

        print ''.join(self.output)
