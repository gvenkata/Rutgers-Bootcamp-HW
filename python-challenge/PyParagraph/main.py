#PyParagraph
import re
#Word Count - split sentence on space
#Sentence Count - Split paragraph on period
#Letter Count (Avg/Word)
#Avg Sentence Length (in Words)
num_words = []
num_sentences_arr = []
num_sentences = 0
total_letters = 0
avg_letters = 0
sent_words = 0
split_sent = []
avg_sent_words = 0

myfile = open("raw_data/paragraph_2.txt", "rt") 
contents = myfile.read()
myfile.close()  
#print(contents) 
 
print()
print("/*********************/")
print("/*Paragraph Analysis */")
print("/*********************/")
print()

#Sentence Count
num_sentences = len(re.split(r'[.!?]+', contents))
#print(re.split(r'[.!?]+', contents))
num_sentences_arr = re.split(r'[.!?]+', contents)

for i in range (len(num_sentences_arr)):
    split_sent = num_sentences_arr[i].split(" ")
    sent_words = len(split_sent) + sent_words

avg_sent_words =  round(sent_words/(num_sentences - 1), 2)    

#Word Count
contents = contents.replace("\n","") 
contents = contents.replace("."," ")            
num_words = contents.split(" ")
#print(num_words)

for i in range (len(num_words)):
    total_letters = len(num_words[i]) + total_letters

avg_letters = round((total_letters/(len(num_words))),2)

print("Approximate Word Count (in entire file):" + str(len(num_words)))
print("Approximate Sentence Count (in entire file):" + str(num_sentences - 1))
print("Average Letter Count (per word in file):" + str(avg_letters))   
print("Average Sentence Length in Words (for sentences in file):" + str(avg_sent_words))               





