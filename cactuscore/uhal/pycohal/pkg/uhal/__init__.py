
import sys
from _core import *

##################################################
# Pythonic additions to uhal::exception API

def exception_to_string(self):
   return self.what

exception.__str__ = exception_to_string


##################################################
# Pythonic additions to the ValWord_uint32 API

def _add_int_method_to_ValWord(method_name, unary=False):
    # Grab standard int method
    int_method = getattr(int, method_name)
    # Wrap around this method for ValWord_uint32 object
    if unary:
        def valWord_method(self):
            return int_method( int(self) )
    else:
        def valWord_method(self, other):
            if isinstance(other, ValWord_uint32):
                return int_method(int(self), int(other))
            else:
                return int_method(int(self), other)
    # Add wraparound method to ValWord_uint32
    setattr(ValWord_uint32, method_name, valWord_method)

def _add_int_methods_to_ValWord(method_names, unary=False):
    for method_name in method_names:
        _add_int_method_to_ValWord(method_name, unary)

# Unary numeric methods
_add_int_methods_to_ValWord(['__invert__', '__neg__', '__pos__'], unary=True)

# Binary numeric methods
_add_int_methods_to_ValWord(['__add__', '__radd__',
                             '__sub__', '__rsub__',
                             '__mul__', '__rmul__',
                             '__mod__', '__rmod__',
                             '__pow__', '__rpow__',
                             '__lshift__', '__rlshift__',
                             '__rshift__', '__rrshift__',
                             '__and__', '__rand__',
                             '__or__', '__ror__',
                             '__xor__', '__rxor__'
                             ])

if sys.hexversion >= 0x020600F0:
    _add_int_method_to_ValWord('__format__')

# Unary comparison operator (used in "if valWord")
_add_int_method_to_ValWord('__nonzero__', unary=True)

# Binary comparison operator
_add_int_method_to_ValWord('__cmp__')

