#!/usr/bin/env python3
import pandas as pd
import plspm.config as c
from plspm.mode import Mode
from plspm.plspm import Plspm
from plspm.scheme import Scheme

corpRep = pd.read_csv("file:data/corporate-reputation.csv", index_col=0)

structure = c.Structure()
structure.add_path(["COMP"], ["CUSA", "CUSL"])
structure.add_path(["LIKE"], ["CUSA", "CUSL"])
structure.add_path(["CUSA"], ["CUSL"])

config = c.Config(structure.path(), scaled=False)
config.add_lv_with_columns_named("COMP", Mode.A, corpRep, "comp")
config.add_lv_with_columns_named("LIKE", Mode.A, corpRep, "like")
config.add_lv_with_columns_named("CUSA", Mode.A, corpRep, "cusa")
config.add_lv_with_columns_named("CUSL", Mode.A, corpRep, "cusl")

plspm_calc = Plspm(corpRep, config, Scheme.CENTROID)
print(plspm_calc.inner_summary())
print(plspm_calc.path_coefficients())
