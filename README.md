# Wordscapes

This project is a solver for the game Wordscapes. It generates all possible words from a given set of characters and checks them against a dictionary to find valid words.

## Project Structure
```
data/ words_alpha.txt words_dictionary.json README.md solve.py
```


- [`data/words_alpha.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fdata%2Fwords_alpha.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/data/words_alpha.txt"): A text file containing a list of words.
- [`data/words_dictionary.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fdata%2Fwords_dictionary.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/data/words_dictionary.json"): A JSON file containing a dictionary of valid words.
- [`README.md`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/README.md"): This file.
- [`solve.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fsolve.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/solve.py"): The main script to run the solver.

## How to Use

1. **Install Dependencies**: Ensure you have Python installed. This script uses the [`json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fsolve.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A7%7D%7D%5D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "Go to definition") and [`itertools`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fsolve.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A5%7D%7D%5D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "Go to definition") libraries, which are included in the Python Standard Library.

2. **Prepare the Dictionary**: Ensure that [`data/words_dictionary.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fdata%2Fwords_dictionary.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/data/words_dictionary.json") is populated with valid words. You can use the `words_alpha.txt` to generate this JSON file if needed.

3. **Run the Solver**: Execute the [`solve.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fduc%2Fstudy%2Fwordscapes%2Fsolve.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22275c6c38-e368-4953-be03-bd7a30b235cb%22%5D "/Users/duc/study/wordscapes/solve.py") script.

```sh
python solve.py
```

Input Characters: When prompted, enter the characters from your Wordscapes puzzle.

View Results: The script will output all valid words that can be formed from the given characters.

## Example
```
$ python solve.py
Enter a word: example
['amp', 'ape', 'axle', 'exam', 'lamp', 'leap', 'male', 'maple', 'pal', 'pale', 'peal', 'plea']
```

## Functions
load_json_from_file(file_path)
Loads a JSON file from the specified path.

generate_words(chars)
Generates all possible permutations of the given characters and returns a list of unique words.

## License
This project is licensed under the MIT License.