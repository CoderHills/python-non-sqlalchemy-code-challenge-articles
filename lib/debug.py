from classes.many_to_many import Author, Magazine, Article
import ipdb

# Create sample authors
a1 = Author("Hillary")
a2 = Author("John")

# Create sample magazines
m1 = Magazine("Tech Today", "Technology")
m2 = Magazine("Health Weekly", "Health")

# Create sample articles
art1 = Article(a1, m1, "The Rise of AI")
art2 = Article(a1, m2, "Healthy Living Tips")
art3 = Article(a1, m1, "Future of Robotics")
art4 = Article(a2, m1, "Quantum Computing 101")
art5 = Article(a2, m2, "Nutrition Facts")

print("Setup complete. Let's debug!")
ipdb.set_trace()
