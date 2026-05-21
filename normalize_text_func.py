import regex as re

def make_text_lower_case(text_to_lower):
    return text_to_lower.lower()

def split_text_into_sentences(text_to_split):
    return re.split(r' *[.\u00A0\n?!][\'")\]\s]*', text_to_split)

def capitalize_sentences(sentences_to_capitalize):
    capitalized_sentences: list = []
    for sentence in sentences_to_capitalize:
        capitalized_sentences.append(sentence.capitalize())
    return capitalized_sentences

def replace_with_capitalized_sentences(lower_case_only_text, capitalize_sentences_list, lower_case_sentences):
    fixed_case_text = lower_case_only_text
    for d in capitalize_sentences_list:
        for h in lower_case_sentences:
            if d.lower() == h:
                fixed_case_text = fixed_case_text.replace(h, d)
    return fixed_case_text

def create_list_of_last_words(sentences_to_find_last_words):
    new_sentence_words: list = []
    for sentence in sentences_to_find_last_words:
        new_sentence_words.append(sentence.split())
    return new_sentence_words

def create_new_sentence(words_to_create_new_sentence):
    new_sentence_list: list = []
    for j in words_to_create_new_sentence:
        if len(j) > 1:
            new_sentence_list.append(j[-1])
    return (' '.join(new_sentence_list)).capitalize() + '.'

def count_spaces(text_to_count_whitespaces):
    spaces = re.findall('\\s+', text_to_count_whitespaces)
    return len(spaces)

if __name__ == "__main__":

    source_text = """homEwork:
      tHis iz your homeWork, copy these Text to variable.
    
    
    
      You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
    
    
    
      it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
    
    
    
      last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


    lower_case_only_text = make_text_lower_case(source_text)

    lower_case_sentences = split_text_into_sentences(lower_case_only_text)

    capitalize_sentences_list = capitalize_sentences(lower_case_sentences)

    fully_fixed_case_text = replace_with_capitalized_sentences(lower_case_only_text, capitalize_sentences_list, lower_case_sentences)

    words_for_new_sentence_lower_case =  create_list_of_last_words(lower_case_sentences)

    new_sentence = create_new_sentence(words_for_new_sentence_lower_case)

    text_with_new_sentence = fully_fixed_case_text.replace('Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.', 'Also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.'+' '+new_sentence)

    final_text = text_with_new_sentence.replace(" iz", " is")

    all_spaces_amount = count_spaces(final_text)

    print(final_text)
    print(all_spaces_amount)



