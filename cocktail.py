from textgenrnn import textgenrnn
textgen = textgenrnn()
textgen.train_from_file('cocktail.txt', num_epochs=3)
textgen.generate_to_file('cocktail-new.txt', n=1000)
