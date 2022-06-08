import os
import sys
from pathlib import Path

here = Path(os.path.abspath(__file__))
src = here.parent.parent.joinpath("src")
sys.path.insert(0, str(src))
