# Numerical_Optimization

## Run the Code
基于python完成代码的编写,直接运行代码 Steepest_gradient.py 即可,需要安装numpy功能包


## Workflow and Results

### Workflow
首先需要设定变量的个数, 仿真步长以及设置变量的初值,然后开启梯度下降法:
* 确定下降方向
* 确定步长大小
* 优化变量,直至变量梯度的范数接近于0

### Results
设置N = 8, 起始步长为1.0, c = 0.5, 初值为所有的元素全为2.0, 即为所有元素均为2.0的一个列向量.

迭代次数: 124639

最终结果: [1.00000559 1.0000112  1.00000559 1.0000112  1.00000559 1.0000112
 1.00000559 1.0000112 ]

## Analysis
Linear-search Steepest Gradient Descent with Armijo condition 相比于固定步长的最速下降法即为提高了算法的稳定性,相比于Diminishing step size
即为提高了算法的收敛速度, 相比于Exact line search则为在每一轮的计算时间和总的迭代次数之间做了一个权衡,当然Exact line search中少的迭代次数不代表高效率.

同时初始值如果偏离最优解较远,那么初始步长要选的稍微大一点,不然迭代次数会很多.

