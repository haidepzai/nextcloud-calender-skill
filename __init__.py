from mycroft import MycroftSkill, intent_file_handler


class NextcloudCalender(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calender.nextcloud.intent')
    def handle_calender_nextcloud(self, message):
        self.speak_dialog('calender.nextcloud')


def create_skill():
    return NextcloudCalender()

