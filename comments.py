import sm
class CommentsSM(sm.SM):
    startState = 'not comment'

    def getNextValues(self, state, inp):
      if state == "comment":
          if inp == '\n':
              nstate ="not comment"
              output = None
          else:
              nstate = state
              output = inp
      else:
          if inp == '#':
              nstate= "comment"
              output = inp
          else:
                nstate = "not comment"
                output = None
      return (nstate, output)
c = CommentsSM()
print(c.transduce("x = 2 #hello"))
