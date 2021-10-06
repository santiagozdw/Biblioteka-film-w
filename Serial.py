from Film import Film

class Serial(Film):
    def __init__(self, episode, season,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __str__(self) -> str:
        return f"Film (title='{self.title}', year='{self.year}', type='{self.type}', viwes='{self.views}', episode='{self.episode}' season='{self.season}')"
        # return f"{self.title} S{str(self.season).zfill(2)}E{str(self.episode).zfill(2)}"