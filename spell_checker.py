from spellchecker import SpellChecker

spell = SpellChecker()

def cek_kata(word):
    if word in spell:
        return word, [] 
    else:
        katabenar = spell.correction(word)
        sugesti = list(spell.candidates(word))
        return katabenar, sugesti

def main():
    print("Welcome to the Spell Checker App!")
    while True:
        # Get user input
        word = input("Enter a word to check (type exit or quit for exit the program): ").lower()
        
        if word in ('exit', 'quit'):
            print("Exiting the Spell Checker App. Goodbye!")
            break
        
        # Check the spelling of the entered word
        katabenar, sugesti = cek_kata(word)
        
        # Output the result
        print(f"Corrected word: {katabenar}")
        print(f"Suggested corrections: {', '.join(sugesti)}")

if __name__ == "__main__":
    main()
