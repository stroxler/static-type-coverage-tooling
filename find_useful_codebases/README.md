# Finding well-typed codebases useful for measuring inference

As part of the Typing Summit talk on static tooling for inferring types,
we wanted to report on how the behavior of `pyre infer` changes as the
number of types in a codebase varies.

To do that, we need to work with some examples of reasonably well-typed
codebases so that we can perform an experiment stripping types and then
applying `pyre infer` types.

This directory contains a pair of scripts we used to measure function-level
coverage using `pyre report` on all the codebases included in the
[mypy_primer database of projects](https://github.com/hauntsaninja/mypy_primer)


Codebases with very high annotation counts (nearly 100%)
- `mypy`
- `bandersnatch`
- `anyio`
- `optuna`
- `urllib3`
- `com2ann`
- `bidict`
- `xarray-dataclasses`
- `Exression`
- `artigraph`
- `schema_salad`
- `nionutils`
- `antidote`
- `pylox`
- `materialize`
- `mkosi`


Some more big projects with well over half of functions fully annotated, but not as
close to 100% as we wanted for our experiment:
- `pytest`
- `spark`
- `aiohttp`
- `poetry`
- `pandera`
- `PyWinCtl`
- `core`
- `rotki`
- `bokeh`
- `discord.py`


The full report is here:
```
> python get_function_level_coverage.py
Stats for mypy_primer
Counter({'FULLY_ANNOTATED': 44})
Stats for mypy
Counter({'FULLY_ANNOTATED': 7534, 'NOT_ANNOTATED': 72, 'PARTIALLY_ANNOTATED': 25})
Stats for black
Counter({'FULLY_ANNOTATED': 817, 'NOT_ANNOTATED': 544, 'PARTIALLY_ANNOTATED': 36})
Stats for pyp
Counter({'FULLY_ANNOTATED': 47, 'NOT_ANNOTATED': 41})
Stats for pytest
Counter({'FULLY_ANNOTATED': 3446, 'NOT_ANNOTATED': 1202, 'PARTIALLY_ANNOTATED': 425})
Stats for pandas
Counter({'NOT_ANNOTATED': 21987, 'FULLY_ANNOTATED': 3634, 'PARTIALLY_ANNOTATED': 2144})
Failed to report on pylint
Stats for aiohttp
Counter({'FULLY_ANNOTATED': 3470, 'NOT_ANNOTATED': 775, 'PARTIALLY_ANNOTATED': 179})
Stats for attrs
Counter({'NOT_ANNOTATED': 910, 'FULLY_ANNOTATED': 13, 'PARTIALLY_ANNOTATED': 3})
Failed to report on sphinx
Stats for scikit-learn
Counter({'NOT_ANNOTATED': 9599, 'FULLY_ANNOTATED': 76, 'PARTIALLY_ANNOTATED': 12})
Stats for bandersnatch
Counter({'FULLY_ANNOTATED': 690, 'PARTIALLY_ANNOTATED': 2})
Stats for boostedblob
Counter({'FULLY_ANNOTATED': 327, 'NOT_ANNOTATED': 72, 'PARTIALLY_ANNOTATED': 3})
Stats for asynq
Counter({'NOT_ANNOTATED': 572})
Stats for scrapy
Counter({'NOT_ANNOTATED': 3795, 'FULLY_ANNOTATED': 261, 'PARTIALLY_ANNOTATED': 104})
Stats for twine
Counter({'NOT_ANNOTATED': 174, 'FULLY_ANNOTATED': 95, 'PARTIALLY_ANNOTATED': 1})
Stats for more-itertools
Counter({'NOT_ANNOTATED': 840})
Stats for xarray
Counter({'NOT_ANNOTATED': 2731, 'FULLY_ANNOTATED': 2642, 'PARTIALLY_ANNOTATED': 642})
Stats for werkzeug
Counter({'NOT_ANNOTATED': 1243, 'FULLY_ANNOTATED': 805, 'PARTIALLY_ANNOTATED': 10})
Stats for jinja
Counter({'NOT_ANNOTATED': 773, 'FULLY_ANNOTATED': 753, 'PARTIALLY_ANNOTATED': 5})
Stats for git-revise
Counter({'FULLY_ANNOTATED': 184, 'NOT_ANNOTATED': 1})
Stats for PyGithub
Counter({'NOT_ANNOTATED': 2864, 'FULLY_ANNOTATED': 5})
Stats for pegen
Counter({'NOT_ANNOTATED': 691, 'FULLY_ANNOTATED': 340, 'PARTIALLY_ANNOTATED': 29})
Stats for zulip
Counter({'FULLY_ANNOTATED': 9988})
Stats for stone
Counter({'NOT_ANNOTATED': 1210})
Stats for paasta
Counter({'NOT_ANNOTATED': 3503, 'FULLY_ANNOTATED': 1489, 'PARTIALLY_ANNOTATED': 134})
Stats for prefect
Counter({'NOT_ANNOTATED': 6336, 'FULLY_ANNOTATED': 1215, 'PARTIALLY_ANNOTATED': 803})
Stats for itsdangerous
Counter({'FULLY_ANNOTATED': 48, 'NOT_ANNOTATED': 40, 'PARTIALLY_ANNOTATED': 19})
Stats for bidict
Counter({'FULLY_ANNOTATED': 193})
Stats for zipp
Counter({'NOT_ANNOTATED': 56})
Stats for websockets
Counter({'NOT_ANNOTATED': 1401, 'FULLY_ANNOTATED': 329, 'PARTIALLY_ANNOTATED': 3})
Stats for isort
Counter({'FULLY_ANNOTATED': 398, 'NOT_ANNOTATED': 318, 'PARTIALLY_ANNOTATED': 66})
Stats for aioredis
Counter({'NOT_ANNOTATED': 462, 'PARTIALLY_ANNOTATED': 359, 'FULLY_ANNOTATED': 282})
Stats for anyio
Counter({'FULLY_ANNOTATED': 1386, 'PARTIALLY_ANNOTATED': 28, 'NOT_ANNOTATED': 1})
Stats for yarl
Counter({'NOT_ANNOTATED': 611, 'FULLY_ANNOTATED': 15})
Stats for freqtrade
Counter({'NOT_ANNOTATED': 1264, 'FULLY_ANNOTATED': 1209, 'PARTIALLY_ANNOTATED': 827})
Stats for jax
Counter({'NOT_ANNOTATED': 11806, 'FULLY_ANNOTATED': 2200, 'PARTIALLY_ANNOTATED': 892})
Stats for dulwich
Counter({'NOT_ANNOTATED': 2794, 'FULLY_ANNOTATED': 277, 'PARTIALLY_ANNOTATED': 133})
Stats for optuna
Counter({'FULLY_ANNOTATED': 2921, 'NOT_ANNOTATED': 46, 'PARTIALLY_ANNOTATED': 24})
Stats for manticore
Counter({'NOT_ANNOTATED': 10291, 'PARTIALLY_ANNOTATED': 555, 'FULLY_ANNOTATED': 384})
Stats for aiortc
Counter({'NOT_ANNOTATED': 782, 'FULLY_ANNOTATED': 420, 'PARTIALLY_ANNOTATED': 47})
Stats for rich
Counter({'FULLY_ANNOTATED': 973, 'NOT_ANNOTATED': 705, 'PARTIALLY_ANNOTATED': 30})
Stats for dedupe
Counter({'FULLY_ANNOTATED': 273, 'NOT_ANNOTATED': 141, 'PARTIALLY_ANNOTATED': 35})
Stats for schemathesis
Counter({'NOT_ANNOTATED': 1171, 'FULLY_ANNOTATED': 1065, 'PARTIALLY_ANNOTATED': 23})
Stats for graphql-core
Counter({'NOT_ANNOTATED': 2921, 'FULLY_ANNOTATED': 940, 'PARTIALLY_ANNOTATED': 118})
Stats for pycryptodome
Counter({'NOT_ANNOTATED': 2680})
Stats for python-chess
Counter({'FULLY_ANNOTATED': 764, 'NOT_ANNOTATED': 341, 'PARTIALLY_ANNOTATED': 8})
Stats for ignite
Counter({'NOT_ANNOTATED': 2791, 'FULLY_ANNOTATED': 809, 'PARTIALLY_ANNOTATED': 96})
Stats for packaging
Counter({'NOT_ANNOTATED': 271, 'FULLY_ANNOTATED': 228})
Stats for pydantic
Counter({'NOT_ANNOTATED': 1397, 'FULLY_ANNOTATED': 860, 'PARTIALLY_ANNOTATED': 151})
Stats for starlette
Counter({'NOT_ANNOTATED': 614, 'FULLY_ANNOTATED': 540, 'PARTIALLY_ANNOTATED': 36})
Stats for janus
Counter({'NOT_ANNOTATED': 98})
Stats for alerta
Counter({'NOT_ANNOTATED': 1055, 'FULLY_ANNOTATED': 243, 'PARTIALLY_ANNOTATED': 53})
Stats for kopf
Counter({'NOT_ANNOTATED': 1881, 'FULLY_ANNOTATED': 676, 'PARTIALLY_ANNOTATED': 73})
Failed to report on parso
Stats for dacite
Counter({'NOT_ANNOTATED': 197, 'FULLY_ANNOTATED': 43, 'PARTIALLY_ANNOTATED': 3})
Stats for com2ann
Counter({'FULLY_ANNOTATED': 88})
Stats for python-htmlgen
Counter({'NOT_ANNOTATED': 530, 'FULLY_ANNOTATED': 1})
Stats for mitmproxy
Counter({'NOT_ANNOTATED': 2730, 'FULLY_ANNOTATED': 1397, 'PARTIALLY_ANNOTATED': 483})
Stats for pyjwt
Counter({'NOT_ANNOTATED': 265, 'FULLY_ANNOTATED': 78, 'PARTIALLY_ANNOTATED': 7})
Stats for spark
Counter({'FULLY_ANNOTATED': 6323, 'NOT_ANNOTATED': 4683, 'PARTIALLY_ANNOTATED': 208})
Stats for paroxython
Counter({'NOT_ANNOTATED': 260, 'FULLY_ANNOTATED': 97, 'PARTIALLY_ANNOTATED': 8})
Stats for porcupine
Counter({'FULLY_ANNOTATED': 757, 'NOT_ANNOTATED': 296, 'PARTIALLY_ANNOTATED': 14})
Stats for mypy-protobuf
Counter({'FULLY_ANNOTATED': 86})
Stats for spack
Counter({'NOT_ANNOTATED': 16838, 'FULLY_ANNOTATED': 983, 'PARTIALLY_ANNOTATED': 131})
Stats for httpx-caching
Counter({'NOT_ANNOTATED': 102, 'FULLY_ANNOTATED': 41, 'PARTIALLY_ANNOTATED': 11})
Stats for poetry
Counter({'FULLY_ANNOTATED': 1523, 'PARTIALLY_ANNOTATED': 739, 'NOT_ANNOTATED': 91})
Stats for sockeye
Counter({'NOT_ANNOTATED': 394, 'FULLY_ANNOTATED': 378, 'PARTIALLY_ANNOTATED': 170})
Stats for nox
Counter({'NOT_ANNOTATED': 393, 'FULLY_ANNOTATED': 194, 'PARTIALLY_ANNOTATED': 10})
Stats for pandera
Counter({'FULLY_ANNOTATED': 643, 'NOT_ANNOTATED': 487, 'PARTIALLY_ANNOTATED': 247})
Stats for cki-lib
Counter({'NOT_ANNOTATED': 467, 'FULLY_ANNOTATED': 140, 'PARTIALLY_ANNOTATED': 7})
Stats for check-jsonschema
Counter({'FULLY_ANNOTATED': 130, 'NOT_ANNOTATED': 116, 'PARTIALLY_ANNOTATED': 4})
Stats for pybind11
Counter({'NOT_ANNOTATED': 720, 'FULLY_ANNOTATED': 36})
Stats for downforeveryone
Counter({'NOT_ANNOTATED': 26, 'FULLY_ANNOTATED': 5})
Failed to report on dd-trace-py
Stats for mkosi
Counter({'FULLY_ANNOTATED': 197, 'NOT_ANNOTATED': 3, 'PARTIALLY_ANNOTATED': 2})
Failed to report on sympy
Stats for nionutils
Counter({'FULLY_ANNOTATED': 810, 'PARTIALLY_ANNOTATED': 8, 'NOT_ANNOTATED': 1})
Stats for flake8-pyi
Counter({'FULLY_ANNOTATED': 91, 'PARTIALLY_ANNOTATED': 3})
Stats for openlibrary
Counter({'NOT_ANNOTATED': 3287, 'FULLY_ANNOTATED': 311, 'PARTIALLY_ANNOTATED': 147})
Stats for imagehash
Counter({'NOT_ANNOTATED': 79})
Stats for PyWinCtl
Counter({'FULLY_ANNOTATED': 223, 'PARTIALLY_ANNOTATED': 95, 'NOT_ANNOTATED': 77})
Stats for pylox
Counter({'FULLY_ANNOTATED': 466})
Stats for ppb-vector
Counter({'PARTIALLY_ANNOTATED': 71, 'NOT_ANNOTATED': 37})
Stats for pyppeteer
Counter({'NOT_ANNOTATED': 569, 'FULLY_ANNOTATED': 458, 'PARTIALLY_ANNOTATED': 2})
Failed to report on pip
Stats for vision
Counter({'NOT_ANNOTATED': 2345, 'FULLY_ANNOTATED': 2246, 'PARTIALLY_ANNOTATED': 160})
Stats for tornado
Counter({'NOT_ANNOTATED': 1879, 'FULLY_ANNOTATED': 1134, 'PARTIALLY_ANNOTATED': 77})
Stats for scipy
Counter({'NOT_ANNOTATED': 18700, 'FULLY_ANNOTATED': 94, 'PARTIALLY_ANNOTATED': 9})
Stats for flake8
Counter({'NOT_ANNOTATED': 312, 'FULLY_ANNOTATED': 205, 'PARTIALLY_ANNOTATED': 1})
^[Stats for core
Counter({'FULLY_ANNOTATED': 40427, 'NOT_ANNOTATED': 12149, 'PARTIALLY_ANNOTATED': 7535})
Stats for kornia
Counter({'NOT_ANNOTATED': 3228, 'FULLY_ANNOTATED': 2060, 'PARTIALLY_ANNOTATED': 91})
Stats for ibis
Counter({'NOT_ANNOTATED': 5825, 'FULLY_ANNOTATED': 960, 'PARTIALLY_ANNOTATED': 220})
Stats for streamlit
Counter({'NOT_ANNOTATED': 2391, 'FULLY_ANNOTATED': 1344, 'PARTIALLY_ANNOTATED': 200})
Stats for dragonchain
Counter({'NOT_ANNOTATED': 804, 'FULLY_ANNOTATED': 698, 'PARTIALLY_ANNOTATED': 22})
Stats for SinbadCogs
Counter({'PARTIALLY_ANNOTATED': 204, 'NOT_ANNOTATED': 149, 'FULLY_ANNOTATED': 73})
Stats for rotki
Counter({'FULLY_ANNOTATED': 3861, 'NOT_ANNOTATED': 1477, 'PARTIALLY_ANNOTATED': 240})
Stats for arviz
Counter({'NOT_ANNOTATED': 1296, 'FULLY_ANNOTATED': 56, 'PARTIALLY_ANNOTATED': 16})
Stats for urllib3
Counter({'FULLY_ANNOTATED': 1401, 'PARTIALLY_ANNOTATED': 8})
Stats for schema_salad
Counter({'FULLY_ANNOTATED': 544, 'NOT_ANNOTATED': 64, 'PARTIALLY_ANNOTATED': 5})
Stats for cwltool
Counter({'FULLY_ANNOTATED': 869, 'NOT_ANNOTATED': 9, 'PARTIALLY_ANNOTATED': 4})
Stats for Tanjun
Counter({'FULLY_ANNOTATED': 1778, 'NOT_ANNOTATED': 1315, 'PARTIALLY_ANNOTATED': 669})
Stats for pyinstrument
Counter({'NOT_ANNOTATED': 194, 'FULLY_ANNOTATED': 81, 'PARTIALLY_ANNOTATED': 63})
Stats for steam.py
Counter({'FULLY_ANNOTATED': 1238, 'PARTIALLY_ANNOTATED': 136, 'NOT_ANNOTATED': 36})
Stats for alectryon
Counter({'NOT_ANNOTATED': 619, 'PARTIALLY_ANNOTATED': 54, 'FULLY_ANNOTATED': 7})
Stats for rclip
Counter({'FULLY_ANNOTATED': 20, 'PARTIALLY_ANNOTATED': 9, 'NOT_ANNOTATED': 7})
Stats for psycopg
Counter({'NOT_ANNOTATED': 2287, 'FULLY_ANNOTATED': 1283, 'PARTIALLY_ANNOTATED': 105})
Stats for python-sop
Counter()
Stats for discord.py
Counter({'FULLY_ANNOTATED': 3186, 'NOT_ANNOTATED': 369, 'PARTIALLY_ANNOTATED': 177})
Stats for cloud-init
Counter({'NOT_ANNOTATED': 5691, 'PARTIALLY_ANNOTATED': 352, 'FULLY_ANNOTATED': 318})
Stats for mongo-python-driver
Counter({'NOT_ANNOTATED': 3317, 'FULLY_ANNOTATED': 907, 'PARTIALLY_ANNOTATED': 3})
Stats for artigraph
Counter({'FULLY_ANNOTATED': 558, 'PARTIALLY_ANNOTATED': 8, 'NOT_ANNOTATED': 4})
Stats for materialize
Counter({'FULLY_ANNOTATED': 1334, 'NOT_ANNOTATED': 38, 'PARTIALLY_ANNOTATED': 20})
Stats for operator
Counter({'NOT_ANNOTATED': 1210, 'FULLY_ANNOTATED': 371, 'PARTIALLY_ANNOTATED': 298})
Stats for xarray-dataclasses
Counter({'FULLY_ANNOTATED': 113})
Stats for apprise
Counter({'NOT_ANNOTATED': 1245, 'PARTIALLY_ANNOTATED': 2})
Stats for sublime_debugger
Counter({'NOT_ANNOTATED': 525, 'PARTIALLY_ANNOTATED': 413, 'FULLY_ANNOTATED': 354})
Stats for antidote
Counter({'FULLY_ANNOTATED': 1357, 'NOT_ANNOTATED': 5, 'PARTIALLY_ANNOTATED': 5})
Stats for Expression
Counter({'FULLY_ANNOTATED': 713, 'NOT_ANNOTATED': 84, 'PARTIALLY_ANNOTATED': 47})
Stats for pyodide
Counter({'NOT_ANNOTATED': 970, 'FULLY_ANNOTATED': 431, 'PARTIALLY_ANNOTATED': 12})
Stats for bokeh
Counter({'FULLY_ANNOTATED': 4750, 'NOT_ANNOTATED': 1009, 'PARTIALLY_ANNOTATED': 358})
Stats for pandas-stubs
Counter({'FULLY_ANNOTATED': 632, 'NOT_ANNOTATED': 124, 'PARTIALLY_ANNOTATED': 31})
Stats for comtypes
Counter({'NOT_ANNOTATED': 882})
Stats for hydra-zen
Counter({'NOT_ANNOTATED': 464, 'FULLY_ANNOTATED': 213, 'PARTIALLY_ANNOTATED': 204})
Stats for Auto-Split
Counter({'PARTIALLY_ANNOTATED': 113, 'NOT_ANNOTATED': 70, 'FULLY_ANNOTATED': 12})
Stats for speedrun.com_global_scoreboard_webapp
Counter({'PARTIALLY_ANNOTATED': 71, 'FULLY_ANNOTATED': 32, 'NOT_ANNOTATED': 20})
Stats for pwndbg
Counter({'NOT_ANNOTATED': 705, 'FULLY_ANNOTATED': 287, 'PARTIALLY_ANNOTATED': 193})
```

