# Alternating Characters

Execute the program as `ruby alternating_characters.rb`. It helps to find out if a given string follows a pattern of VOWEL to NON-VOWEL characters.

Here, the `cycle` method helps to keep switching between the VOWEL regex & the NON-VOWEL regex.
We convert the string into an array of characters with chars so that we can use the all? method.