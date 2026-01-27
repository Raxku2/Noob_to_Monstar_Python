# 🧵 Project_43: String Manipulation Challenges

**Author: Pinaka**

---

## 🎯 Project Goal

Strings are everywhere.

If loops train your **structure thinking**,
strings train your **precision thinking**.

This project sharpens your ability to:

* inspect characters
* transform text
* validate input
* build logic-heavy features

Most **real-world bugs** happen in string handling.

---

## 🧠 Why String Manipulation Is Critical

Strings are used in:

* user input
* passwords & validation
* logs
* APIs
* filenames
* parsing data
* CLI tools
* web apps

If you master strings →
you control **data flow**.

---

## 🧱 Core String Concepts (Quick Recall)

| Concept    | Example              |
| ---------- | -------------------- |
| Indexing   | `s[0]`, `s[-1]`      |
| Slicing    | `s[1:5]`             |
| Length     | `len(s)`             |
| Looping    | `for ch in s:`       |
| Membership | `"a" in s`           |
| Methods    | `lower()`, `split()` |

---

## 🟢 Challenge 1: Reverse a String

### Task

Input a string and print it reversed.

### Solution

```python
text = input("Enter text: ")
print(text[::-1])
```

### 🧠 Logic

* slicing with step `-1`
* fastest & pythonic

---

## 🟢 Challenge 2: Count Vowels & Consonants

### Solution

```python
text = input("Enter text: ").lower()

vowels = "aeiou"
v = c = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
```

### 🧠 Learning

* filtering characters
* `isalpha()` matters
* real input ≠ clean input

---

## 🟢 Challenge 3: Check Palindrome

### Solution

```python
text = input("Enter text: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

### 🧠 Insight

* preprocessing input is key
* ignore spaces & case

---

## 🟢 Challenge 4: Word Frequency Counter

### Solution

```python
text = input("Enter sentence: ").lower()
words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
```

### 🧠 Used In

* search engines
* NLP
* log analysis
* SEO tools

---

## 🟢 Challenge 5: Capitalize First Letter of Each Word

### Solution

```python
text = input("Enter text: ")

result = ""
capitalize = True

for ch in text:
    if ch == " ":
        capitalize = True
        result += ch
    else:
        if capitalize:
            result += ch.upper()
            capitalize = False
        else:
            result += ch.lower()

print(result)
```

### 🧠 Why Not `.title()`?

Because **real control beats shortcuts**.

---

## 🟡 Challenge 6: Mask Sensitive Data (Password Style)

### Task

Convert:

```
mypassword123 → ***********123
```

### Solution

```python
text = input("Enter password: ")
masked = "*" * (len(text) - 3) + text[-3:]
print(masked)
```

---

## 🟡 Challenge 7: Check Anagram

### Solution

```python
a = input("Enter first word: ").replace(" ", "").lower()
b = input("Enter second word: ").replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")
```

---

## 🔴 Challenge 8: Compress String (Basic Encoding)

### Input

```
aaabbccccd
```

### Output

```
a3b2c4d1
```

### Solution

```python
text = input("Enter text: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)
print(result)
```

### 🧠 Used In

* compression
* encoding
* interview problems

---

## 🧪 Practice Challenges (DO THESE)

### 🟡 Practice 1

Remove duplicate characters:

```
banana → ban
```

---

### 🟡 Practice 2

Find longest word in a sentence.

---

### 🟡 Practice 3

Check if string has **all unique characters**.

---

### 🔴 Practice 4 (Advanced)

Build a **CLI username validator**:

* min 6 chars
* no spaces
* must contain number
* must start with letter

---
