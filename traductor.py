main_language = "spanish"

def traductor_of_the_game():
    if main_language == "spanish":
        import languages.es as l
    elif main_language == "english":
        import languages.en as l
    elif main_language == "japanese":
        import languages.ja as l
    elif main_language == "portuguese":
        import languages.pt as l
    elif main_language == "france":
        import languages.fr as l
    elif main_language == "germany":
        import languages.de as l
    else:
        import languages.es as l
    
    return l