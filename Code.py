import datetime

class Salvadanaio:
    def __init__(self, obiettivo_nome, target):
        self.obiettivo_nome = obiettivo_nome
        self.target = target
        self.budget_attuale = 0.0
        self.cronologia = []

    def aggiorna_budget(self, nuovo_importo):
        differenza = nuovo_importo - self.budget_attuale
        self.budget_attuale = nuovo_importo
        data_ora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
        
        # Registra la transazione
        transazione = {
            "data": data_ora,
            "importo_totale": self.budget_attuale,
            "variazione": differenza
        }
        self.cronologia.append(transazione)
        self.mostra_stato()

    def mostra_stato(self):
        mancanti = max(0, self.target - self.budget_attuale)
        percentuale = min(100, (self.budget_attuale / self.target) * 100)
        
        print(f"\n--- {self.obiettivo_nome} ---")
        print(f"Target: {self.target:.2f}€")
        print(f"Stato attuale: {self.budget_attuale:.2f}€ ({percentuale:.1f}%)")
        print(f"Mancano: {mancanti:.2f}€")
        print("-" * 20)
        print("Ultimi movimenti:")
        for t in self.cronologia[-5:]:  # Mostra gli ultimi 5
            segno = "+" if t['variazione'] >= 0 else ""
            print(f"[{t['data']}] {segno}{t['variazione']:.2f}€")