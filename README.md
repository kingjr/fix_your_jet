fix_your_jet
============

You wished you hadn't used jet when you saved that figure? Here is a quick fix!

![alt text](https://github.com/kingjr/fix_your_jet/blob/master/example.gif "fix your jet")

# Dependencies
* numpy
* imageio
* matplotlib
* scipy

# Installation

Clone this repository and install using setup.py:

```python setup.py develop --user```


# Examples

```
from imageio import imread, imwrite
from fix_your_jet import fix

example_fix = fix(imread('example.png'),
                  from_cmap='jet', to_cmap='RdBu_r',
                  threshold=100)
imwrite('example_fix.png', example_fix)
```
