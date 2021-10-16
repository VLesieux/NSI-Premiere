#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Competitor` module

:author: `FIL - Département Informatique - Université de Lille <http://portail.fil.univ-lille1.fr>`_

:date: Juin, 2019

Module for competitor representation.
A competitor

"""



def create (first_name, last_name, sex, birth_date, bib_num):
    """
    
    :param first_name: first name of a competitor
    :type name: string
    :param last_name: last name of a competitor
    :type name: string
    :param sex: sex of a competitor 'M' or 'F'
    :type name: string
    :param birth_date: birth date of the competitor, format is "DD/MM/YYY"
    :type birth_date: string
    :param bib_num: bib number of the competitor
    :type bib_num: int    
    :return: a new record for this competitor
    :rtype: Competitor
    :UC: bib_num > 0 and sex in 'MF'
    """
    assert bib_num > 0 and sex in 'MF'
    return {
        'bib_num' : bib_num,
        'first_name' : first_name,
        'last_name' : last_name,
        'sex' : sex,
        'birth_date' : birth_date,
        'performance' : None
    }

def get_firstname (comp):
    """
    
    :param comp:
    :type comp: Competitor
    :return: first name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['first_name']

def get_lastname (comp):
    """
    
    :param comp:
    :type comp: Competitor
    :return: last name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['last_name']

def get_birthdate (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: birthdate of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['birthdate']

def get_bib_num (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: bib number of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['bib_num']

def get_performance (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: performance of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['performance']


def get_sex (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: sex of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['sex']

def set_performance (comp, d):
    """

    :param comp: competitor to be modified
    :type comp: Competitor
    :param d: performance of competitor comp
    :type d: time
    :return: None
    :Side effect: performance of competitor comp is modified with value d
    :UC: none
    """
    comp['performance'] = d

def to_string(competitor):
    """
    :param competitor: a competitor
    :type comp: Competitor
    :return: a string represnetation for given competitor
    """
    return "[{bib_num}]: {first_name} {last_name} ({sex} - {birth_date}) ".format(**competitor)


    
if __name__ == '__main__':
    pass    


