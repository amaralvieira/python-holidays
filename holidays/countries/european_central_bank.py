# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase

class EuropeanCentralBank(HolidayBase):
    def __init__(self, **kwargs):
        self.country = 'ECB'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        #https://www.ecb.europa.eu/home/contacts/working-hours/html/index.en.html
        #* : TARGET closing day
        self[date(year, JAN, 1)] = "New Year's Day*"
        e = easter(year)
        self[e - rd(days=2)] = "Good Friday*"
        self[e + rd(days=1)] = "Easter Monday*"
        self[date(year, MAY, 1)] = "Labour Day*"
        self[date(year, MAY, 9)] = "Anniversary of Robert Schuman's Declaration"
        self[easter(year) + rd(days=39)] = "Ascension Day"
        self[easter(year) + rd(days=50)] = "Whit Monday"
        self[easter(year) + rd(days=60)] = "Corpus Christi"
        self[date(year, OCT, 3)] = "Day of German Unity"
        self[date(year, NOV, 1)] = "All Saints' Day"
        self[date(year, DEC, 24)] = "Christmas Eve"
        self[date(year, DEC, 25)] = "Christmas Day*"
        self[date(year, DEC, 26)] = "Christmas Holiday*"
        self[date(year, DEC, 31)] = "New Year's Eve"

class ECB(EuropeanCentralBank):
    pass

class Target2(HolidayBase):
    # https://en.wikipedia.org/wiki/TARGET2
    # http://www.ecb.europa.eu/press/pr/date/2000/html/pr001214_4.en.html

    def __init__(self, **kwargs):
        self.country = 'EU'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year >= 1999:
            self[date(year, JAN, 1)] = "New Year's Day"
            self[date(year, DEC, 25)] = "Christmas Day"

        if year > 1999:
            e = easter(year)
            self[e - rd(days=2)] = "Good Friday"
            self[e + rd(days=1)] = "Easter Monday"
            self[date(year, MAY, 1)] = "1 May (Labour Day)"
            self[date(year, DEC, 26)] = "26 December"

        if year in (1999, 2001):
            #https://www.ecb.europa.eu/press/pr/date/1999/html/pr990715_1.en.html
            #https://www.ecb.europa.eu/press/pr/date/2000/html/pr000525_2.en.html
            self[date(year, DEC, 31)] = "31 December"

class TAR(Target2):
    pass
