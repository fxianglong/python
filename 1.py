Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("i love you")
i love you
>>> open(1.py)
SyntaxError: invalid syntax
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
>>> open('C:\\Users\\lenovo\\Desktop\\1.py')
<_io.TextIOWrapper name='C:\\Users\\lenovo\\Desktop\\1.py' mode='r' encoding='cp936'>
>>> f = open('C:\\Users\\lenovo\\Desktop\\1.py')
>>> f
<_io.TextIOWrapper name='C:\\Users\\lenovo\\Desktop\\1.py' mode='r' encoding='cp936'>
>>> 
>>> f.read
<built-in method read of _io.TextIOWrapper object at 0x03AC6730>
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x03AC6730>
>>> f.close()
>>> f = open('C:\\Users\\lenovo\\Desktop\\1.py')
>>> f.read()
'Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32\nType "help", "copyright", "credits" or "license()" for more information.\n>>> print("i love you")\ni love you\n>>> '
>>> f.tell
<built-in method tell of _io.TextIOWrapper object at 0x03AC66B8>
>>> f.tell()
211
>>> list(f)
[]
>>> f.seek(0,0)
0
>>> f.tell()
0
>>> f=open('C:\\Users\\lenovo\\Desktop\\test.txt')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    f=open('C:\\Users\\lenovo\\Desktop\\test.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\lenovo\\Desktop\\test.txt'
>>> f=open('C:\\Users\\lenovo\\Desktop\\test.txt','w')
>>> f.write("i love you")
10
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    f.read()
io.UnsupportedOperation: not readable
>>> f.tell()
10
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x03AC6820>
>>> f.close()
>>> import os
>>> os.getcwd()
'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python38-32'\
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll']
>>> os.DirEntry()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    os.DirEntry()
TypeError: cannot create 'nt.DirEntry' instances
>>> os.makedirs(A)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    os.makedirs(A)
NameError: name 'A' is not defined
>>> os.remove('C:\\Users\\lenovo\\Desktop\\1.py')
>>> os.system('cmd')
1
>>> os.system('cmd')
1
>>> os.system('计算机')
1
>>> os.system('计算器')
1
>>> os.system('calc')
1
>>> os.se()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    os.se()
AttributeError: module 'os' has no attribute 'se'
>>> os.sep()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    os.sep()
TypeError: 'str' object is not callable
>>> os.name()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    os.name()
TypeError: 'str' object is not callable
>>> os.path.basename('C:\\config.ini')
'config.ini'
>>> os.path.dirname('C:\\config.ini')
'C:\\'
>>> class base1:
	def foo1(self):
		printf("foo1")

		
>>> class base2
SyntaxError: invalid syntax
>>> class base2:
	def foo2(self):
		print("foo2")

		
>>> class base(base1,base2):
	super().foo1()
	super().foo2()
	print("base")

	
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    class base(base1,base2):
  File "<pyshell#54>", line 2, in base
    super().foo1()
RuntimeError: super(): no arguments
>>> class base(base1,base2):
	super().foo1(self)
	super().foo2(self)
	print("base")

	
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    class base(base1,base2):
  File "<pyshell#56>", line 2, in base
    super().foo1(self)
RuntimeError: super(): no arguments
>>> class trute:
	def __init__(self,x):
		self.num = x

		
>>> class fish:
	def __init__(self,y):
		self.num = y

		
>>> class pool:
	def __init__(self,x,y):
		self.trute = trute(x)
		self.fish = fish(y)
	def print_num(self):
		print("%d,%d"%(self.trute.num,self.fish.num))

		
>>> pool = pool(1,10)
>>> pool.print_num()
1,10
>>> class for:
	
SyntaxError: invalid syntax
>>> class Forma:
	def __init__(self,x,y):
		self.x=x
		self.y = y

		
>>> class Forma:
	def __init__(self,x,y):
		self.x=x
		self.y = y
	def getper(self):
		return (self.x+self.y)*2
	def get arr(self):
		
SyntaxError: invalid syntax
>>> class Forma:
	def __init__(self,x,y):
		self.x=x
		self.y = y
	def getper(self):
		return (self.x+self.y)*2
	def getarr(self):
		return self.x*self.y

	
>>> Forma(3,7)
<__main__.Forma object at 0x00BC1FE8>
>>> f = Forma(2,7)
>>> f.getper()
18
>>> f.getarr()
14
>>> class Forma:
	def __init__(self,x=1,y=1):
		self.x=x
		self.y = y
	def getper(self):
		return (self.x+self.y)*2
	def getarr(self):
		return self.x*self.y

	
>>> f = new Forma
SyntaxError: invalid syntax
>>> f = __new__( Forma)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    f = __new__( Forma)
NameError: name '__new__' is not defined
>>> class ma(Forma):
	def tenb(self):
		print("hgfdsrtyu")

		
>>> type(int)
<class 'type'>
>>> type(list)
<class 'type'>
>>> type(len)
<class 'builtin_function_or_method'>
>>> type(sizeof)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    type(sizeof)
NameError: name 'sizeof' is not defined
>>> type(sizeof())
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    type(sizeof())
NameError: name 'sizeof' is not defined
>>> 