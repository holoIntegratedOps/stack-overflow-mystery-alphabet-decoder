# Stack Overflow Challenge - Mystery Alphabet Decoder

This is a solution to the [Challenge #15: Mystery Alphabet Decoder](https://stackoverflow.com/beta/challenges/79866337/challenge-15-mystery-alphabet-decoder).

## Table of contents

- [Stack Overflow Challenge - Mystery Alphabet Decoder](#stack-overflow-challenge---mystery-alphabet-decoder)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
    - [The challenge](#the-challenge)
    - [Links](#links)
  - [My process](#my-process)
    - [Tool \& Technology](#tool--technology)
    - [What I learned](#what-i-learned)
    - [Continued development](#continued-development)
    - [Useful resources](#useful-resources)
  - [Author](#author)
  - [Acknowledgments](#acknowledgments)

## Overview

### The challenge

You've intercepted pieces of a dictionary from an unknown civilization. You have managed to get a list of words which you know that are sorted alphabetically according to their language's alphabet. But you don't know what order their letters go in. You are tasked with figuring out the alphabetical order of all the symbols used in this language.

**Rules**  

- The dictionary is sorted just like any normal dictionary (e.g. ant comes before trout)
- If one word is a prefix of another (like "car" and "cart"), the shorter one comes first
- All symbols appear in the dictionary and there is no capitalization
- All correct responses will be designated as winners
- The challenge deadline is February 11, 2025
- Please include your code as well as a small description of your approach and anything interesting you encountered
- Your entry is not permitted to be written by AI. For any feedback on this Challenge, please head over to the feedback post on Meta.

### Links

- [Solution URL](https://github.com/holoIntegratedOps/stack-overflow-mystery-alphabet-decoder)
- [Live Site URL](https://projects.holointegratedops.site/stack-overflow-mystery-alphabet-decoder/)

## My process

Following GeeksForGeeks explaination method, I compare the letters of two lines of words. I pick the first position where they are differ, I append them to form set data. I did the same on the each two line till I got to the end of line. To ease the process I used a [python script](./utils/script.py) to achieve my target. The script take in the giving [words](./docs/mystery_alphabet.txt) and perform the infer on it and finally produce the [result](./docs/reconstructed_alphabet.txt).

### Tool & Technology

- python

### What I learned

I have learnt to used automated script to solve programming problems/challenges, with the help of Python documentations and programming communities, I came up with this script to extract the matching words.

To see how you can add code snippets, see below:

```py
def infer(file_path):
    try:
        edges = set()
        # check if file exist
        if not os.path.exists(file_path):
            print("Error: File does not exist.")
            return
        # read file content
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        # pick line
        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
        # compare each words
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    edges.add((word1[i], word2[i]))
                    break
        return edges
    # error handling
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    # file closure
    finally:
        if f is not None and not f.closed:
            f.close()
```

### Continued development

In my first upload, I knew my solution was correct but at least I was about to create a script that help to automate the infer processig despite that I do not understand the language of the giving words. Thanks to [Amance](https://stackoverflow.com/users/17142551/amance) for correction and update tips

### Useful resources

- [GeeksForGeeks](https://www.geeksforgeeks.org/dsa/given-sorted-dictionary-find-precedence-characters/) - This helped me to understand the content of the challenge and how to solve it.

## Author

- Website - [](https://www.holointegratedops.site)
- StackOverflow - [@yourusername](https://www.frontendmentor.io/profile/yourusername)

## Acknowledgments

I gave credibility to [Geeksforgeeks](https://www.geeksforgeeks.org/) for the amazing documentations and video tutorial, I also acknowlege the programmering communities for the hint and tips for creating my python infer automated script.

Thanks to [Amance](https://stackoverflow.com/users/17142551/amance) for correction and update tips
