# Create icalendar .icl


from icalendar import Calendar
import icalendar
from datetime import datetime, timedelta


class Event():
    def __init__(self, summary, description, duration_days):


        self.calendar = Calendar()
        self.event = icalendar.Event()

        self.calendar.add('prodid', '-//UNT Schedule Exporter//undercase//')
        self.calendar.add('version', '2.0')

        self.event['dtstart'] = icalendar.vDatetime(datetime.now())
        self.event['dtend'] = icalendar.vDatetime(datetime.now() + timedelta(days=duration_days))
        self.event['summary'] = summary
        self.event['description'] = description
        self.calendar.add_component(self.event)

        #output = open('UNT_schedule.ics', 'wb')
        #output.write(self.calendar.to_ical())
        #output.close()

    def get_ical(self):
        return self.calendar.to_ical()




if __name__ == '__main__':
    pass


