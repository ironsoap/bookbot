def count_words(text_str):
    split_text = text_str.split()
    return len(split_text)

def count_chars(text_str):
    single_case_text = text_str.lower()
    analysis = {}
    for i in range(len(single_case_text)):
        # print(single_case_text[i])
        key_exists = single_case_text[i] in analysis
        if key_exists:
            analysis[single_case_text[i]] += 1
        else:
            analysis[single_case_text[i]] = 1

    return analysis

def enumerate_counts(counts_dict):
    list = []
    for chr in counts_dict:
        if chr.isalpha():
            cnt = counts_dict[chr]
            list.append({"char": chr, "num": cnt})
    
    return list

def sort_on(items):
    return items["num"]