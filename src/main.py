import logging

from simulator.simkernel import SimKernel


# logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)
s = SimKernel()
s.start()
