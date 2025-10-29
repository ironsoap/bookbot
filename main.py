from stats import *
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_text = get_book_text(sys.argv[1])
		book_words = count_words(book_text)
		# book_chars = count_chars(book_text)
		# print(book_chars)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ----------")
		print(f"Found {book_words} total words")
		print("--------- Character Count -------")
		book_chars = count_chars(book_text)
		counts = enumerate_counts(book_chars)
		#print(counts.sort(reverse=True, key=sort_on))
		counts.sort(reverse=True, key=sort_on)
		#print(counts)
		for i in counts:
			print(f"{i['char']}: {i['num']}")
		print("============= END ===============")

main()