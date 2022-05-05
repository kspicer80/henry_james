import re
import spacy

def annotate(xml):
    # xml matches the pattern above
    if xml[1] == "/":
        return xml[2:-1] + "-end"

    else:
        return xml[1:-1] + "-start"

def strip_word(word, matches, nlp, stripped, all_tokens, no_space, annotations):
    pattern_start = re.compile("<[a-zA-Z_]+>")
    pattern_end = re.compile("</[a-zA-Z_]+>")
    w_annotations = []
    for match in matches:
        w_annotations.append(annotate(match))
    splitted_start = re.split(pattern_start, word)
    # TODO: we assume no word contains more than one annotation
    if len(splitted_start) > 1:
        prefix, rest = splitted_start
        if prefix:
            tokens = list(nlp(prefix))
            all_tokens.extend(tokens)
            # The prefix requires space before, but the tag itself not
            no_space[len(stripped) + 1] = True
            stripped.append(prefix)
    else:
        rest = splitted_start[0]
    splitted_end = re.split(pattern_end, rest)
    tag = splitted_end[0]
    stripped.append(tag)
    tokens = list(nlp(tag))
    n_tokens = len(all_tokens)
    for j, _ in enumerate(tokens):
        annotations[n_tokens + j] = w_annotations
    all_tokens.extend(tokens)
    if len(splitted_end) > 1:
        suffix = splitted_end[1]
        if suffix:
            tokens = list(nlp(suffix))
            all_tokens.extend(tokens)
            no_space[len(stripped)] = True
            stripped.append(suffix)

def split_annotations(txt, nlp):
    pattern = re.compile("</?[a-zA-Z_]+>")
    original_words = txt.split()
    stripped = []
    # A mapping between token index and its annotations
    annotations = {}
    all_tokens = []
    # A mapping between stripped_words index and
    # whether it's preceded by a space
    no_space = {}
    for word in original_words:
        matches = re.findall(pattern, word)
        if matches:
            strip_word(word, matches, nlp, stripped, all_tokens, no_space, annotations)
        else:
            stripped.append(word)
            tokens = list(nlp(word))
            all_tokens.extend(tokens)

    return (stripped, annotations, no_space)

def reassemble_txt(stripped_words, no_space):
    stripped_txt = stripped_words[0]
    for i, word in enumerate(stripped_words[1:]):
        if i + 1 in no_space:
            stripped_txt += word
        else:
            stripped_txt += " " + word

    return stripped_txt

def main():
    nlp = spacy.load("en")
    txt = "<personName>Harry Potter</personName> goes to \
        <orgName>Hogwarts</orgName>. <personName>Sally</personName> \
        lives in #<locationName>London</locationName>."
    stripped_words, annotations, no_space = split_annotations(txt, nlp)
    stripped_txt = reassemble_txt(stripped_words, no_space)
    doc = nlp(stripped_txt)
    n_tokens = 0
    print(txt)
    for sent_ind, sent in enumerate(doc.sents):
        print("sentence{}: {}".format(sent_ind, sent))
        for tok in list(sent):
            if n_tokens in annotations:
                anns = annotations[n_tokens]
            else:
                anns = []
            print("\t token{}: {}, annotations: {}".format(n_tokens, tok, anns))
            n_tokens += 1

if __name__ == "__main__":
    main()
