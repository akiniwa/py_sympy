# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from sympy import *

# <codecell>

init_printing()

# <codecell>

x, y, z = symbols('x y z')

# <markdowncell>

# #### 方程式をつくる

# <codecell>

expr = exp(x)/y + z**2
expr

# <markdowncell>

# #### 展開

# <codecell>

expand((x + y)**3)

# <markdowncell>

# #### 因数分解

# <codecell>

factor(x**2 + 2*x*y + y**2)

# <markdowncell>

# #### 方程式を簡単にする

# <codecell>

sympify((x + 2*x + x**3)*4 + 3 + x + 4*x)

# <markdowncell>

# #### 方程式を解く

# <codecell>

expr = x * y + 2/y

# <codecell>

solve(expr, x)

# <markdowncell>

# #### 極限

# <codecell>

# 1/x を x について無限大の極限をとる
limit(1/x, x, oo)

# <markdowncell>

# #### 微分

# <codecell>

diff(sin(x), x)

# <markdowncell>

# #### 積分

# <codecell>

integrate(cos(x), x)

# <codecell>


