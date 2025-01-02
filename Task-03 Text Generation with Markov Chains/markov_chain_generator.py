import random

# Function to build a Markov Chain model
def build_markov_chain(text, n=2):
    """
    Build a Markov Chain model based on n-grams.
    Args:
        text (str): The input text dataset.
        n (int): The size of the n-gram (default is bigram).
    Returns:
        dict: A dictionary representing the Markov Chain.
    """
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)

    return markov_chain

# Function to generate text using the Markov Chain model
def generate_text(chain, n=2, length=50):
    """
    Generate text using the Markov Chain model.
    Args:
        chain (dict): The Markov Chain model.
        n (int): The size of the n-gram.
        length (int): Number of words to generate.
    Returns:
        str: The generated text.
    """
    start_key = random.choice(list(chain.keys()))
    generated_words = list(start_key)

    for _ in range(length - n):
        key = tuple(generated_words[-n:])
        if key in chain:
            next_word = random.choice(chain[key])
            generated_words.append(next_word)
        else:
            break

    return ' '.join(generated_words)

# Function to read dataset from a file
def read_dataset(file_path):
    """
    Read the dataset from a text file.
    Args:
        file_path (str): Path to the text file.
    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Main execution
if __name__ == "__main__":
    # Prompt user to input dataset type
    input_type = input("Enter 'file' to provide a dataset file or 'text' to input a string: ").strip().lower()

    if input_type == 'file':
        file_path = input("Enter the file path: ").strip()
        try:
            dataset = read_dataset(file_path)
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
            exit()
    elif input_type == 'text':
        dataset = input("Enter the text dataset: ").strip()
    else:
        print("Invalid input. Please enter 'file' or 'text'.")
        exit()

    # Prompt user to choose n-gram size
    n_gram_size = int(input("Enter the n-gram size (1 for unigram, 2 for bigram, 3 for trigram): ").strip())

    # Build Markov Chain model
    chain = build_markov_chain(dataset, n=n_gram_size)

    # Generate text
    text_length = int(input("Enter the number of words to generate: ").strip())
    generated_text = generate_text(chain, n=n_gram_size, length=text_length)

    # Output the generated text
    print("\nGenerated Text:")
    print(generated_text)
