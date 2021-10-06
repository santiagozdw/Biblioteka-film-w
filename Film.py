class Film:
    def __init__(self, title, year, type, views) -> None:
        self.title = title
        self.year = year
        self.type = type
        self.views = views

    def __str__(self) -> str:
        return f"Film (title='{self.title}', year='{self.year}', type='{self.type}', views='{self.views}')"
        # return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1