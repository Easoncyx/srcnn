import argparse
from functools import partial
import json
from keras import optimizers
from pathlib import Path

from toolbox.data import load_set
from toolbox.models import get_model
from toolbox.experiment import Experiment


parser = argparse.ArgumentParser()
parser.add_argument('param_file', type=Path)
args = parser.parse_args()
param = json.load(args.param_file.open())
