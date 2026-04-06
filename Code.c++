#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

struct Transazione {
    std::string data;
    double variazione;
    double totale_dopo;
};

class Salvadanaio {
private:
    std::string obiettivo;
    double target;
    double budgetAttuale;
    std::vector<Transazione> cronologia;

public:
    Salvadanaio(std::string obj, double trg) : obiettivo(obj), target(trg), budgetAttuale(0.0) {}

    void aggiorna(double nuovoImporto) {
        double diff = nuovoImporto - budgetAttuale;
        budgetAttuale = nuovoImporto;

        // In C++ reale useresti <chrono>, qui simuliamo la stringa data
        Transazione t = {"06/04/2026", diff, budgetAttuale};
        cronologia.push_back(t);
        mostraReport();
    }

    void mostraReport() {
        double mancanti = std::max(0.0, target - budgetAttuale);
        double perc = (budgetAttuale / target) * 100.0;

        std::cout << "\n========== " << obiettivo << " ==========" << std::endl;
        std::cout << "Completato: " << std::fixed << std::setprecision(2) << perc << "%" << std::endl;
        std::cout << "Mancano: " << mancanti << " EUR" << std::endl;
        std::cout << "------------------------------------" << std::endl;
        std::cout << "CRONOLOGIA MOVIMENTI:" << std::endl;

        for (const auto& t : cronologia) {
            std::string segno = (t.variazione >= 0) ? "+" : "";
            std::cout << t.data << " | " << segno << t.variazione << " EUR" << std::endl;
        }
    }
};

int main() {
    Salvadanaio mioSalva("Vacanza", 2000.0);
    
    mioSalva.aggiorna(500.0);  // Aggiunta
    mioSalva.aggiorna(1200.0); // Aggiunta
    mioSalva.aggiorna(1100.0); // Perdita/Spesa

    return 0;
}