import sys
from extracteur import ExtracteurDePortefeuille

def main():
    utilisateur = "XXXXXX"
    mot_de_passe = "XXXXXX"
    otp_code = "XXXXXX"

    if len(sys.argv) == 4:
        utilisateur = sys.argv[1]
        mot_de_passe = sys.argv[2]
        otp_code = sys.argv[3]
    elif len(sys.argv) != 1:
        print("Utilisation : python3 main.py [login password otp]")
        sys.exit(1)

    solde = ExtracteurDePortefeuille.extrait_solde(
        utilisateur=utilisateur,
        mot_de_passe=mot_de_passe,
        otp_code=otp_code,
        headless=False
    )
    print("Solde total :", solde)

if __name__ == "__main__":
    main()
