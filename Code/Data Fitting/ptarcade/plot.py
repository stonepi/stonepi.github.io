from ptarcade import chains_utils as c_utils
from ptarcade import plot_utils as p_utils

model_name = "hsc_14"
params, chain = c_utils.import_chains("./chains/" + model_name)

p_utils.plot_posteriors(
    [chain],
    [params],
    par_names=[
        {
            r"$\log_{10} f_\mathrm{min}$": [-8.5, -5],
        }
    ],
    save=True,
    model_name=model_name,
)
