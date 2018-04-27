categories = {}
import sys
from nltk.corpus import wordnet as wn
import os    


def main():

	files_in_dir = os.listdir('v1')
	for file_in_dir in files_in_dir:
		fp = open('v1' + '/'+file_in_dir).readlines()

		for line in fp:
			if '[' in line:
				words = line.split()
				for w in words:
					if '[' in w:
						values = w.split('[')
						#print values
						if values[0] != '' and values[1] != '':
							x = values[1].index(']')
							cat = values[1][:x]
							adj = values[0]
							if cat not in categories:
								categories[cat] = []
							categories[cat].append(adj)

							# append synsets
							for i in wn.synsets(adj): 
								#if i.pos() in ['a', 's']: # If synset is adj or satelite-adj.
									for j in i.lemmas():  # Iterating through lemmas for each synset.

										# append synonyms
										syn = str(j.name())
										if syn not in categories[cat]:
											categories[cat].append(syn)

										# append antonyms
										if j.antonyms():  # If adj has antonym.
											ant = str(j.antonyms()[0].name())
											if ant not in categories[cat]:
												categories[cat].append(ant)

	for c in categories:
		categories[c] = list(set(categories[c]))
	#	print c, ':', categories[c]

	# fp = open("cat_dict.txt","w")
	# fp.write("categories = ")
	# fp.write(str(categories))

	return categories


if __name__ == '__main__':
	main()