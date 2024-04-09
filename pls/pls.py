#!/usr/bin/env python3
import pandas as pd
import plspm.config as c
from plspm.mode import Mode
from plspm.plspm import Plspm
from plspm.scheme import Scheme

# https://github.com/GoogleCloudPlatform/plspm-python/tree/trunk?tab=readme-ov-file#pls-pm-with-metric-data
satisfaction = pd.read_csv("file:data/satisfaction.csv", index_col=0)

structure = c.Structure()
structure.add_path(["IMAG"], ["EXPE", "SAT", "LOY"])
structure.add_path(["EXPE"], ["QUAL", "VAL", "SAT"])
structure.add_path(["QUAL"], ["VAL", "SAT"])
structure.add_path(["VAL"], ["SAT"])
structure.add_path(["SAT"], ["LOY"])

config = c.Config(structure.path(), scaled=False)
config.add_lv_with_columns_named("IMAG", Mode.A, satisfaction, "imag")
config.add_lv_with_columns_named("EXPE", Mode.A, satisfaction, "expe")
config.add_lv_with_columns_named("QUAL", Mode.A, satisfaction, "qual")
config.add_lv_with_columns_named("VAL", Mode.A, satisfaction, "val")
config.add_lv_with_columns_named("SAT", Mode.A, satisfaction, "sat")
config.add_lv_with_columns_named("LOY", Mode.A, satisfaction, "loy")

plspm_calc = Plspm(satisfaction, config, Scheme.CENTROID)
print(plspm_calc.inner_summary())
print(plspm_calc.path_coefficients())
