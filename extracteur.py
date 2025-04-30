from playwright.sync_api import sync_playwright
from constantes import Constantes
import time

class ExtracteurDePortefeuille:

    @staticmethod
    def extrait_solde(utilisateur: str, mot_de_passe: str, otp_code: str = None, headless: bool = True) -> str:
        with sync_playwright() as p:
            navigateur = p.chromium.launch(headless=headless)
            page = navigateur.new_page()

            page.goto(Constantes.LOGIN_PAGE)
            try:
                page.wait_for_selector(Constantes.ACCEPTER_COOKIES_BUTTON_SELECTOR, timeout=5000)
                page.click(Constantes.ACCEPTER_COOKIES_BUTTON_SELECTOR)
            except:
                pass  

            page.fill(Constantes.LOGIN_SELECTOR, utilisateur)
            page.fill(Constantes.PASSWORD_SELECTOR, mot_de_passe)
            page.click(Constantes.SUBMIT_BUTTON_SELECTOR)
            if otp_code:
                page.wait_for_selector(Constantes.OTP_INPUTS_SELECTOR, timeout=10000)
                otp_inputs = page.query_selector_all(Constantes.OTP_INPUTS_SELECTOR)
                page.check(Constantes.TRUST_DEVICE_SELECTOR)
                for i, chiffre in enumerate(otp_code[:6]):
                    otp_inputs[i].fill(chiffre)

            page.wait_for_timeout(2000)
            page.goto(Constantes.PTF_URL)
            if page.is_visible(Constantes.CLOSE_BUTTON_SELECTOR):
                page.click(Constantes.CLOSE_BUTTON_SELECTOR, timeout=5000)
            
            page.wait_for_timeout(2000)
            solde = page.locator(f"xpath={Constantes.EVALUATION_TOTALE_XPATH}").inner_text()
            navigateur.close()
            return solde
