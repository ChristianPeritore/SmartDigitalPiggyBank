#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

struct Translation {
    string title, goal, target, current, calc, remaining, accumulated, completed, trend, history, clear;
};

map<string, Translation> dict = {
    {"it", {"Salvadanaio Digitale", "Obiettivo", "Target Totale", "Budget Attuale", "Salva e Aggiorna", "Mancano", "Accumulato", "Completato", "Andamento Budget", "Cronologia", "Svuota"}},
    {"en", {"Digital Piggy Bank", "Goal", "Total Target", "Current Budget", "Save & Update", "Remaining", "Saved", "Completed", "Budget Trend", "History Log", "Clear"}},
    {"fr", {"Ma Tirelire", "Objectif", "Cible Totale", "Budget Actuel", "Sauver", "Restant", "Accumulé", "Complété", "Tendance", "Historique", "Effacer"}},
    {"de", {"Sparschwein", "Sparziel", "Gesamtziel", "Aktuelles Budget", "Speichern", "Fehlend", "Gespart", "Abgeschlossen", "Verlauf", "Verlauf", "Löschen"}},
    {"sp", {"Mi Hucha Digital", "Meta", "Meta Total", "Ahorro Actual", "Guardar", "Faltante", "Acumulado", "Completado", "Tendencia", "Historial", "Limpiar"}}
};

void displayInterface(string lang, double target, double saved, const vector<double>& history) {
    Translation t = dict[lang];
    double missing = (target - saved > 0) ? target - saved : 0;
    double percent = (target > 0) ? (saved / target) * 100 : 0;

    cout << "\n========================================" << endl;
    cout << "       " << t.title << "       " << endl;
    cout << "========================================" << endl;
    cout << t.remaining << ": " << fixed << setprecision(2) << missing << endl;
    cout << t.accumulated << ": " << percent << "% (" << t.completed << ")" << endl;
    cout << "----------------------------------------" << endl;
    cout << ">>> " << t.history << ":" << endl;
    
    for (int i = history.size() - 1; i >= 0 && i >= (int)history.size() - 5; --i) {
        cout << " - Entry " << i + 1 << ": " << history[i] << endl;
    }
    cout << "========================================\n" << endl;
}

int main() {
    string lang = "en";
    double target = 0, saved = 0, input;
    vector<double> history;

    cout << "Select Language (it, en, fr, de, sp): ";
    cin >> lang;
    if (dict.find(lang) == dict.end()) lang = "en";

    cout << dict[lang].target << ": ";
    cin >> target;

    while (true) {
        cout << dict[lang].current << " (Enter -1 to quit): ";
        cin >> input;
        if (input == -1) break;

        saved = input;
        history.push_back(saved);
        displayInterface(lang, target, saved, history);
    }

    return 0;
}
