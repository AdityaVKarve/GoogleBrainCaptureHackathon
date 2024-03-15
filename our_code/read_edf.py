import os
import mne
import numpy as np
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt

from src.data.utils.eeg import get_raw
from src.data.processing import load_data_dict, get_data
from src.data.conf.eeg_annotations import braincapture_annotations

subject = 'S016'
session = 'R01'

example_file = '../data/S001R01.edf'

raw = get_raw(example_file)
print(raw)