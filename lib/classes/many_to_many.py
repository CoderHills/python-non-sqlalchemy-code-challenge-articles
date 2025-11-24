class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters")
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")

    @classmethod
    def get_all_articles(cls):
        return cls.all


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("author name is of type str and cannot change")

    def articles(self):
        return self._articles if self._articles else None

    def magazines(self):
        mags = list({article.magazine for article in self._articles})
        return mags if mags else None

    def topic_areas(self):
        areas = list({article.magazine.category for article in self._articles})
        return areas if areas else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)


class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            self._name = None
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            self._category = None
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles if self._articles else None

    def contributors(self):
        authors = list({article.author for article in self._articles})
        return authors if authors else None

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        counts = {}
        for article in self._articles:
            counts[article.author] = counts.get(article.author, 0) + 1
        return [author for author, count in counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        counts = {mag: len(mag._articles) for mag in cls.all}
        max_count = max(counts.values())
        top_mags = [mag for mag, count in counts.items() if count == max_count]
        return top_mags[0] if top_mags else None
