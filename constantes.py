class Constantes:
    LOGIN_PAGE = "https://www.boursedirect.fr/fr/login"

    ACCEPTER_COOKIES_BUTTON_SELECTOR = 'button:has-text("Accepter tous les cookies")'
    
    LOGIN_SELECTOR = "#bd_auth_login_type_login"
    PASSWORD_SELECTOR = "#bd_auth_login_type_password"
    SUBMIT_BUTTON_SELECTOR = 'button[type="submit"]'

    OTP_INPUTS_SELECTOR = ".code-input.react-code-input input"
    TRUST_DEVICE_SELECTOR = "#trusted"

    PTF_URL = "https://www.boursedirect.fr/fr/mon-compte/portefeuilles"
    CLOSE_BUTTON_SELECTOR = 'button:has-text("Fermer")'

    EVALUATION_TOTALE_XPATH = "/html/body/div[5]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]"