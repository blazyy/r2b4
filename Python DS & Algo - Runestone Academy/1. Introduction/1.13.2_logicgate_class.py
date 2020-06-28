class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel() + " -->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        return int(input('Enter Pin B input for gate ' + self.getLabel() + " --> "))

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel() + " -->"))

class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)
    def performGateLogic(self):
        pin = self.getPin()
        if pin == 0:
            return 1
        return 0

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fgate

    def getTo(self):
        return self.tgate

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
                self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
