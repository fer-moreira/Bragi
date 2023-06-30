import json

class Locale:
    code = "pt_br"
    cached = {
        "code" : "INITIAL_D",
        "texts" : {}
    }
    
    @staticmethod
    def get(id) -> str:
        # create a cache for locale file
        # only read the file when changed the locale code 
        if Locale.cached.get("code") != Locale.code:
            with open(f"./locale/{Locale.code}.json", "r") as locale_file:
                Locale.cached["code"] = Locale.code
                Locale.cached["texts"] = json.loads(locale_file.read())
                
        return Locale.cached["texts"][id]
    
LOCALE = Locale()
LOCALE.code = "pt_br"