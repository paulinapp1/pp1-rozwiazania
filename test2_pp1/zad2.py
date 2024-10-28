#Utwórz funkcje f(t) która zmienia stringa z godzina zapisana w formacie 24h (np. 13:05 albo 09:02) zmienia na format 12h  (1:05pm, 9:02am)
def convert_to_12h_format(time):
    hour, minute = time.split(':')  # Rozdzielanie godziny i minut

    hour = int(hour)
    minute = int(minute)

    if hour == 0:
        return f"12:{minute:02}am"  # Jeśli godzina to 0, zmieniamy na 12am (północ)

    elif hour < 12:
        return f"{hour}:{minute:02}am"  # Jeśli godzina jest mniejsza niż 12, to jest przedpołudnie (am)

    elif hour == 12:
        return f"12:{minute:02}pm"  # Jeśli godzina to 12, to jest południe (12pm)

    else:
        return f"{hour - 12}:{minute:02}pm"  # W przeciwnym razie, konwertujemy na format popołudniowy (pm)

# Przykłady użycia funkcji
print(convert_to_12h_format("13:05"))  # Konwertuje 13:05 na 1:05pm
print(convert_to_12h_format("09:02"))  # Konwertuje 09:02 na 9:02am
