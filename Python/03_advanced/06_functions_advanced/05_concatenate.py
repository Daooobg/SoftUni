def concatenate(*args, **kwargs):
    text = ''

    for word in args:
        text += word

    for k, v in kwargs.items():
        while k in text:
            text = text.replace(k, v)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))