import os
import re
import socket
from collections import Counter

# Directory and file paths
base_path = '/home/data'
output_file_path = '/home/output/result.txt'
file1_path = os.path.join(base_path, 'IF.txt')
file2_path = os.path.join(base_path, 'Limerick-1.txt')

# Function to count words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content)
        return len(words)

# Function to find top 3 words with counts
def top_words(file_path, n=3):
    with open(file_path, 'r') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content)
        word_counts = Counter(words)
        return word_counts.most_common(n)

# List all text files in the directory
file_list = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

# Count total number of words in each text file
total_words_file1 = count_words(file1_path)
total_words_file2 = count_words(file2_path)

# Calculate the grand total
grand_total_words = total_words_file1 + total_words_file2

# Find the top 3 words with counts in IF.txt
top_words_list = top_words(file1_path)

# Find the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())

# Write all the output to the result.txt file
with open(output_file_path, 'w') as output_file:
    output_file.write(f"List of text files in {base_path}:\n{file_list}\n\n")
    output_file.write(f"Total number of words in {file1_path}: {total_words_file1}\n")
    output_file.write(f"Total number of words in {file2_path}: {total_words_file2}\n")
    output_file.write(f"Grand total number of words: {grand_total_words}\n\n")
    output_file.write(f"Top 3 words in {file1_path} with counts: {top_words_list}\n\n")
    output_file.write(f"IP address of the machine: {ip_address}\n")

# Print the information on the console
with open(output_file_path, 'r') as output_file:
    print(output_file.read())
