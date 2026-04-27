import re
import regex as re

source_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# print("source_text:", source_text.lower())

text_lower = source_text.lower()

sentences = re.split(r' *[\.\u00A0\n\?!][\'"\)\]\s]*', text_lower)

capitalized_sentences: list = []
fixed_case_text = text_lower

for sentence in sentences:
    capitalized_sentences.append(sentence.capitalize())

for d in capitalized_sentences:
    for h in sentences:
        if d.lower() == h:
            fixed_case_text = fixed_case_text.replace(h, d)

    print(fixed_case_text)
    print(capitalized_sentences)

new_sentence_words:list = []
last_sentence_words:list = []
new_sentence_list: list = []

for sentence in sentences:
    new_sentence_words.append(sentence.split())

for j in new_sentence_words:
    if len(j) > 1:
        new_sentence_list.append(j[-1])

new_sentence = (' '.join(new_sentence_list)).capitalize() + '.'


text_with_new_sentence = fixed_case_text.replace('Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.', 'Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.'+' '+new_sentence)

final_text = text_with_new_sentence.replace(" iz", " is")

spaces = re.findall('\s+', final_text)
spaces_amount:int = 0

for i in range(0, len(spaces)):
    spaces_amount = len(spaces)

print(final_text)
print(spaces_amount)



