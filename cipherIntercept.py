from collections import Counter
import os

os.system('pip install nltk')
try:
    import nltk
except ImportError:
    os.system('pip install nltk')
nltk.download('wordnet')

from nltk.corpus import wordnet

first = True
text = ""
#English letter frequencies
with open("freq.txt", "r") as file:
    freqs = [line.strip() for line in file]

def freq(text):
    text = text.lower()
    filtered = ''.join([c for c in text if c.isalpha()])
    counts = Counter(filtered)
    return ''.join(sorted(counts, key=counts.get, reverse=True))

def build_dict(c_freq, e_freq):
    return {c: p for c, p in zip(c_freq, e_freq)}

def decrypt(ct, sub_dict):
    pt = ''
    for ch in ct:
        if ch.lower() in sub_dict:
            pt += sub_dict[ch.lower()].upper() if ch.isupper() else sub_dict[ch]
        else:
            pt += ch
    return pt

def solve():
    biggest = 0
    best_text = ''
    best_dict = {}
    with open('input.txt', 'r') as f:
        ct = f.read()
    c_freq = freq(ct)
  
    results = {}
    #iterate over and take note of the decryption with most correct words
    for index, e_freq in enumerate(freqs, start=1):
        sub_dict = build_dict(c_freq, e_freq)
        pt = decrypt(ct, sub_dict)
        recog_words = 0
        for word in pt.split():
          if wordnet.synsets(word):
            recog_words += 1
        results[index] = recog_words
        if recog_words > biggest:
            biggest = recog_words
            best_text = pt
            best_dict = sub_dict
  
    return best_text, best_dict, ct 

def manual_adjustment(text, sub_dict, ciphertext):
  print("\nCurrent text:", text)
  print("Current substitution dictionary:", sub_dict)
  while True:
      change = input("Enter two letters to swap (e.g., 'a t' to swap 'a' with 't'), or 'done' to finish: ")
      if change.lower() == 'done':
          break
      try:
          old, new = change.split()
          if len(old) == 1 and len(new) == 1 and old in sub_dict.values() and new in sub_dict.values():
              # Swap values
              old_key = next(key for key, value in sub_dict.items() if value == old)
              new_key = next(key for key, value in sub_dict.items() if value == new)
            
              sub_dict[old_key], sub_dict[new_key] = sub_dict[new_key], sub_dict[old_key]

              # Decrypt original with new dictionary
              text = decrypt(ciphertext, sub_dict)
              print("\nUpdated text:", text)
          else:
              print("Invalid input")
      except ValueError:
          print("Please enter exactly two letters separated by a space.")
      except:
          pass

  return text

best_text, best_dict, ct = solve()
final_text = manual_adjustment(best_text, best_dict, ct)
print("Final adjusted text:")
print(final_text)