from typing_extensions import Protocol


class Profile:
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email


class ProfileIterator(Protocol):
    def get_next(self) -> Profile:
        ...

    def has_more(self) -> bool:
        ...


class SocialNetwork(Protocol):
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        ...

    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        ...


class FacebookIterator(ProfileIterator):
    def __init__(self, facebook: "Facebook", profile_id: str, type_: str):
        self._facebook = facebook
        self._profile_id = profile_id
        self._type = type_

        self._cache: list[Profile] = []
        self._current_position: int = 0

    def _lazy_init(self):
        if not self._cache:
            self._cache = self._facebook._social_graph_request(self._profile_id, self._type)

    def get_next(self) -> Profile:
        if (self.has_more()):
            result = self._cache[self._current_position]
            self._current_position += 1
            return result

    def has_more(self) -> bool:
        self._lazy_init()
        return self._current_position < len(self._cache)


class Facebook(SocialNetwork):
    def create_friends_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")

    def _social_graph_request(self, profile_id, type):
        print(f"Here are contacts belongs to profile named : {profile_id}, {type}")
        return [
            Profile('tom', 'tom@tom.com'),
            Profile('mac', 'mac@tom.com'),
            Profile('mas', 'mas@tom.com'),
            Profile('ss', 'ss@tom.com'),
            Profile('xi', 'xi@tom.com'),
        ]


class SocialSpammer:
    def send(self, iterator: ProfileIterator, message):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f"Send email {profile.get_email()}, message : {message}")
