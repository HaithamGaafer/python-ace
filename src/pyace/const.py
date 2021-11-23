FIT_NITER_KW = 'maxiter'
FIT_OPTIONS_KW = 'options'
BACKEND_BATCH_SIZE_KW = "batch_size"
BACKEND_BATCH_SIZE_REDUCTION_KW = "batch_size_reduction"
BACKEND_BATCH_SIZE_REDUCTION_FACTOR_KW = "batch_size_reduction_factor"
POTENTIAL_RANKMAX_KW = 'rankmax'
BACKEND_NWORKERS_KW = "n_workers"
BACKEND_PARALLEL_MODE_KW = "parallel_mode"
BACKEND_GPU_CONFIG = "gpu_config"
POTENTIAL_METADATA_KW = "metadata"
POTENTIAL_DELTASPLINEBINS_KW = "deltaSplineBins"
POTENTIAL_RADCOEFFICIENTS_KW = "radcoefficients"
POTENTIAL_RADPARAMETERS_KW = 'radparameters'
POTENTIAL_RADBASE_KW = "radbase"
POTENTIAL_NDENSITY_KW = "ndensity"
POTENTIAL_NRADBASE_KW = 'nradbase'
POTENTIAL_CUTOFF_FUNCTION_KW = 'NameOfCutoffFunction'
POTENTIAL_DCUT_KW = "dcut"
POTENTIAL_RCUT_KW = 'rcut'
POTENTIAL_FS_PARAMETERS_KW = "fs_parameters"
POTENTIAL_NPOT_KW = 'npot'
POTENTIAL_LMAX_KW = 'lmax'
POTENTIAL_NRADMAX_KW = 'nradmax'
POTENTIAL_ELEMENT_KW = "element"
POTENTIAL_BASISDF_KW = 'basisdf'
POTENTIAL_INITIAL_POTENTIAL_KW = "initial_potential"
POTENTIAL_FUNC_COEFS_INIT_KW = "func_coefs_init"  # random or zero

ORDERS_NRADMAX_KW = "nradmax_by_orders"
ORDERS_LMAX_KW = "lmax_by_orders"

ATOMIC_ENV_DF_COLUMN = "atomic_env"
TP_ATOMS_DF_COLUMN = "tp_atoms"
PYACE_EVAL = 'pyace'
TENSORPOT_EVAL = 'tensorpot'
ENERGYBASED_WEIGHTING_POLICY = "EnergyBasedWeightingPolicy"
EXTERNAL_WEIGHTING_POLICY = "ExternalWeightingPolicy"
WEIGHTING_TYPE_KW = "type"
FIT_WEIGHTING_KW = 'weighting'
FIT_LOSS_KW = "loss"
FIT_OPTIMIZER_KW = 'optimizer'
FIT_OPTIMIZER_OPTIONS_KW = 'optimizer_options'
FIT_FIT_CYCLES_KW = "fit_cycles"
FIT_LADDER_STEP_KW = 'ladder_step'
FIT_LADDER_TYPE_KW = 'ladder_type'
FIT_NOISE_REL_SIGMA = "noise_relative_sigma"
FIT_NOISE_ABS_SIGMA = "noise_absolute_sigma"

BACKEND_EVALUATOR_KW = 'evaluator'
TARGET_POTENTIAL_YAML = "target_potential.yaml"
METADATA_USER_KW = 'user'
METADATA_STARTTIME_KW = 'starttime'

# Column names: string constants
ATOMIC_ENV_COL = "atomic_env"
ENERGY_CORRECTED_COL = "energy_corrected"
ENERGY_PRED_COL = "energy_pred"
EWEIGHTS_COL = "w_energy"
FORCES_COL = "forces"
FORCES_PRED_COL = "forces_pred"
FWEIGHTS_COL = "w_forces"