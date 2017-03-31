import numpy as np
from scipy.optimize import least_squares
from curve_fit_models import models

xdata = np.array([x*100 for x in range(1, 17)])

for model, func, jac, numParams in models:
    y = models[](np.array([0.3, 0.2, 0.1]), xdata)
    y_noise = 0.0001 * np.random.normal(size=xdata.size)
    ydata = y + y_noise

    t_init = np.array([0.2, 0.1, 0.01])

    res = least_squares(f2, t_init, jac=jac2, bounds=(-100, 100), args=(xdata, ydata), verbose=1)
    res.cost

    print res.x
    print model2(res.x, xdata)
    print ydata
