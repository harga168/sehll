# Tambahkan semua source yang disebutkan ke dalam file api_keys.py

extended_api_keys_path = "/mnt/data/api_keys_extended_full.py"

extended_keys_content = """
# === API KEY CONFIG FILE – FULL VERSION ===

# Data Market & On-Chain
COINGECKO_API_KEY = "your_coingecko_api_key"
COINMARKETCAP_API_KEY = "your_coinmarketcap_api_key"
GLASSNODE_API_KEY = "your_glassnode_api_key"
TOKENUNLOCKS_API_KEY = "your_tokenunlocks_api_key"
INTO_THE_BLOCK_API_KEY = "your_intotheblock_api_key"
MESSARI_API_KEY = "your_messari_api_key"
NANSEN_API_KEY = "your_nansen_api_key"
ARKHAM_API_KEY = "your_arkham_api_key"
SANTIMENT_API_KEY = "your_santiment_api_key"
COINGLASS_API_KEY = "your_coinglass_api_key"
CRYPTOQUANT_API_KEY = "your_cryptoquant_api_key"
DUNE_API_KEY = "your_dune_api_key"
KAIKO_API_KEY = "your_kaiko_api_key"
TOKEN_TERMINAL_API_KEY = "your_tokenterminal_api_key"

# Bitcoin Resources / Analytics
BITNODES_API_KEY = "your_bitnodes_api_key"
BTC_FEAR_GREED_API_KEY = "your_btcfeargreed_api_key"
COIN360_API_KEY = "your_coin360_api_key"

# Smart Money / Airdrop Sources
ICODROPS_API_KEY = "your_icodrops_api_key"
CHAINBROKER_API_KEY = "your_chainbroker_api_key"
CRYPTORANK_API_KEY = "your_cryptorank_api_key"
DROPSTAB_API_KEY = "your_dropstab_api_key"
ICO_ANALYTICS_API_KEY = "your_icoanalytics_api_key"
COINLAUNCH_API_KEY = "your_coinlaunch_api_key"
CRYPTOTOTEM_API_KEY = "your_cryptototem_api_key"

# Macroeconomic Sources
TRADINGECONOMICS_API_KEY = "your_tradingeconomics_api_key"
IMF_API_KEY = "your_imf_api_key"
WORLD_BANK_API_KEY = "your_worldbank_api_key"
FED_API_KEY = "your_federalreserve_api_key"
ECB_API_KEY = "your_ecb_api_key"
OECD_API_KEY = "your_oecd_api_key"
BIS_API_KEY = "your_bis_api_key"

# Institutional Finance / Media
REUTERS_API_KEY = "your_reuters_api_key"
BLOOMBERG_API_KEY = "your_bloomberg_api_key"
WSJ_API_KEY = "your_wsj_api_key"
CNBC_API_KEY = "your_cnbc_api_key"
FT_API_KEY = "your_ft_api_key"
ECONOMIST_API_KEY = "your_economist_api_key"
MSCI_API_KEY = "your_msci_api_key"
CMEGROUP_API_KEY = "your_cmegroup_api_key"
INVESTSOCIAL_API_KEY = "your_investsocial_api_key"

# VC & Riset
DELPHI_DIGITAL_API_KEY = "your_delphidigital_api_key"
A16Z_API_KEY = "your_a16z_api_key"
ELECTRIC_CAPITAL_API_KEY = "your_electriccapital_api_key"
PANTERA_API_KEY = "your_pantera_api_key"
ARK_INVEST_API_KEY = "your_arkinvest_api_key"

# Tools / Charting / Edukasi
COOKIE_FUN_API_KEY = "your_cookiefun_api_key"
INTO_THE_CRYPTOVERSE_API_KEY = "your_intothecryptoverse_api_key"
KEVIN_ROOKE_API_KEY = "your_kevinrooke_api_key"
BUBBLEMAPS_API_KEY = "your_bubblemaps_api_key"
CANDLECHARTS_API_KEY = "your_candlecharts_api_key"
"""

# Simpan file
with open(extended_api_keys_path, "w") as f:
    f.write(extended_keys_content.strip())

extended_api_keys_path
