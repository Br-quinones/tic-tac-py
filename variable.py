main_language = "spanish"

def traductor_of_the_game():
    if main_language == "spanish":
        import languages.es as l
    elif main_language == "english":
        import languages.en as l
    elif main_language == "japanese":
        import languages.ja as l
    else:
        import languages.es as l
    
    return l