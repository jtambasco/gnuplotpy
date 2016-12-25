import os
import numpy as np

class _GnuplotScriptTemp:
    def __init__(self, gnuplot_cmds):
        self.name = '.tmp_gnuplot.gpi'
        with open(self.name, 'w') as fs:
            fs.write(gnuplot_cmds)

    def __del__(self):
        os.remove(self.name)

class _GnuplotDataTemp:
    def __init__(self, *args):
        self.name = '.tmp_gnuplot_data.dat'

        data = np.array(args).T
        with open(self.name, 'wb') as fs:
            np.savetxt(fs, data, delimiter=',')

    def __del__(self):
        os.remove(self.name)

class _GnuplotDataZMatrixTemp:
    def __init__(self, z_matrix):
        self.name = '.tmp_gnuplot_data_z_matrix.dat'

        with open(self.name, 'wb') as fs:
            np.savetxt(fs, z_matrix, delimiter=',')

    def __del__(self):
        os.remove(self.name)

def gnuplot(script_name, args_dict={}, data=[]):
    gnuplot_command = 'gnuplot'

    if data:
        assert 'data' not in args_dict, \
            'Can\'t use \'data\' variable twice.'
        data_temp = _GnuplotDataTemp(*data)
        args_dict['data'] = data_temp.name

    if args_dict:
        gnuplot_command += ' -e "'
        for arg in args_dict.items():
            gnuplot_command += arg[0] + '='
            if isinstance(arg[1], str):
                gnuplot_command += '\'' + arg[1] + '\''
            elif isinstance(arg[1], bool):
                if arg[1] is True:
                    gnuplot_command += '1'
                else:
                    gnuplot_command += '0'
            else:
                gnuplot_command += str(arg[1])
            gnuplot_command += '; '
        gnuplot_command  = gnuplot_command[:-1]
        gnuplot_command += '"'

    gnuplot_command += ' ' + script_name
    os.system(gnuplot_command)

    return gnuplot_command

def gnuplot_2d(x, y, filename, title='', x_label='', y_label=''):
    gnuplot_cmds = \
    '''
    set datafile separator ","
    set term pngcairo size 30cm,25cm
    set out filename

    unset key
    set border lw 1.5
    set grid lt -1 lc rgb "gray80"

    set title title
    set xlabel x_label
    set ylabel y_label

    plot filename_data u 1:2 w lp pt 6 ps 0.5

    set out
    '''
    scr = _GnuplotScriptTemp(gnuplot_cmds)
    data = _GnuplotDataTemp(x, y)

    args_dict = {
        'filename': filename,
        'filename_data': data.name,
        'title': title,
        'x_label': x_label,
        'y_label': y_label
    }
    gnuplot(scr.name, args_dict)

def gnuplot_3d(x, y, z, filename, title='', x_label='', y_label='', z_label=''):
    gnuplot_cmds = \
    '''
    set datafile separator ","
    set term pngcairo size 30cm,25cm
    set out filename

    unset key
    set border lw 1.5
    set view map

    set title title
    set xlabel x_label
    set ylabel y_label
    set zlabel z_label

    splot filename_data u 1:2:3 w pm3d

    set out
    '''
    scr = _GnuplotScriptTemp(gnuplot_cmds)
    data = _GnuplotDataTemp(x, y, z)

    args_dict = {
        'filename': filename,
        'filename_data': data.name,
        'title': title,
        'x_label': x_label,
        'y_label': y_label,
        'z_label': z_label
    }
    gnuplot(scr.name, args_dict)

def gnuplot_3d_matrix(z_matrix, filename, title='', x_label='', y_label='', z_label=''):
    gnuplot_cmds = \
    '''
    set datafile separator ","
    set term pngcairo size 30cm,25cm
    set out filename

    unset key
    set border lw 1.5
    set view map

    set title title
    set xlabel x_label
    set ylabel y_label
    set zlabel z_label

    splot filename_data matrix w pm3d

    set out
    '''
    scr = _GnuplotScriptTemp(gnuplot_cmds)
    data = _GnuplotDataZMatrixTemp(z_matrix)

    args_dict = {
        'filename': filename,
        'filename_data': data.name,
        'title': title,
        'x_label': x_label,
        'y_label': y_label,
        'z_label': z_label
    }
    gnuplot(scr.name, args_dict)
