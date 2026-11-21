"""ODR fit and fit statistics, copied from the course Colab notebooks
(freefall/colab/*.ipynb, heat-conduction/colab/LabA_data_processing.ipynb: same cells).

odr_fit and linear are the notebooks' text unchanged. calc_stats takes fit_func as an
argument; the notebook version reads a global fit_func instead.
"""
from scipy import stats
from scipy.odr import Model, ODR, RealData


def linear(A, x):
    return A[1] * x + A[0]


def odr_fit(fit_func, initial_guesses, x, delta_x, y, delta_y):
    model = Model(fit_func)
    odr_data = RealData(x, y, sx=delta_x, sy=delta_y)
    odr = ODR(data=odr_data, model=model, beta0=initial_guesses)
    output = odr.run()

    fit_params = output.beta
    fit_params_error = output.sd_beta
    fit_cov = output.cov_beta
    return fit_params, fit_params_error, fit_cov, output


def calc_stats(fit_func, x, y, fit_params, output):
    residuals = y - fit_func(fit_params, x)
    degrees_of_freedom = len(x) - len(fit_params)
    chi2 = output.sum_square
    chi2_red = chi2/degrees_of_freedom
    p_val = stats.chi2.sf(chi2, degrees_of_freedom)
    return residuals, degrees_of_freedom, chi2_red, p_val
