from nltk.tokenize import sent_tokenize, word_tokenize 
  
text = "Natural language processing (NLP) is a field of computer science, artificial intelligence and computational linguistics concerned with the interactions between computers and human (natural) languages, and, in part involve natural language understanding, natural language generation (frequently from formal, machine-readable logical forms), connecting language and machine perception, managing human-computer dialog systems, or some combination thereof."
  
print(sent_tokenize(text)) 
print(word_tokenize(text)) 