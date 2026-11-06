"""Exercise C2: hallucination hunt helper."""


def unsupported_sentences(answer, source_text):
    src = set(source_text.lower().split())
    result = []
    for sent in answer.replace("!", ".").replace("?", ".").split("."):
        sent = sent.strip()
        if not sent:
            continue
        words = [w for w in sent.lower().split() if w.isalnum()]
        if not words:
            continue
        supported = sum(1 for w in words if w in src)
        if supported / len(words) < 0.5:
            result.append(sent)
    return result


# Try changing: modify this file and re-run the tests.
