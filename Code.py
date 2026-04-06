import os

class PiggyBank:
    def __init__(self):
        self.history = []
        self.target = 0.0
        self.saved = 0.0
        self.lang = "en"
        
        self.translations = {
            "it": {"title": "Salvadanaio Digitale", "target": "Target Totale", "current": "Budget Attuale", "missing": "Mancano", "saved": "Accumulato", "history": "Cronologia"},
            "en": {"title": "Digital Piggy Bank", "target": "Total Target", "current": "Current Budget", "missing": "Remaining", "saved": "Saved", "history": "History Log"},
            "fr": {"title": "Ma Tirelire", "target": "Cible Totale", "current": "Budget Actuel", "missing": "Restant", "saved": "Accumulé", "history": "Historique"},
            "de": {"title": "Sparschwein", "target": "Gesamtziel", "current": "Aktuelles Budget", "missing": "Fehlend", "saved": "Gespart", "history": "Verlauf"},
            "sp": {"title": "Mi Hucha Digital", "target": "Meta Total", "current": "Ahorro Actual", "missing": "Faltante", "saved": "Acumulado", "history": "Historial"}
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_screen()
        t = self.translations[self.lang]
        missing = max(0, self.target - self.saved)
        percent = (self.saved / self.target * 100) if self.target > 0 else 0
        
        print(f"{'='*40}")
        print(f"{t['title'].center(40)}")
        print(f"{'='*40}")
        print(f"{t['missing']}: {missing:.2f}")
        print(f"{t['saved']}: {percent:.1f}%")
        print(f"{'-'*40}")
        print(f"{t['history']}:")
        for entry in reversed(self.history[-5:]):
            print(f" > {entry:.2f}")
        print(f"{'='*40}")

    def run(self):
        self.lang = input("Language (it/en/fr/de/sp): ").lower()
        if self.lang not in self.translations: self.lang = "en"
        
        self.target = float(input(f"{self.translations[self.lang]['target']}: "))
        
        while True:
            try:
                val = input(f"{self.translations[self.lang]['current']} (or 'q' to quit): ")
                if val.lower() == 'q': break
                
                self.saved = float(val)
                self.history.append(self.saved)
                self.display()
            except ValueError:
                print("Invalid input!")

if __name__ == "__main__":
    bank = PiggyBank()
    bank.run()
