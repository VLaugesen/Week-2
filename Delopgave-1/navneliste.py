# %%
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import statistics

def perform_analysis(name_list):
    """
    Takes a list of names and counts the frquencies of each letter as well as different name lengths.
    Returns two dictionaries with the corresponding mapping.
    """
    letters = {}
    lengths = {}

    for name in name_list:
        length = len(name)
        lengths[length] = lengths.get(length, 0) + 1
        for letter in name:
            letters[letter] = letters.get(letter, 0) + 1
    return letters, lengths

# %%
with open(os.path.join("..", "Data", "Navneliste.txt")) as file:
    names = file.read().lower().split(',')
    names_no_duplicates = list(set(names))

    print("Sorted alphabetically:", sorted(names))
    print("Sorted by length:", sorted(names, key=str.__len__))
 
    letters, lengths = perform_analysis(names)
    letters_no_duplicates, lengths_no_duplicates = perform_analysis(names_no_duplicates)
    

    print(letters)

# %%
def plot_wordcloud(letters):
    """
    Generate a wordcloud based on the frequence of each letter.
    Doesn't seem to be working correctly, as some letters appear twice with others missing.
    Fixing it has been downprioritized due to time.
    """
    letter_cloud = ""
    # Try to use the provided dictionary to create a string containing 
    # single letter "words" matching the frequencies for the WordCloud package
    for item in letters:
        letter_cloud += (item + " ") * letters[item]
    wordcloud = WordCloud().generate(letter_cloud)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# %%
plot_wordcloud(letters)

# %%
def plot_dicts(letters, lengths):
    """"
    Plots the frequencies of each letter in the total name list as a bar plot,
    sorted both alphabetically as well as by frequency.
    Additionally plots frequency of lengths for each full name.
    """
    fig, axs = plt.subplots(3, figsize=(8, 6))

    # Sorting the plot alphabetically by letter
    xs, ys = zip(*sorted(letters.items()))
    axs[0].bar(xs, ys)

    # Sorting the plot by frequencies
    xs, ys = zip(*sorted(letters.items(), key=lambda item: item[1], reverse=True))
    axs[1].bar(xs, ys)

    axs[2].bar(lengths.keys(), lengths.values())

    plt.show()

# %%
plot_dicts(letters, lengths)


