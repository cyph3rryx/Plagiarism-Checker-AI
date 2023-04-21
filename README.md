# Plagiarism Checker

This is a Python script that can check for plagiarism between two text documents using Natural Language Processing (NLP) libraries such as NLTK and spaCy.

## Usage

1. Install the required libraries using pip:

``` python
pip install nltk spacy
python -m spacy download en_core_web_sm
```

2. Run the script and follow the prompts to select the files to compare:

``` python 
python plagiarism_checker.py
```

The script will compare the two files and print a message indicating whether plagiarism was detected or not.

## How it works

The script uses the following steps to check for plagiarism:

1. Preprocess the text by removing stopwords and punctuations.

2. Create document objects using spaCy.

3. Compute the similarity score using the `similarity` method of the spaCy document object.

4. If the score is above a threshold (default value is 0.8), plagiarism is detected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
