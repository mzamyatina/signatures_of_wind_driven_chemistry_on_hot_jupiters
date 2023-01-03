import iris
from pathlib import Path
from util_mypaths import path_to_data_umserve

PLANETS = {
    "hatp11b": {"tex": "HAT-P-11b"},
    "hd189733b": {"tex": "HD 189733b"},
    "hd209458b": {"tex": "HD 209458b"},
    "wasp17b": {"tex": "WASP-17b"},
}

SUITES = {
    "hatp11b": {
        "equilibrium": {
            "1x solar": {
                "planet": "hatp11b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "initial_profile"
                    / "pt_hatp11b_equilibrium_mdh_0.ncdf"
                ),
                "rose_suite": "u-bl336",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "equilibrium",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "merged"
                ),
                "dir_for_regridded": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "regridded"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hatp11"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hatp11"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336"
                    / "raw"
                    / "atmos_base_1006"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            },
            "100x solar": {
                "planet": "hatp11b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=2 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "initial_profile"
                    / "pt_hatp11b_equilibrium_mdh_2.ncdf"
                ),
                "rose_suite": "u-bl336",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "equilibrium",
                "metallicity": "2",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "bd257"
                    / "um_runs"
                    / "kinetics"
                    / "hatp11_rt"
                    / "u-bl336"
                    / "raw_output"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336_100timesSolar"
                    / "merged"
                ),
                "dir_for_regridded": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "equilibrium"
                    / "u-bl336_100timesSolar"
                    / "regridded"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hatp11"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hatp11"
                ),
            },
        },
        "kinetics": {
            "1x solar": {
                "planet": "hatp11b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "initial_profile"
                    / "pt_hatp11b_equilibrium_mdh_0.ncdf"
                ),
                "rose_suite": "u-bl344",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "kinetics",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "merged"
                ),
                "dir_for_regridded": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "regridded"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hatp11"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hatp11"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344"
                    / "raw"
                    / "atmos_base_1006"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            },
            "100x solar": {
                "planet": "hatp11b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium mdh=2 dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "initial_profile"
                    / "pt_hatp11b_equilibrium_mdh_2.ncdf"
                ),
                "rose_suite": "u-bl344",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "kinetics",
                "metallicity": "2",
                "dir_for_raw_1": Path(
                    path_to_data_umserve
                    / "bd257"
                    / "um_runs"
                    / "kinetics"
                    / "hatp11_rt"
                    / "u-bl344"
                    / "raw_output"  # 0-1000 days
                ),
                "dir_for_raw_2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344_100timesSolar"
                    / "raw"  # 1000-2000 days
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344_100timesSolar"
                    / "merged"
                ),
                "dir_for_regridded": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hatp11b"
                    / "kinetics"
                    / "u-bl344_100timesSolar"
                    / "regridded"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hatp11"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hatp11b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hatp11"
                ),
            },
        },
    },
    "hd189733b": {
        "equilibrium": {
            "1x solar": {
                "planet": "hd189733b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "initial_profile"
                    / "pt_hd189733b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bk868",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "equilibrium",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hd189"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hd189"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "equilibrium"
                    / "u-bk868"
                    / "raw"
                    / "atmos_base_1003"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
        "kinetics": {
            "1x solar": {
                "planet": "hd189733b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "initial_profile"
                    / "pt_hd189733b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bk893",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "kinetics",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hd189"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd189733b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hd189"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd189733b"
                    / "kinetics"
                    / "u-bk893"
                    / "raw"
                    / "atmos_base_1003"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
    },
    "hd209458b": {
        "equilibrium": {
            "1x solar": {
                "planet": "hd209458b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "initial_profile"
                    / "pt_hd209458b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bk852",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "equilibrium",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hd209"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hd209"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "equilibrium"
                    / "u-bk852"
                    / "raw"
                    / "atmos_base_1008"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
        "kinetics": {
            "1x solar": {
                "planet": "hd209458b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "initial_profile"
                    / "pt_hd209458b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bk871",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "kinetics",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_hd209"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "hd209458b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_hd209"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "hd209458b"
                    / "kinetics"
                    / "u-bk871"
                    / "raw"
                    / "atmos_base_1008"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
    },
    "wasp17b": {
        "equilibrium": {
            "1x solar": {
                "planet": "wasp17b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "initial_profile"
                    / "pt_wasp17b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bl436",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "equilibrium",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_wasp17"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_wasp17"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "equilibrium"
                    / "u-bl436"
                    / "raw"
                    / "atmos_base_1008"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
        "kinetics": {
            "1x solar": {
                "planet": "wasp17b",
                "initial_pt_profile_info": "1D ATMO Venot2012 equilibrium 1x solar dayside-average",
                "initial_pt_profile_file": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "initial_profile"
                    / "pt_wasp17b_equilibrium.ncdf"
                ),
                "rose_suite": "u-bl543",
                "chemical_network": "reduced Venot2019",
                "chemical_scheme": "kinetics",
                "metallicity": "1x solar",
                "dir_for_raw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                ),
                "dir_for_merged": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "merged"
                ),
                "dir_for_star_spectrum_lw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "spectral_files"
                    / "sp_lw_500ir_bd_wasp17"
                ),
                "dir_for_star_spectrum_sw": Path(
                    path_to_data_umserve
                    / "um_inputs"
                    / "planets"
                    / "wasp17b"
                    / "spectral_files"
                    / "sp_sw_500ir_bd_wasp17"
                ),
                "dir_for_transmission_day_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day"
                ),
                "dir_for_transmission_night_total": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night"
                ),
                "dir_for_transmission_day_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_ch4"
                ),
                "dir_for_transmission_night_ch4": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_ch4"
                ),
                "dir_for_transmission_day_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co"
                ),
                "dir_for_transmission_night_co": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co"
                ),
                "dir_for_transmission_day_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_co2"
                ),
                "dir_for_transmission_night_co2": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_co2"
                ),
                "dir_for_transmission_day_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2o"
                ),
                "dir_for_transmission_night_h2o": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2o"
                ),
                "dir_for_transmission_day_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_hcn"
                ),
                "dir_for_transmission_night_hcn": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_hcn"
                ),
                "dir_for_transmission_day_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_nh3"
                ),
                "dir_for_transmission_night_nh3": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_nh3"
                ),
                "dir_for_transmission_day_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_h2_cia"
                ),
                "dir_for_transmission_night_h2_h2_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_h2_cia"
                ),
                "dir_for_transmission_day_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_day_h2_he_cia"
                ),
                "dir_for_transmission_night_h2_he_cia": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.ph0000001000_00_night_h2_he_cia"
                ),
                "dir_for_flux_contribution_function_lw": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1001"
                    / "atmosa.pi0000001000_00_flux_con_func"
                ),
                "dir_for_phase_curves": Path(
                    path_to_data_umserve
                    / "um_runs"
                    / "wasp17b"
                    / "kinetics"
                    / "u-bl543"
                    / "raw"
                    / "atmos_base_1008"
                    / "atmosa.pj0000001000_00_phase_curves"
                ),
            }
        },
    },
}

GASES = {
    "He": {"tex": "$He$", "color": "C4"},  # needs changing (C4 as HCN)
    "CH3": {"tex": "$CH_3$"},
    "H": {"tex": "$H$", "color": "C9"},
    "1CH2": {"tex": "$^{1}CH_2$"},
    "H2": {"tex": "$H_2$", "color": "C0"},  # needs changing (C0 as H2O)
    "CH4": {
        "molar_mass": iris.cube.Cube(
            16.043, units="g mol-1", long_name="CH4 molar mass"
        ),
        "tex": "$CH_4$",
        "color": "C3",
    },
    "O-3P": {"tex": "$O(^{3}P)$"},
    "OH": {"tex": "$OH$"},
    "CO": {
        "molar_mass": iris.cube.Cube(
            28.010, units="g mol-1", long_name="CO molar mass"
        ),
        "tex": "$CO$",
        "color": "C1",
    },
    "3CH2": {"tex": "$^{3}CH_2$"},
    "H2CO": {"tex": "$H_2CO$"},
    "CH3O": {"tex": "$CH_3O$"},
    "H2O": {
        "molar_mass": iris.cube.Cube(
            18.015, units="g mol-1", long_name="H2O molar mass"
        ),
        "tex": "$H_2O$",
        "color": "C0",
    },
    "CH3OH": {"tex": "$CH_3OH$"},
    "CO2": {
        "molar_mass": iris.cube.Cube(
            44.009, units="g mol-1", long_name="CO2 molar mass"
        ),
        "tex": "$CO_2$",
        "color": "C2",
    },
    "HCO": {"tex": "$HCO$"},
    "CH2OH": {"tex": "$CH_2OH$"},
    "NH": {"tex": "$NH$"},
    "NNH": {"tex": "$NNH$"},
    "N2": {"tex": "$N_2$", "color": "C7"},
    "NH2": {"tex": "$NH_2$"},
    "N2H2": {"tex": "$N_2H_2$"},
    "NH3": {
        "molar_mass": iris.cube.Cube(
            17.031, units="g mol-1", long_name="NH3 molar mass"
        ),
        "tex": "$NH_3$",
        "color": "C5",
    },
    "N2H3": {"tex": "$N_2H_3$"},
    "HOCN": {"tex": "$HOCN$"},
    "NCO": {"tex": "$NCO$"},
    "CN": {"tex": "$CN$"},
    "HCN": {
        "molar_mass": iris.cube.Cube(
            27.025, units="g mol-1", long_name="HCN molar mass"
        ),
        "tex": "$HCN$",
        "color": "C4",
    },
    "HNCO": {"tex": "$HNCO$"},
    "H2CN": {"tex": "$H_2CN$"},
}

CIA = {
    "h2_h2_cia": {"tex": "$H_2$-$H_2$ CIA", "color": "C6"},
    "h2_he_cia": {"tex": "$H_2$-He CIA", "color": "C8"},
}

STASH = {
    "x_wind": "x_wind",
    "y_wind": "y_wind",
    "upward_air_velocity": "upward_air_velocity",
    "air_pressure": "air_pressure",
    "air_temperature": "air_temperature",
    "toa_incoming_shortwave_flux": "toa_incoming_shortwave_flux",
    "toa_outgoing_longwave_flux": "toa_outgoing_longwave_flux",
    "toa_outgoing_shortwave_flux": "toa_outgoing_shortwave_flux",
    "m01s56i001": "H mole fraction",
    "m01s56i002": "OH mole fraction",
    "m01s56i003": "CH3 mole fraction",
    "m01s56i004": "H2CO mole fraction",
    "m01s56i005": "O-3P mole fraction",
    "m01s56i006": "NH2 mole fraction",
    "m01s56i007": "H2 mole fraction",
    "m01s56i008": "CO mole fraction",
    "m01s56i009": "H2O mole fraction",
    "m01s56i010": "HCO mole fraction",
    "m01s56i011": "NH mole fraction",
    "m01s56i012": "HCN mole fraction",
    "m01s56i013": "CH3OH mole fraction",
    "m01s56i014": "CH4 mole fraction",
    "m01s56i015": "CH3O mole fraction",
    "m01s56i016": "NCO mole fraction",
    "m01s56i017": "CH2OH mole fraction",
    "m01s56i018": "N2H2 mole fraction",
    "m01s56i019": "NH3 mole fraction",
    "m01s56i020": "NNH mole fraction",
    "m01s56i021": "CN mole fraction",
    "m01s56i022": "HNCO mole fraction",
    "m01s56i023": "3CH2 mole fraction",
    "m01s56i024": "N2 mole fraction",
    "m01s56i025": "N2H3 mole fraction",
    "m01s56i026": "1CH2 mole fraction",
    "m01s56i027": "HOCN mole fraction",
    "m01s56i028": "H2CN mole fraction",
    "m01s56i029": "CO2 mole fraction",
    "m01s56i030": "He mole fraction",
}