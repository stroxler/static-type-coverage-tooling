# Code realated to a Typing Summit 2023 presentation on static type-coverage tools


This repo is a dumping ground for code related to collecting data and/or
learning about tools in preparation for a presentation at the 2023 PyCon Typing
Summit about static tooling for measuring and improving type coverage.

We focused on the small but very well typed `anyio` library because it is small
enough to do many rounds of stripping hints from random modules and then
running `pyre infer` to average out noise and see a pattern.


To generate results, we ran:
```
python -m stct.main strip
python -m stct.main infer
python -m stct.main count-infer-output
```

The count actions printed out:
```
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.2_a:
  n_functions is 4, for an average of 0.8 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.2_b:
  n_functions is 8, for an average of 1.6 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.2_c:
  n_functions is 14, for an average of 2.0 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.2_d:
  n_functions is 9, for an average of 1.2857142857142858 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.2_e:
  n_functions is 16, for an average of 3.2 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.4_a:
  n_functions is 13, for an average of 1.3 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.4_b:
  n_functions is 18, for an average of 2.0 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.4_c:
  n_functions is 20, for an average of 1.8181818181818181 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.4_d:
  n_functions is 11, for an average of 1.2222222222222223 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.4_e:
  n_functions is 22, for an average of 2.2 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.6_a:
  n_functions is 30, for an average of 2.142857142857143 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.6_b:
  n_functions is 17, for an average of 1.2142857142857142 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.6_c:
  n_functions is 20, for an average of 1.3333333333333333 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.6_d:
  n_functions is 29, for an average of 1.9333333333333333 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.6_e:
  n_functions is 18, for an average of 1.2 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.8_a:
  n_functions is 32, for an average of 1.6842105263157894 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.8_b:
  n_functions is 25, for an average of 1.3888888888888888 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.8_c:
  n_functions is 33, for an average of 1.5714285714285714 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.8_d:
  n_functions is 35, for an average of 1.8421052631578947 per module
On project /home/stroxler/kode/static-type-coverage-tooling/stripped_examples/anyio__0.8_e:
  n_functions is 25, for an average of 1.1904761904761905 per module
```

From this we determined that the mean annotations
- With 20% stripping, 1.776 (`sum([0.8, 1.6, 2.0, 1.28, 3.2]) / 5`)
- With 40% stripping, 1.708 (`sum([1.3, 2.0, 1.82, 1.22, 2.2]) / 5`)
- With 60% stripping, 1.562 (`sum([2.14, 1.21, 1.33, 1.93, 1.2]) / 5`)
- With 80% stripping, 1.532 (`sum([1.68, 1.38, 1.57, 1.84, 1.19]) / 5`)
