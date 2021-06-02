from storyRepository import RepositoryBase


class RepositoryLocal(RepositoryBase):
    _data = [
        {
            'id': 1,
            'headline': 'How to grow rich',
            'description': 'Best selling book and author, Tony Robbins',
            'story': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
            'author': 'Ron Barry',
            'published': '2017/04/15',
            'rating': 5
        },
        {
            'id': 2,
            'headline': 'Get the physique you want',
            'description': 'From lifetime coach and advisor, Jeff Cavalier',
            'story': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
            'author': 'Susie Wonder',
            'published': '2019/09/04',
            'rating': 5
        },
        {
            'id': 3,
            'headline': 'Set your boundaries',
            'description': 'Incredible stories and moral principles, Dr. Henry Cloud',
            'story': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation',
            'author': 'Michele Prince',
            'published': '2021/05/25',
            'rating': 5
        },
    ]

    def __init__(self):
        super().__init__()

    def connect(self):
        pass

    def get_story(self, story_id):
        for item in self._data:
            if item.get('id') == story_id:
                return item
        return None

    def get_stories(self):
        return self._data

    def create_story(self, story):
        self._data.append(story)

    def delete_story(self, story_id):
        for i in range(len(self._data)):
            if self._data[i].get('id') == story_id:
                self._data.pop(i)
