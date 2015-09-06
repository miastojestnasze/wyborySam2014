#!/usr/bin/python
# coding=UTF-8


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

dictionary_base = {
    "number_of_voters": "Liczba wyborców",
    "number_of_proxies": "Liczba wyborców głosujących przez pełnomocnika",
    "cards_given": "Wydane karty",
    "cards_taken": "Karty wyjęte z kopert na karty do głosowania",
    "cards_taken_from_box": "Karty wyjęte z urny",
    "votes_valid": "Głosy ważne",
    "votes_invalid": "Głosy nieważne",
    "cards_received": "Otrzymane karty",
    "cards_valid": "Karty ważne",
    "cards_invalid": "Karty nieważne",
    "cards_invalid_x": "w tym z powodu niepostawienia znaku „X” obok nazwiska żadnego kandydata",
    "cards_invalid_xx": "w tym z powodu postawienia znaku „X” obok nazwiska dwóch lub większej liczby kandydatów",
    "cards_unused": "Niewykorzystane karty",
    "polish_citizens": "w tym obywatele polscy",
    "polish_citizens_b": "w tym w części A spisu wyborców (obywatele polscy)",
    "type": "Typ",
    "number_of_district": "Nr okr.",
    "teryt": "TERYT",
    "envelope_unsealed": "Niezaklejona koperta na kartę do głosowania",
    "envelopes_thrown_into_box": "Koperty na kartę do głosowania wrzucone do urny",
    "envelopes_without_statement": "Koperty  bez oświadczenia",
    "envelopes_returned": "Koperty zwrotne",
    "envelopes_returned_without_envelope": "Koperty zwrotne bez koperty na kartę do głosowania",
    "unsigned_statements": "Niepodpisane oświadczenie",
    "address": "Adres",
    "eu_citizens": "w tym obywatele UE niebędący obywatelami polskimi",
    "eu_citiznes_b": "w tym w części B spisu wyborców (obywatele UE niebędący obywatelami polskimi)",
    "number_of_electoral_circuit": "Nr obw.",
    "number_electoral_circuits": "Liczba obwodów",
    "electoral_packages": "Pakiety wyborcze",
    "district": "Dzielnica"
}

dictionary_parties = {
    "kww1": "Komitet Wyborczy Stowarzyszenia Wawer",
    "kww2": "Komitet Wyborczy Wyborców Razem dla Ochoty",
    "kww3": "Komitet Wyborczy Wyborców Gwiaździsta",
    "kww4": "Komitet Wyborczy Wyborców Włochy- Miasto Ogród",
    "kww5": "Komitet Wyborczy Stowarzyszenia Zwykłego Nasz Targówek",
    "kww6": "Komitet Wyborczy Rembertów Bezpośbrednio",
    "kww7": "Komitet Wyborczy Wyborców FORUM DLA REMBERTOWA",
    "kww8": "Komitet Wyborczy Wyborców Ochocka Wspólnota Samorządowa",
    "kww9": "Komitet Wyborczy Stowarzyszenia Mieszkańców Miasteczka Wilanów",
    "kww10": "Komitet Wyborczy Stowarzyszenia Sąsiedzkie Włochy",
    "kww11": "Komitet Wyborczy Wyborców Wola Zmian",
    "kww12": "Komitet Wyborczy Warszawska Wspólnota Samorządowa",
    "kww13": "Komitet Wyborczy Wyborców Inicjatywa Mieszkańców Białołęki",
    "kww14": "Koalicyjny Komitet Wyborczy SLD Lewica Razem",
    "kww15": "Komitet Wyborczy Wyborców \"Mieszkańcy Bródna - Targówka- Zacisza\"",
    "kww16": "Komitet Wyborczy Wyborców Andrzeja Rozenka",
    "kww17": "Komitet Wyborczy Wyborcóww Patriotyzm i Kultura",
    "kww18": "Komitet Wyborczy Stowarzyszenie Sąsiedzkie Stara Miłosna \"Sąsiedzi dla Wesołej\"",
    "kww19": "Komitet Wyborczy Wyborców Inicjatywa Mieszkańców Mokotowa",
    "kww20": "Komitet Wyborczy Wyborców Inicjatywa Mieszkańców Ursynowa ",
    "kww21": "Komitet Wyborczy Wyborców Miasto Jest Nasze - Targówek Zacisze Bródno",
    "kww22": "Komitet Wyborczy Stowarzyszenie Obywatelskie w Ursusie",
    "kww23": "Komitet Wyborczy Wyborców Miasto Jest Nasze-Mieszkańców Śródmieścia",
    "kww24": "Komitet Wyborczy Wyborców \"Wspólnota Dzielnicy Włochy\"",
    "kww25": "Komitet Wyborczy Wyborców Projekt Żoliborz",
    "kww26": "Komitet Wyborczy Wyborców Wawerska Inicjatywa Samorządowa",
    "kww27": "Komitet Wyborczy Wyborców WESOŁA 2014",
    "kww28": "Komitet Wyborczy Wyborców \"Ochocianie\"",
    "kww29": "Komitet Wyborczy Stowarzyszenia \"Lepszy Rembertów\"",
    "kww30": "Komitet Wyborczy Wyborców Miasto jest Nasze - Mieszkańcy Bielan",
    "kww31": "Komitet Wyborczy Stowarzyszenia Nasz Ursynów",
    "kww32": "Komitet Wyborczy Wyborców Ruch Sprawiedliwości Społecznej - Piotr Ikonowicz",
    "kww33": "Komitet Wyborczy Wyborców Miasto Jest Nasze #\u017boliborz",
    "kww34": "Komitet Wyborczy Warszawa Społeczna",
    "kww35": "Komitet Wyborczy Bemowska Wspólnota Samorządowa",
    "kww36": "Komitet Wyborczy Wyborców Jarosław Dąbrowski burmistrzem DLA BEMOWA",
    "kww37": "Komitet Wyborczy Wyborców Razem Dla Ursusa",
    "kww38": "Komitet Wyborczy Wyborców Wspólnota Samorządowa Gospodarność",
    "kww39": "Komitet Wyborczy Nowa Prawica \u2014 Janusza Korwin-Mikke",
    "kww40": "Komitet Wyborczy Wyborców Nowoczesne Bielany",
    "kww41": "Komitet Wyborczy Wyborców Miasto Jest Nasze - Mieszkańców Pragi",
    "kww42": "Komitet Wyborczy Wyborców Inicjatywa Mieszkańców Miasto Jest Nasze",
    "kww43": "Komitet Wyborczy Wyborców Praska Wspólnota Samorządowa",
    "kww44": "Komitet Wyborczy Wyborców Mieszkańcy Rembertowa",
    "kww45": "Komitet Wyborczy Platforma Obywatelska RP",
    "kww46": "Komitet Wyborczy Prawo i Sprawiedliwość"
}

dictionary_candidates_president = {
    "prez": "WRZESIŃSKI Zbigniew Antoni",
    "prez1": "SASIN Jacek Robert",
    "prez2": "WIERZBICKI Sebastian", 
    "prez3": "NOSAL-IKONOWICZ Agata Alina", 
    "prez4": "GRONKIEWICZ-WALTZ Hanna Beata", 
    "prez5": "ROZENEK Andrzej Tadeusz",
    "prez6": "DZIERŻAWSKI Mariusz Andrzej",
    "prez7": "GORAYSKI Andrzej Józef",
    "prez8": "ERBEL Joanna Agnieszka",
    "prez9": "WIPLER Przemysław Janusz", 
    "prez10": "GUZIAŁ Piotr Andrzej",
}

dictionary_candidates = {
    "surname": "Nazwisko",
    "teryt": "TERYT",
    "nationality": "Obywatelstwo",
    "names": "Imiona",
    "age": "Wiek",
    "grade": "Szczebel",
    "number_of_district": "Nr\nokr.",
    "number_of_list": "Nr\nlisty",
    "place_of_living": "Miejsce zam.",
    "voivodeship": "Nazwa",
    "sex": "Płeć",
    "votes": "Głosy",
    "election_committee": "Komitet",
    "pos": "Poz."
}

dictionary_voivodeship = {
    "county": "Powiat",
    "commune": "Gmina",
    "voivodeship": "Województwo",
    "commune_type": "Typ gminy"
}

#remove '\n' from keys!!!!!
dictionary_voivodeship_council = {
    "kw": "Komitet Wyborczy Wyborców Ruch Narodowy",
    "kw1": "Komitet Wyborczy Demokracja Bezpośrednia",
    "kw2": "Komitet Wyborczy Związku Słowiańskiego",
    "kw3": "Komitet Wyborczy Twój Ruch",
    "kw4": "Komitet Wyborczy Narodowego Odrodzenia Polski",
    "kw5": "Komitet Wyborczy Samoobrona",
    "kw6": "Koalicyjny Komitet Wyborczy SLD Lewica Razem",
    "kw7": "Komitet Wyborczy Nowa Prawica — Janusza Korwin-Mikke",
    "kw8": "Komitet Wyborczy Wyborców Wspólnota Patriotyzm Solidarność",
    "kw9": "Komitet Wyborczy Mazowiecka Wspólnota Samorządowa",
    "kw10": "Komitet Wyborczy Platforma Obywatelska RP",
    "kw11": "Komitet Wyborczy Polskie Stronnictwo Ludowe",
    "kw12": "Komitet Wyborczy Prawo i Sprawiedliwość",
    "kw13": "Komitet Wyborczy Oburzeni",
    "kw14": "Komitet Wyborczy Wyborców Współpraca i Partnerstwo",
}

dictionary_city_council = {
    "kwc": "Komitet Wyborczy Inicjatywa Mieszkańców Warszawy",
    "kwc1": "Komitet Wyborczy Wyborców Warszawa Dla Rodziny",
    "kwc2": "Komitet Wyborczy Wyborców Andrzeja Rozenka",
    "kwc3": "Komitet Wyborczy Warszawska Wspólnota Samorządowa",
    "kwc4": "Komitet Wyborczy Demokracja Bezpośrednia",
    "kwc5": "Komitet Wyborczy Partia Zieloni",
    "kwc6": "Komitet Wyborczy Wyborców Ruch Sprawiedliwości Społecznej - Piotr Ikonowicz",
    "kwc7": "Komitet Wyborczy Warszawa Społeczna",
    "kwc8": "Koalicyjny Komitet Wyborczy SLD Lewica Razem",
    "kwc9": "Komitet Wyborczy Nowa Prawica — Janusza Korwin-Mikke",
    "kwc10": "Komitet Wyborczy Wyborców Wspólnota Patriotyzm Solidarność",
    "kwc11": "Komitet Wyborczy Platforma Obywatelska RP",
    "kwc12": "Komitet Wyborczy Prawo i Sprawiedliwość",
    "kwc13": "Komitet Wyborczy Związku Sybiraków",
    "kwc14": "Komitet Wyborczy Wyborców Krzysztofa Bieleckiego",
    "kwc15": "Komitet Wyborczy Wyborców Współpraca i Partnerstwo",
}

decoder = merge_dicts(dictionary_base, dictionary_parties,
                      dictionary_candidates_president, dictionary_candidates,
                      dictionary_voivodeship, dictionary_voivodeship_council,
                      dictionary_city_council)


coder = {v: k for k, v in decoder.iteritems()}
