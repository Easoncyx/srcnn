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

scale = param['scale']
build_model = partial(get_model(param['model']['name']),
                      **param['model']['params'])

if 'optimizer' in param:
    optimizer = getattr(optimizers, param['optimizer']['name'].lower())
    optimizer = optimizer(**param['optimizer']['params'])
else:
    optimizer = 'adam'

load_set = partial(load_set,
                   lr_sub_size=param['lr_sub_size'],
                   lr_sub_stride=param['lr_sub_stride'])

expt = Experiment(scale=param['scale'], load_set=load_set,
                  build_model=build_model,optimizer=optimizer,
                  save_dir=param['save_dir'])


repo_dir = Path(__file__).parents[1]
data_dir = repo_dir / 'data' /'mytest' / '1.jpg'
expt.test_on_image(str(data_dir), )
