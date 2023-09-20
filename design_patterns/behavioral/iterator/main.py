from iterator import *

if __name__ == '__main__':
    network: SocialNetwork = None
    spammer: SocialSpammer = SocialSpammer()

    network = Facebook()

    # spam friends
    spammer_profile = Profile('jan', 'jannn@example.com')

    iterator = network.create_friends_iterator(spammer_profile.get_id())
    spammer.send(iterator, "Very important message")
