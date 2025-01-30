adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
quantity_letter_h = adwentures_of_tom_sawer.count("h")
print(f"Quantity of letter h is {quantity_letter_h}")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_capital_letters =0
for letter in adwentures_of_tom_sawer:
    status = letter.isupper()
    if status:
        count_capital_letters+=1
print(f"Quantity of capital letters is {count_capital_letters}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_Tom_start = adwentures_of_tom_sawer.find("Tom")
index_Tom = adwentures_of_tom_sawer.find("Tom", index_Tom_start+3)
print(f"Tom appeared secondly at position {index_Tom}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
count_sentence = 0
splited_text = adwentures_of_tom_sawer.split(".")
for sentence in splited_text:
    adwentures_of_tom_sawer_sentences = splited_text[count_sentence]
    adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences.strip()
    print(adwentures_of_tom_sawer_sentences)
    count_sentence +=1
general_quantity_of_sentences = len(splited_text)-1

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences = splited_text[general_quantity_of_sentences-2].strip()
adwentures_of_tom_sawer_sentences_lower = adwentures_of_tom_sawer_sentences.lower()
print(adwentures_of_tom_sawer_sentences_lower)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in splited_text:
    sentence = sentence.strip()
    status_sentence = sentence.startswith("By the time")
    if status_sentence:
        status = sentence
print(f"Sentence that starts with \"By the time\" is {status}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = splited_text[general_quantity_of_sentences-1]
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_sentences.strip()
quantity_words_list = adwentures_of_tom_sawer_sentences.split()
quantity_words = len(quantity_words_list)
print(f"Quantity of words in the last sentence is {quantity_words}")