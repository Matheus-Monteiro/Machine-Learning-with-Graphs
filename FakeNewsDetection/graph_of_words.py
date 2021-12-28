from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def get_graphs(path_abs, label):

	stop_words = set(stopwords.words('portuguese')) 
	lemmatizer = WordNetLemmatizer()
	number_of_files = 3500
	graphs, y = [], []
	
	for k in tqdm(range(0, number_of_files)):
	
		sentences = []
		vertex = dict()
		N = 1

		path = path_abs + str(k) + '.txt'

		try:
			with open(path,'r') as f:
				for line in f:
					for word in line.split():
						word = word.lower()
						if word not in stop_words:
							word = lemmatizer.lemmatize(word)
							sentences.append(word)
							if word not in vertex:
								vertex[word] = N 
								N += 1
		
			g = [[0 for x in range(N)] for y in range(N)] 

			for i in range(0, len(sentences)):
				for j in range(i + 1, min(len(sentences), i + 3)):
				
					u = vertex[ sentences[i] ]
					v = vertex[ sentences[j] ]
					g[u][v] = 1
					g[v][u] = 1

			graphs.append(g.copy())
			y.append(label)
		
		except FileNotFoundError:
			pass
	
	return graphs, y

def graph_of_words(flag):

	graphs, label = [], []

	if flag == False:
		path = 'Fake.br-Corpus/size_normalized_texts/'
	else:
		path = 'Fake.br-Corpus/full_texts/'
	
	print('Generating Graphs of the true news')
	g_true, y_true = get_graphs(path + 'true/', 1)

	print('Generating Graphs of the fake news')
	g_fake, y_fake = get_graphs(path + 'fake/', 0)

	print(len(g_true))
	print(len(y_true))
	print(len(g_fake))
	print(len(y_fake))

	
if __name__ == "__main__":
	graph_of_words(False)