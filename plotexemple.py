"""example.py

Compute the maximum of a Bessel function and plot it.


MODE interactif  :::
lemp@lemp-ThinkPad-W540:~/bin$ ipython --pylab
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
Type "copyright", "credits" or "license" for more information.

IPython 1.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Using matplotlib backend: TkAgg

In [1]: from scipy import special, optimize

In [2]: f = lambda x: -special.jv(3, x)

In [3]: sol = optimize.minimize(f , 1.0)

In [4]: x = linspace(0, 10, 5000)

In [5]: x
Out[5]: 
array([  0.00000000e+00,   2.00040008e-03,   4.00080016e-03, ...,
         9.99599920e+00,   9.99799960e+00,   1.00000000e+01])

In [6]: plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')

Out[7]: 
[<matplotlib.lines.Line2D at 0x7f5361329bd0>,
 <matplotlib.lines.Line2D at 0x7f5361329e50>]



"""

#http://www.scipy.org/getting-started.html


import argparse

import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--order", type=int, default=3, help="order of Bessel function")
    parser.add_argument("--output", default="plot.png", help="output image file")
    args = parser.parse_args()

    # Compute maximum
    f = lambda x: -special.jv(args.order, x)
    sol = optimize.minimize(f, 1.0)

    # Plot
    x = np.linspace(0, 10, 5000)
    plt.plot(x, special.jv(args.order, x), '-', sol.x, -sol.fun, 'o')

    # Produce output
    plt.savefig(args.output, dpi=96)

if __name__ == "__main__":
    main()
