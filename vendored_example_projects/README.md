# Vendored projects

In order to play with various typing tools on some example projects, we not only
need to clone them but also:
- set up a working environment for each that includes depedency stubs
- build configs that may be needed to use tools (e.g. pyre configurations)

As a result, I'm going ahead and vendoring the projects I want to use for exploring
static analysis tools. All of these projects contain the code exactly as cloned on
April 1, 2023, plus possibly some configs and/or instructions I added later as I was
learning to use various tools and measuring the behavior of `pyre infer`.

# Creating

Initially created as follows:
```
git clone --depth 1 https://github.com/python/mypy
rm -rf mypy/.git
git clone --depth 1 https://github.com/urllib3/urllib3
rm -rf urllib3/.git
git clone --depth 1 https://github.com/agronholm/anyio
rm -rf anyio/.git
```
and then
```
pip install -r requirements.txt
```

The requirements came from combining the pip instructions from `mypy_primer` for
all four of these libraries, plus the tools we wanted to play with:
- mypy
- pyanalyze
- pyre-check
- strip-hints (to power experiments removing types and re-adding them)


The `.pyre_configuration` files came from me looking at the relevant `mypy_primer`
commands for mypy to work out the equivalents in Pyre.
