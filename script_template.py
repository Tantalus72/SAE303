import os
import shutil

# --- Script de génération des configurations pour un site spécifique ---

def main():
    """Fonction principale du script."""
    print("--- Générateur de Configurations Réseau par Site ---")
    try:
        num = input(f"Entrez le numéro de poste pour le site : ")
    except KeyboardInterrupt:
        print("\nOpération annulée")
        return

    placeholder = f"[m]"  # Le placeholder à remplacer, ex: "[m]"
    source_dir = "M"  # Le dossier source, ex: "M"
    dest_dir = f"configs-generees-{num}" # Le dossier de destination

    # Vérifier si le dossier source existe
    if not os.path.isdir(source_dir):
        print(f"Erreur : Le dossier source '{source_dir}' est introuvable.")
        print("Assurez-vous que le script est dans le même répertoire que les dossiers M et N.")
        return

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)

    print(f"\nGénération des configurations pour le site {source_dir} avec le numéro {num}...")

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)

        if os.path.isfile(source_path):
            with open(source_path, 'r', encoding='utf-8') as f_in:
                content = f_in.read()

            # Remplacer le placeholder spécifique au site choisi
            new_content = content.replace(placeholder, num)

            with open(dest_path, 'w', encoding='utf-8') as f_out:
                f_out.write(new_content)

    print(f"Terminé ! Les configurations sont dans le dossier '{dest_dir}'.")

if __name__ == "__main__":
    main()