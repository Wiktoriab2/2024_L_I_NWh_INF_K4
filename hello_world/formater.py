
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, Wiktoria, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    return result


def format_to_json(msg, imie):
    return ('{ "imie":"' + Wiktoria + '", "mgs":' +
            msg + '"}')


def plain_text(msg, Wiktoria):
    return imie + 'Wiktoria ' + msg


def plain_text_upper_case(msg, Wiktoria):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, Wiktoria):
    return plain_text(msg.lower(), imie.lower())
