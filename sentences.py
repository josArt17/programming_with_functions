import random

def main():
    tenses = ['past', 'present', 'future']

    for _ in range(6):
        quantity = random.randint(1, 2)
        if quantity == 1:
          quantity_str = "single"
        else :
            quantity_str = "plural"
        

        tense = random.choice(tenses)

        print(f"{quantity_str} - {tense}")
        make_sentence(quantity, tense)
        print()


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sec_prepositional_phrase = get_prepositional_phrase(quantity)
    adverb = get_adverb()
    

    sentence = f"{determiner} {noun} {verb} {prepositional_phrase} {adverb.lower()} {sec_prepositional_phrase}"
    print(sentence)

def get_determiner(quantity):
    """Return a randomly chosen determiner.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word.capitalize()

def get_noun(quantity):
    """Return a randomly chosen noun.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb.
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    return random.choice(verbs)


def get_preposition():
    prepo = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    return random.choice(prepo)


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase = f"{preposition} {determiner.lower()} {noun}"
    return phrase

def get_adverb():
 adverb = ["Quickly", "Much", "Sweetly", "Often", "Regularly", "Now", "Mostly", "Barely", "Casually", "Nearly", "Inside", "Easily",
           "Early", "Later", "In", "Accidentally", "Successfully", "Nicely", "Probably", "Down", "Possibly"]
 
 return random.choice(adverb)

main()

       