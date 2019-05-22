import numpy as np

import scipy.optimize
from hyperopt import hp, fmin, tpe

# IDX_PARAMETERS = 0
# IDX_MODEL = 1
# IDX_ARGUMENTS = 2

MAX_EVALS = 500  # Only if tpe


class Fit:

    def __init__(self, method='de'):

        self.method = method

    def _bic(self, lls, best_param, p_choices):
        """
        :param lls: log-likelihood sum
        :return: BIC
        """

        k = len(best_param)
        n_obs = len(p_choices)

        return -2 * lls + np.log(n_obs) * k

    @classmethod
    def _log_likelihood_sum(cls, p_choices):
        return np.sum(np.log(p_choices))

    def _model_stats(self, p_choices, best_param):

        mean_p = np.mean(p_choices)
        lls = self._log_likelihood_sum(p_choices)
        bic = self._bic(lls=lls, best_param=best_param, p_choices=p_choices)

        return mean_p, lls, bic

    def evaluate(self, p_provider, bounds):

        def objective(parameters):

            p_choices_ = p_provider.get_p_choices(parameters)

            if p_choices_ is None or np.any(np.isnan(p_choices_)):
                # print("WARNING! Objective function returning 'None'")
                to_return = np.inf

            else:
                to_return = - self._log_likelihood_sum(p_choices_)

            return to_return

        if self.method == 'tpe':  # Tree of Parzen Estimators

            space = [hp.uniform(*b) for b in bounds]
            best_param = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=MAX_EVALS)

        elif self.method in ('de', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP'):  # Differential evolution

            bounds_scipy = [b[-2:] for b in bounds]

            print("Finding best parameters...", end=' ')

            if self.method == 'de':
                res = scipy.optimize.differential_evolution(
                    func=objective, bounds=bounds_scipy)
            else:
                x0 = np.zeros(len(bounds)) * 0.5
                res = scipy.optimize.minimize(fun=objective, bounds=bounds_scipy, x0=x0)

            best_param_values = res.x
            best_param = {b[0]: v for b, v in zip(bounds, best_param_values)}

            print(f"{res.message} [best loss: {res.fun}]")
            if not res.success:
                raise Exception(f"The fit did not succeed with method {self.method}.")

        else:
            raise Exception(f'Method {self.method} is not defined')

        # Get probabilities with best param
        p_choices = p_provider.get_p_choices(best_param_values)
        model_name = p_provider.model_name()

        # Compute bic, etc.
        mean_p, lls, bic = self._model_stats(p_choices=p_choices, best_param=best_param)

        self._print(model_name, best_param, mean_p, lls, bic)
        return best_param, mean_p, lls, bic

    def _print(self, model_name, best_param, mean_p, lls, bic):

        dsp_best_param = ''.join(f'{k}={round(best_param[k], 3)}, ' for k in sorted(best_param.keys()))

        print(f"[{model_name} - '{self.method}'] Best param: " + dsp_best_param +
              f"LLS: {round(lls, 2)}, " +
              f'BIC: {round(bic, 2)}, mean(P): {round(mean_p, 3)}\n')
