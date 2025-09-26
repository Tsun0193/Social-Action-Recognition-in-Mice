import os
import sys
import json
import logging
import warnings
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, DefaultDict
from collections import defaultdict
import argparse
import numpy as np
import polars as pl
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
from tqdm.auto import tqdm

print("\n" + "="*70)
print(">>> 🧪 SYSTEM CUDA & GPU CHECK (BEFORE ANYTHING ELSE)")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  → GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("  → NO GPU AVAILABLE. Training on CPU.")
print("<<<")
print("="*70 + "\n")
