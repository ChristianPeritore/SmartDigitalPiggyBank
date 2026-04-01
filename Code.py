import json
import os

# Dizionario completo delle traduzioni
translations = {
    "it": {
        "title": "Salvadanaio Digitale",
        "reason": "Cosa vuoi comprare?",
        "target": "Obiettivo Totale",
        "saved": "Budget Attuale",
        "btn": "Calcola",
        "rem": "Ti mancano:",
        "perc": "Accumulato:",
        "done": "Completato",
        "missing": "Mancante"
    },
    "en": {
        "title": "Digital Piggy Bank",
        "reason": "What are you buying?",
        "target": "Total Target",
        "saved": "Current Budget",
        "btn": "Calculate",
        "rem": "Remaining:",
        "perc": "Saved:",
        "done": "Completed",
        "missing": "Missing"
    },
    "fr": {
        "title": "Ma Tirelire",
        "reason": "Qu'allez-vous acheter?",
        "target": "Objectif Total",
        "saved": "Argent Épargné",
        "btn": "Calculer",
        "rem": "Il vous reste:",
        "perc": "Accumulé:",
        "done": "Complété",
        "missing": "Manquant"
    },
    "de": {
        "title": "Sparschwein",
        "reason": "Was möchtest du kaufen?",
        "target": "Gesamtbetrag",
        "saved": "Gespartes Geld",
        "btn": "Berechnen",
        "rem": "Noch zu sparen:",
        "perc": "Gespart:",
        "done": "Abgeschlossen",
        "missing": "Fehlend"
    },
    "sp": {
        "title": "Mi Hucha Digital",
        "reason": "¿Qué quieres comprar?",
        "target": "Meta Total",
        "saved": "Dinero Ahorrado",
        "btn": "Calcular",
        "rem": "Te faltan:",
        "perc": "Acumulado:",
        "done": "Completado",
        "missing": "Faltante"
    }
}

def load_data():
    if os.path.exists("piggy_data.json"):
        with open("piggy_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_data(data):
    with open("piggy_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    # Caricamento dati precedenti
    old_data = load_data()
    
    print("--- Configuration / Configurazione ---")
    if old_data:
        print(f"(Last session / Ultima sessione: {old_data['reason']})")
    
    # Scelta Lingua
    lang = input("Language (it, en, fr, de, sp): ").lower().strip()
    if lang not in translations:
        print("Language not supported, defaulting to English.")
        lang = "en"
    
    t = translations[lang]
    
    # Scelta Valuta
    currency = input("Currency / Valuta (€, $, £): ").strip() or "€"

    print(f"\n{'='*30}")
    print(f" {t['title']} ")
    print(f"{'='*30}\n")
    
    # Input utente
    reason = input(f"{t['reason']}: ")
    target = float(input(f"{t['target']} ({currency}): "))
    saved = float(input(f"{t['saved']} ({currency}): "))

    # Calcoli
    remaining = max(0, target - saved)
    percent_saved = min(100, (saved / target) * 100)
    percent_missing = 100 - percent_saved

    # Output Risultati
    print(f"\n--- {reason.upper()} ---")
    print(f"{t['rem']} {currency} {remaining:.2f} ({percent_missing:.1f}%)")
    print(f"{t['perc']} {percent_saved:.1f}% {t['done']}")
    
    # "Grafico" a barre testuale per impatto visivo
    bar_length = 20
    filled = int(bar_length * percent_saved / 100)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"[{bar}] {percent_saved:.1f}%")

    # Salvataggio
    data_to_save = {
        "reason": reason,
        "target": target,
        "saved": saved,
        "lang": lang,
        "currency": currency
    }
    save_data(data_to_save)
    print(f"\n[Data saved to piggy_data.json]")

if __name__ == "__main__":
    main()