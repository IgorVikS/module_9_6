def all_variants(text):
    for i in range(1, len(text) + 1):
        j = 0
        while j < len(text):
            if j + i <= len(text):
                yield (text[j:j + i])
            j += 1

a = all_variants("abc")
for i in a:
    print(i)