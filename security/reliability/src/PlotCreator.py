import matplotlib.pyplot as plt


class PlotCreator:
    graphics = []
    
    '''
    1. Normal conditions
    '''
    def DrawProbabilityGraph(self, data):
        # Hardware.
        self.graphics.append(plt.subplot(1, 3, 1))
        self.graphics.append(plt.plot(data['timepoint'], data['hardware'], 'o-'))
        plt.title('Hardware')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Software.
        self.graphics.append(plt.subplot(1, 3, 2))
        self.graphics.append(plt.plot(data['timepoint'], data['software'], 'o-'))
        plt.title('Software')
        plt.xlabel('time')

        # Computer.
        self.graphics.append(plt.subplot(1, 3, 3))
        self.graphics.append(plt.plot(data['timepoint'], data['computer'], 'o-'))
        plt.title('Computer')
        plt.xlabel('time')
        plt.ylabel('probability')


    def DrawStoringProbability(self, data):
        # Software.
        self.graphics.append(plt.subplot(1, 2, 1))
        self.graphics.append(plt.plot(data['timepoint'], data['safe'], 'o-'))
        plt.title('Safe stroing')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Computer.
        self.graphics.append(plt.subplot(1, 2, 2))
        self.graphics.append(plt.plot(data['timepoint'], data['fail'], 'o-'))
        plt.title('Fail storing')
        plt.xlabel('time')
        plt.ylabel('probability')


    '''
    2. Real conditions
    '''
    def DrawRealConditionsGraph(self, data):
        # Software.
        self.graphics.append(plt.subplot(1, 2, 1))
        self.graphics.append(plt.plot(data['timepoint'], data['uptime'], 'o-'))
        plt.title('Uptime')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Computer.
        self.graphics.append(plt.subplot(1, 2, 2))
        self.graphics.append(plt.plot(data['timepoint'], data['danial'], 'o-'))
        plt.title('Denial')
        plt.xlabel('time')
        plt.ylabel('probability')


    '''
    3. Cyclic working.
    '''
    def DenialFreeCycligProbability(self, data):
        # Hardware.
        self.graphics.append(plt.subplot(1, 3, 1))
        self.graphics.append(plt.plot(data['timepoint'], data['hardware'], 'o-'))
        plt.title('Hardware')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Software.
        self.graphics.append(plt.subplot(1, 3, 2))
        self.graphics.append(plt.plot(data['timepoint'], data['software'], 'o-'))
        plt.title('Software')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Computer.
        self.graphics.append(plt.subplot(1, 3, 3))
        self.graphics.append(plt.plot(data['timepoint'], data['computer'], 'o-'))
        plt.title('Computer')
        plt.xlabel('time')
        plt.ylabel('probability')


    def DenialCycligProbability(self, data):
        # Hardware.
        self.graphics.append(plt.subplot(1, 3, 1))
        self.graphics.append(plt.plot(data['timepoint'], data['hardware'], 'o-'))
        plt.title('Hardware')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Software.
        self.graphics.append(plt.subplot(1, 3, 2))
        self.graphics.append(plt.plot(data['timepoint'], data['software'], 'o-'))
        plt.title('Software')
        plt.xlabel('time')
        plt.ylabel('probability')

        # Computer.
        self.graphics.append(plt.subplot(1, 3, 3))
        self.graphics.append(plt.plot(data['timepoint'], data['computer'], 'o-'))
        plt.title('Computer')
        plt.xlabel('time')
        plt.ylabel('probability')


    def draw(self):
        plt.show()


if __name__ != "__main__":
    plc = PlotCreator()