#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <map>

using namespace std;

struct Translation {
    string title, reasonPrompt, targetPrompt, savedPrompt, remaining, completed;
};

map<string, Translation> dict = {
    {"it", {"Salvadanaio Digitale", "Cosa vuoi comprare?", "Obiettivo", "Risparmiati", "Mancano", "Completato"}},
    {"en", {"Digital Piggy Bank", "What are you buying?", "Target", "Saved", "Remaining", "Completed"}},
    {"fr", {"Tirelire Numérique", "Qu'allez-vous acheter?", "Objectif", "Épargné", "Restant", "Complété"}},
    {"de", {"Sparschwein", "Was möchtest du kaufen?", "Zielbetrag", "Gespart", "Verbleibend", "Abgeschlossen"}},
    {"sp", {"Hucha Digital", "¿Qué quieres comprar?", "Objetivo", "Ahorrado", "Restante", "Completado"}}
};

void saveToFile(string reason, double target, double saved, string lang) {
    ofstream file("data.txt");
    file << reason << endl << target << endl << saved << endl << lang;
    file.close();
}

int main() {
    string lang = "it", reason, currency = "€";
    double target, saved;

    cout << "Select Language (it, en, fr, de, sp): ";
    cin >> lang;
    
    Translation t = dict[lang];
    cout << "\n--- " << t.title << " ---" << endl;

    cout << t.reasonPrompt << ": ";
    cin.ignore();
    getline(cin, reason);

    cout << t.targetPrompt << " (€): ";
    cin >> target;

    cout << t.savedPrompt << " (€): ";
    cin >> saved;

    double remaining = (target - saved > 0) ? target - saved : 0;
    double percent = (saved / target) * 100;

    cout << "\n--- RESULTS ---" << endl;
    cout << "Item: " << reason << endl;
    cout << t.remaining << ": " << fixed << setprecision(2) << remaining << "€" << endl;
    cout << t.completed << ": " << setprecision(1) << percent << "%" << endl;

    saveToFile(reason, target, saved, lang);
    cout << "\nData saved to data.txt" << endl;

    return 0;
}