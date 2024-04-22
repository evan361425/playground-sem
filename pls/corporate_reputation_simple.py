#!/usr/bin/env python3
import numpy as np
import pandas as pd
import plspm.config as c
from plspm.mode import Mode
from plspm.plspm import Plspm
from plspm.scale import Scale
from plspm.scheme import Scheme

source = pd.read_csv("file:data/corporate-reputation.csv", index_col=0)
source[source == -99] = np.NaN

structure = c.Structure()
structure.add_path(["COMP"], ["CUSA", "CUSL"])
structure.add_path(["LIKE"], ["CUSA", "CUSL"])
structure.add_path(["CUSA"], ["CUSL"])

config = c.Config(structure.path(), default_scale=Scale.NUM)  # Mean Replacement
config.add_lv_with_columns_named("COMP", Mode.A, source, "comp")
config.add_lv_with_columns_named("LIKE", Mode.A, source, "like")
config.add_lv_with_columns_named("CUSA", Mode.A, source, "cusa")
config.add_lv_with_columns_named("CUSL", Mode.A, source, "cusl")

calculator = Plspm(source, config, Scheme.CENTROID)
print(calculator.inner_summary())
print(calculator.path_coefficients())
