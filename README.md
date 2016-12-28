# gnuplotpy
Basic Python interface to Gnuplot.

Works under Python 2 and Python 3.

##  Installation
* pip: `pip install gnuplotpy`
* setuptools: `cd gnuplotpy && python setup.py install`
* Arch Linux: `yaourt -S python-gnuplotpy`

### Dependencies
If installing using the [Arch Linux AUR package](https://aur.archlinux.org/packages/python-modesolverpy/), dependencies will be automatically downloaded and installed, if not, one should ensure the following dependencies are installed:

#### Python

* [setuptools](https://pypi.python.org/pypi/setuptools).

#### Other

* [Gnuplot](http://www.gnuplot.info/).

## Examples
### Passing Python variables to a Gnuplot script:

#### Gnuplot script:

	set datafile separator ','
	set term pngcairo size 20cm,20cm
	set out filename

	unset key
	set grid
	set border lw 1.5

	set title the_title
	set xrange [x_max-1.1*x_max:x_max*1.1]
	set yrange [-1.1*amp:1.1*amp]

	plot data u 1:2 w lp pt 7 ps 0.5 lw 2

	set out

#### Python script:

	import numpy as np
	import gnuplotpy as gp

	amplitude = 3.
	x = np.linspace(0., 2*3.14, 100)
	y = amplitude*np.sin(x)

	args = {
	    'the_title': 'Example 1',
	    'amp': amplitude,
	    'x_max': x[-1],
	    'filename': 'example1.png'
	}
	data = [x, y]
	gp.gnuplot('test.gpi', args, data)
	
<img src="./examples/example1.png " width="400">

### Plotting simple 2D and 3D plots:

#### Python script

	import numpy as np
	import gnuplotpy as gp

	x = np.linspace(-5, 5, 100)
	y = x**2
	gp.gnuplot_2d(x, y, 'example2a.png', 'Example 2a', 'x', 'x^2')

	z = np.linspace(0., 2.*np.pi, 10000)
	z = z.reshape(100, 100)
	z = np.round(np.sin(z), 1)
	gp.gnuplot_3d_matrix(z, 'example2b.png', 'Example 2b', 'x', 'y')
	
### Output

<img src="./examples/example2a.png " width="400">
<img src="./examples/example2b.png " width="400">

## Contributions
If you add functionality, I'd be interested and would appreciate if you send me a pull request.
