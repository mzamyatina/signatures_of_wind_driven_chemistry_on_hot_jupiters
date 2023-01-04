Code for reproducing results from

Maria Zamyatina, Eric Hébrard, Benjamin Drummond, Nathan J Mayne, James Manners, Duncan A Christie, Pascal Tremblin, David K Sing, Krisztian Kohary, Observability of signatures of transport-induced chemistry in clear atmospheres of hot gas giant exoplanets, Monthly Notices of the Royal Astronomical Society, 2022;, stac3432, https://doi.org/10.1093/mnras/stac3432

Tables and Figures
| Item | Description | Code |
|:-----|:------------|:-----|
| Tables 1,2 | Stellar and planetary parameters | calc_astro_parameters.ipynb,<br />calc_astro_parameters_from_atmo.ipynb,<br />calc_astro_parameters_from_um.ipynb,<br />calc_elemental_abundances.ipynb |
| Figure 1 | Zonal-mean zonal wind speed | plt_znl_mean_pres_u.ipynb,<br />plt_latlon_var_wind_at_plevs.ipynb |
| Figure 2 | Pressure-temperature profiles | plt_vp_pres_temp_along_latitude.ipynb,<br />check_dtheta_dz.ipynb |
| Figures 3,C3 | Chemical species vertical profiles | plt_vp_pres_molefrac_along_latitude.ipynb |
| Figures 4,C4,C5 | Photosphere | calc_contribition_function.ipynb,<br />plt_latlon_var_at_norm_con_func_of_1.ipynb |
| Figures 5,6,C7 | Transmission spectra | calc_transmission_spectrum.ipynb |
| Figure 7 | Emission spectra | calc_emission_spectrum.ipynb |
| Figure 8 | Phase curves | calc_phase_curve_timesteps.ipynb,<br />calc_phase_curve.ipynb |
| Table 3 |  Observability of signatures of<br />transport-induced quenching | - |
| Table A1 | Line lists and partition functions | - |
| Table A2 | Pressure broadening | - |
| Figure B1 | Dynamical steady state | check_max_winds.ipynb |
| Figure B2 | Radiative steady state | check_toa_net_energy_flux.ipynb |
| Figure B3 | Chemical steady state | check_burden.ipynb |
| Figures C1,C2 | Temperature, horizontal wind at 10<sup>4</sup>, 10<sup>5</sup> Pa | plt_latlon.ipynb |
| Figure C6 | Absolute absorption cross-sections | plt_absorption_cross_section.ipynb |

Utilities
| Description | Code |
|:------------|:-----|
| Master dictionaries | util_commons.py |
| Master paths | util_mypaths.py |
| Code order | util_order.md |
| Plotting functions | util_plot_func.py |
| Figure style | util_paper.mplstyle |
| Process .pp to .nc | proc_pp_to_nc.ipynb |