# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:44:56 2017

@author: hp
"""

import numpy

class CA(object):
    """A CA is a cellular automaton; the parameters for __init__ are:

    rule:  an integer in the range 0-255 that represents the CA rule
           using Wolfram's encoding.
    n:     the number of rows (timesteps) in the result.
    ratio: the ratio of columns to rows.
    """

    def __init__(self, rule, n=100, ratio=2):
        """Attributes:
        table:  rule dictionary that maps from triple to next state.
        n, m:   are the number of rows, columns.
        array:  the numpy array that contains the data.
        next:   the index of the next empty row.
        """
        self.table = self.make_table(rule)
        self.n = n
        self.m = ratio*n + 1
        self.array = numpy.zeros((n, self.m), dtype=numpy.int8)
        self.next = 0

    def make_table(self, rule):
        """Returns a table for the given CA rule.  The table is a 
        dictionary that maps 3-tuples to binary values.
        """
        table = {}
        for i, bit in enumerate(binary(rule, 8)):
            t = binary(7-i, 3)
            table[t] = bit
        return table

    def start_single(self):
        """Starts with one cell in the middle of the top row."""
        self.array[0, self.m/2] = 1
        self.next += 1

    def start_random(self):
        """Start with random values in the top row."""
        self.array[0] = numpy.random.random([1,self.m]).round()
        self.next += 1

    def loop(self, steps=1):
        """Executes the given number of time steps."""
        [self.step() for i in xrange(steps)]

    def step(self):
        """Executes one time step by computing the next row of the array."""
        i = self.next
        self.next += 1

        a = self.array
        t = self.table
        for j in xrange(1,self.m-1):
            a[i,j] = t[tuple(a[i-1, j-1:j+2])]

    def get_array(self, start=0, end=None):
        """Gets a slice of columns from the CA, with slice indices
        (start, end).  Avoid copying if possible.
        """
        if start==0 and end==None:
            return self.array
        else:
            return self.array[:, start:end]


def binary(n, digits):
    """Returns a tuple of (digits) integers representing the
    integer (n) in binary.  For example, binary(3,3) returns (0, 1, 1)"""
    t = []
    for i in range(digits):
        n, r = divmod(n, 2)
        t.append(r)

    return tuple(reversed(t))


def print_table(table):
    """Prints the rule table in LaTeX format."""
    t = table.items()
    t.sort(reverse=True)

    print '\\beforefig'
    print '\\centerline{'
    print '\\begin{tabular}{|c|c|c|c|c|c|c|c|c|}'
    print '\\hline'

    res = ['prev']
    for k, v in t:
        s = ''.join([str(x) for x in k])
        res.append(s)
    print ' & '.join(res) + ' \\\\ \n\\hline'

    res = ['next']
    for k, v in t:
        res.append(str(v))
    print ' &   '.join(res) + ' \\\\ \n\\hline'

    print '\\end{tabular}}'


class UnimplementedMethodException(Exception):
    """Used to indicate that a child class has not implemented an
    abstract method."""


class Drawer(object):
    """Drawer is an abstract class that should not be instantiated.
    It defines the interface for a CA drawer; child classes of Drawer
    should implement draw, show and save.

    If draw_array is not overridden, the child class should provide
    draw_cell.
    """
    def __init__(self):
        msg = 'CADrawer is an abstract type and should not be instantiated.'
        raise UnimplementedMethodException, msg

    def draw(self, ca):
        """Draws a representation of cellular automaton (CA).
        This function generally has no visible effect."""
        raise UnimplementedMethodException
    
    def draw_array(self, a):
        """Iterate through array (a) and draws any non-zero cells."""
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                if a[i,j]:
                    self.draw_cell(j, self.rows-i-1)

    def draw_cell(self, ca):
        """Draws a single cell.
        Not required for all implementations."""
        raise UnimplementedMethodException
    
    def show(self):
        """Displays the representation on the screen, if possible."""
        raise UnimplementedMethodException

    def save(self, filename):
        """Saves the representation of the CA in filename."""
        raise UnimplementedMethodException
        

class PyplotDrawer(Drawer):
    """Implementation of Drawer using matplotlib."""

    def __init__(self):
        # we only need to import pyplot if a PyplotDrawer
        # gets instantiated
        global pyplot
        import matplotlib.pyplot as pyplot

    def draw(self, ca, start=0, end=None):
        """Draws the CA using pyplot.pcolor."""
        pyplot.gray()
        a = ca.get_array(start, end)
        rows, cols = a.shape

        # flipud puts the first row at the top; 
        # negating it makes the non-zero cells black.
        pyplot.pcolor(-numpy.flipud(a))
        pyplot.axis([0, cols, 0, rows])

        # empty lists draw no ticks
        pyplot.xticks([])
        pyplot.yticks([])

    def show(self):
        """display the pseudocolor representation of the CA"""
        pyplot.show()

    def save(self, filename='ca.png'):
        """save the pseudocolor representation of the CA in (filename)."""
        pyplot.savefig(filename)
    

class PILDrawer(Drawer):
    """Implementation of Drawer using PIL and Swampy."""

    def __init__(self, csize=4, color='black'):
        # we only need to import these modules if a PILDrawer
        # gets instantiated
        global Image, ImageDraw, ImageTk, Gui
        import Image
        import ImageDraw
        import ImageTk
        try:
            import Gui
        except ImportError:
            import swampy.Gui
        self.csize = csize
        self.color = color

    def draw(self, ca, start=0, end=None):
        a = ca.get_array(start, end)
        self.rows, self.cols = a.shape
        size = [self.cols * self.csize, self.rows * self.csize]

        self.gui = Gui.Gui()
        self.button = self.gui.bu(command=self.gui.quit)

        self.image = Image.new(mode='1', size=size, color='white')
        self.drawable = ImageDraw.Draw(self.image)
        self.draw_array(numpy.flipud(a))

    def draw_cell(self, i, j):
        size = self.csize
        x, y = i*size, j*size
        self.drawable.rectangle([x, y, x+size, y+size], fill=self.color)

    def show(self):
        self.tkpi = ImageTk.PhotoImage(self.image)
        self.button.config(image=self.tkpi)
        self.gui.mainloop()
 
    def save(self, filename='ca.gif'):
        self.image.save(filename)


class EPSDrawer(Drawer):
    """Implementation of Drawer using encapsulated Postscript (EPS)."""

    def __init__(self):
        self.cells = []

    def draw(self, ca, start=0, end=None):
        a = ca.get_array(start, end)
        self.rows, self.cols = a.shape
        self.draw_array(a)

    def draw_cell(self, i, j):
        self.cells.append((i,j))
        
    def show(self):
        raise UnimplementedMethodException

    def save(self, filename='ca.eps'):
        fp = open(filename, 'w')
        self.print_header(fp)
        self.print_outline(fp)
        self.print_cells(fp)
        self.print_footer(fp)

    def print_cells(self, fp):
        for i, j in self.cells:
            fp.write('%s %s c\n' % (i, j))

    def print_header(self, fp, size=0.9):
        fp.write('%!PS-Adobe-3.0 EPSF-3.0\n')
        fp.write('%%%%BoundingBox: -2 -2 %s %s\n' % (self.cols+2, self.rows+2))

        fp.write('/c {\n')
        fp.write('   newpath moveto\n')
        fp.write('   0 %g rlineto\n' % size)
        fp.write('   %g 0 rlineto\n' % size)
        fp.write('   0 -%g rlineto\n' % size)
        fp.write('   closepath fill\n')
        fp.write('} def\n')

    def print_outline(self, fp):
        fp.write('newpath 0.1 setlinewidth 0 0 moveto\n')
        fp.write('0 %s rlineto\n' % self.rows)
        fp.write('%s 0 rlineto\n' % self.cols)
        fp.write('0 -%s rlineto\n' % self.rows)
        fp.write('closepath stroke\n')

    def print_footer(self, fp):
        fp.write('%%EOF\n')


    import sys
    sys.path.append('E:/wulingfei/CA')#保存CA和CADrawer的地址
    
    
    def CAplot(rule,n,initiate):
        ca = CA.CA(rule, n)
        if initiate == "single":
            ca.start_single()
        else:
            ca.start_random()
        ca.loop(n-1)
        drawer = CADrawer.PyplotDrawer()
        drawer.draw(ca)
    
    
    CAplot(50,10,"random")
