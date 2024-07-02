# Import each module within the DeepST package
from .adj import *
from .augment import *
from ._compat import *
from .DeepST import *
from .his_feat import *
from .model import *
from .trainer import *
from .utils_func import *

# Define an __all__ list that specifies all the modules you want to be imported when 'from DeepST import *' is used
__all__ = [
    'adj',
    'augment',
    '_compat',
    'DeepST',
    'his_feat',
    'model',
    'trainer',
    'utils_func'
]
