import numpy as np
import gnuplotpy as gp

x = np.linspace(-5, 5, 100)
y = x**2
gp.gnuplot_2d(x, y, 'example2a.png', 'Example 2a', 'x', 'x^2')

z = np.linspace(0., 2.*np.pi, 10000)
z = z.reshape(100, 100)
z = np.round(np.sin(z), 1)
gp.gnuplot_3d_matrix(z, 'example2b.png', 'Example 2b', 'x', 'y')
