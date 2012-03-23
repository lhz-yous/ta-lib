import numpy
import pylab

import talib

TEST_LEN = 1000

r = numpy.arange(TEST_LEN)
idata = numpy.random.random((TEST_LEN))

(bidx, elements, odata) = talib.MA(idata)

(bidx, elements, upper, middle, lower) = talib.BBANDS(idata)

(bidx, elements, kama) = talib.KAMA(idata)

length = min(len(odata), len(upper), len(kama))

# make them all the same length
r = r[-length:]
idata = idata[-length:]
odata = odata[-length:]
upper = upper[-length:]
middle = middle[-length:]
lower = lower[-length:]
kama = kama[-length:]

pylab.plot(r, idata, 'b-', label="original")
pylab.plot(r, odata, 'g-', label="MA")
pylab.plot(r, upper, 'r-', label="Upper")
pylab.plot(r, middle, 'r-', label="Middle")
pylab.plot(r, lower, 'r-', label="Lower")
pylab.plot(r, kama, 'g', label="KAMA")
pylab.legend()
pylab.show()

