from setuptools import setup

setup(name='gnuplotpy',
      version='0.3',
      description='Basic Python interface to Gnuplot.',
      url='https://github.com/jtambasco/gnuplotpy.git',
      author='Jean-Luc Tambasco',
      author_email='an.obscurity@gmail.com',
      license='MIT',
      install_requires=[
          'numpy'
      ],
      packages=['gnuplotpy'],
      zip_safe=False)
