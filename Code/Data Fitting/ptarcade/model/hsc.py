import numpy as np
from ptarcade.models_utils import g_rho
from scipy.interpolate import interp1d
from ptarcade.models_utils import prior

name = "hsc_14"

parameters = {
    "log_f_min": prior("Uniform", -9, -7),
}

rootp = "/Users/wangao/Desktop/Work/HSC/"
datap = rootp + "data/"

igw = np.loadtxt(datap + "GWarray_results_10e3.csv", delimiter=",")

igwint = interp1d(
    igw[:, 0], igw[:, 1], kind="cubic", bounds_error=False, fill_value=0.0
)
A = 0.014


def spectrum(f, log_f_min):
    fmin = 10**log_f_min
    transfer = 1.62e-5 * (g_rho(fmin, is_freq=True) / 106.75) ** (-1 / 3)
    k = f / fmin * 10**-3
    return (
        igwint(k)
        * transfer
        * (g_rho(f, is_freq=True) / g_rho(fmin, is_freq=True)) ** (-1 / 3)
        * A**2
    )
