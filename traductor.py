main_language = "spanish"

def traductor_of_the_game():
    if main_language == "spanish":
        import languages.spanish as l
    elif main_language == "english":
        import languages.english as l
    elif main_language == "japanese":
        import languages.japanese as l
    elif main_language == "portuguese":
        import languages.portuguese as l
    elif main_language == "france":
        import languages.french as l
    elif main_language == "germany":
        import languages.germany as l
    else:
        import languages.spanish as l
    
    return l