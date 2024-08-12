class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name
        }

    @staticmethod
    def from_dict(data):
        return User(data['user_id'], data['name'])
