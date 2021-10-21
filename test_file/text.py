from pprint import pprint


a = [
    "vsdjklsdjfksdljkflsd\n",
    "sjfksdjfsiodfjiods\n"
]

with open('text_text.txt', 'w') as f:
    f.writelines(a)