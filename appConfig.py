
# These parameters are required
INPUT_RATE_BIN = "/home/ubuntu/URDMEMining/data/rateBands.json"
INPUT_SPECIE_BIN = "/home/ubuntu/URDMEMining/data/speciesAmount.json"
INPUT_PATH = "/home/ubuntu/URDMEMining/data/dataMetaBands/"

# Skip alpha_m and alpha_m_g because the values are not varied.
RATE_TYPE = ["k1","k2","alpha_p","mu_m", "mu_p"]
SPECIE_BIN_NUMBER = 10
CONTROL_PARAM = "median"
WIN_SIZE = 4000

DEPENDENT_VARIABLE = ['k1_B0','k1_B1','k1_B2','k1_B3','k1_B4','k1_B5','k1_B6','k1_B7','k1_B8']
DEPENDENT_VARIABLE.extend(['k2_B0','k2_B1','k2_B2','k2_B3','k2_B4','k2_B5','k2_B6','k2_B7','k2_B8'])
DEPENDENT_VARIABLE.extend(['alpha_p_B0','alpha_p_B1','alpha_p_B2','alpha_p_B3','alpha_p_B4','alpha_p_B5','alpha_p_B6','alpha_p_B7','alpha_p_B8'])
DEPENDENT_VARIABLE.extend(['mu_m_B0','mu_m_B1','mu_m_B2','mu_m_B3','mu_m_B4','mu_m_B5','mu_m_B6','mu_m_B7','mu_m_B8'])
DEPENDENT_VARIABLE.extend(['mu_p_B0','mu_p_B1','mu_p_B2','mu_p_B3','mu_p_B4','mu_p_B5','mu_p_B6','mu_p_B7','mu_p_B8'])


