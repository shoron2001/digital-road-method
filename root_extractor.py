# -*- coding: utf-8 -*-
import re

def extract_algorithmic_root(word):
    if not isinstance(word, str):
        return []
    cleaned = re.sub(r'^(mu|ma|ta|ya|a|al)', '', word.lower())
    cleaned = re.sub(r'(in|un|an|at|oon|een)$', '', cleaned)
    root_vector = [char for char in cleaned if char.isalpha()]
    return root_vector

if __name__ == "__main__":
    print("--- Section 6 & 7: Root Vector Extraction Pipeline ---")
    test_words = ["masjid", "sujud", "sajidin"]
    for w in test_words:
        print(f"Linguistic Token: {w: <8} -> Extracted Root Vector R: {extract_algorithmic_root(w)}")
