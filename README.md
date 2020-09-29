# nighti
The Night Preprocesser
This currently supports two commands:

.include filename:
Copies the contents of the filename into the current file, like C.

.define A b:
replaces A with b throughtout code.

Note that with
```
.define 1 2
.define a 1
print(a)
```
A will be two, since it does not apply to any macros.
