
#!/usr/bin/python3

def find_ana(search_w="", n_words=0, f_name=""):
  # transformar el string a lista en minusculas
  sort_s_word = list(search_w.lower())
  print(sort_s_word)
  # volvemos la lista a string con las letras ordenadas alfabeticamente
  sort_s_word = "".join(sorted(sort_s_word))
  print(sort_s_word)
  with open(f_name, mode='r+', encoding='utf-8') as f:
    words = f.read()
    words = words.split()
    c_words = len(words)
    for n in range(1, n_words + 1):
      print("==============================================")
      print("************* With {:d} words ****************".format(n))
      offset = 0
      while (offset + n - 1  < c_words):
        anag = ("".join(words[offset:n + offset])).lower()
        anag = "".join(sorted(list(anag)))
        if sort_s_word == anag:
          words.insert(offset, "[")
          words.insert(offset + n + 1, "]")
          print(" ".join(words[offset + 1: n + offset + 1]))
          offset += 2

        offset += 1

    with open("copy_" + f_name, mode="w", encoding="utf-8") as f2:
      f2.write(" ".join(words))



find_ana("Holberton", 3, "text.txt")