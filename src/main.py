
from simkernel import SimKernel
import logging

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)
s = SimKernel()
s.start()
