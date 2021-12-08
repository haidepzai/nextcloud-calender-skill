from mycroft import MycroftSkill, intent_file_handler
import caldav

caldav_url = "https://nextcloud.humanoidlab.hdm-stuttgart.de/remote.php/dav"

class NextcloudCalender(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        
    def initialize(self):
        self.log.info('Collecting login information')

        self.user = self.settings.get('username')
        if not self.user:
            self.log.info('Failed to retrieve username')

        self.password = self.settings.get('password')
        if not self.password:
            self.log.info('failed to retrieve password')
            
        client = caldav.DAVClient(url=caldav_url, username=self.user, password=self.password)
            

    @intent_file_handler('calender.nextcloud.intent')
    def handle_calender_nextcloud(self, message):
        self.speak_dialog('calender.nextcloud')


def create_skill():
    return NextcloudCalender()

