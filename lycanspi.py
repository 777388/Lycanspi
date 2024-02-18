import sys
import matplotlib
class superpi:
    def __init__(self, instance):
        self.instance = instance
    def lycanspi(self):
        return self.instance-self.instance/(float(self.instance)*2.314), (self.instance-self.instance/(float(self.instance)*2.314))-self.instance
class run(superpi):
    def __init__(self, instance):
        super(run, self).__init__(instance)


for i in str(matplotlib.inspect.tokenize.PseudoToken):
    allocator = run(int(ord(i)))
    allocator.lycanspi()
allocator = run(int(sys.argv[1]))
print(allocator.lycanspi())