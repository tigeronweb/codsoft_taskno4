from collections import defaultdict


users = {
    "Harry": [("Harry Potter", 5), ("Spider Man", 4), ("James Bond", 3)],
    "Tobi": [("Harry Potter", 4), ("The Dark Knight", 5), ("Two States", 3)],
    "Ethan": [("James Bond", 5), ("Two States", 4), ("World War One", 3)],
    "Veer": [("James Bond", 5), ("Two States", 5), ("The Dark Knight", 3)],
    "Tommy": [("Harry Potter", 3), ("The Dark Knight", 3), ("World War One", 3)],
    "Jolly": [("James Bond", 5), ("Two States",  3), ("Harry Potter", 4)],
    "Bob": [("Harry Potter", 4), ("Harry Potter", 3), ("World War One", 5)],
    "Bean": [("James Bond", 5), ("Two States", 4), ("The Dark Knight", 3)],
    "Elon": [("James Bond", 4), ("Harry Potter", 4), ("Spider Man", 3)],
}

books = {
    "Harry Potter": {"genre": "fantasy", "keywords": ["magic", "adventure"]},
    "Spider Man": {"genre": "sci-fi", "keywords": ["space", "aliens"]},
    "James Bond": {"genre": "mystery", "keywords": ["detective", "crime"]},
    "The Dark Knight": {"genre": "thriller", "keywords": ["suspense", "action"]},
    "Two States": {"genre": "romance", "keywords": ["love", "relationships"]},
    "World War One": {"genre": "historical fiction", "keywords": ["war", "history"]},
}


def create_user_vector(user_data):
    user_vector = defaultdict(int)
    for book, rating in user_data:
        for keyword in books[book]["keywords"]:
            user_vector[keyword] += rating
    return user_vector


def create_book_vector(book_data):
    book_vector = defaultdict(int)
    for keyword in book_data["keywords"]:
        book_vector[keyword] = 1
    return book_vector


def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1.values(), vec2.values()))
    mag1 = sum(v * v for v in vec1.values()) ** 0.5
    mag2 = sum(v * v for v in vec2.values()) ** 0.5
    if mag1 * mag2 == 0:
        return 0
    return dot_product / (mag1 * mag2)


user_vectors = {user: create_user_vector(data) for user, data in users.items()}
book_vectors = {book: create_book_vector(data) for book, data in books.items()}


def recommend_books(user, n=3):
    user_vec = user_vectors[user]
    similarities = {book: cosine_similarity(user_vec, book_vec) for book, book_vec in book_vectors.items() if book not in [b[0] for b in users[user]]}
    sorted_sims = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return sorted_sims[:n]


user = "Harry"
recommendations = recommend_books(user)
print(f"Recommendations for {user}:")
for book, similarity in recommendations:
    print(f"- {book} ({similarity:.2f})")
