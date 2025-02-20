
def main():
    
    # read file into variable, then count words, then print number of words.
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    length = len(file_contents.split())

    print("--- Begin report of books/frankenstein.txt ---")
    print(length, " words found in the document")
    print("\n")
 
    # itterate through every character of file, taking a total count of each character, then printing the total of each alphabetic character.
    characters = {}

    for char in file_contents:

        lowchar = char.lower()

        if characters.get(lowchar):
            characters.update({lowchar: characters.get(lowchar) + 1})
        else:
            characters.update({lowchar: 1})

    
    processed = sorted(characters, key=characters.get, reverse=True)
    
    for key in processed:
        if key.isalpha():
            print(f"The '{key}' character was found {characters[key]} times")


main()
    




