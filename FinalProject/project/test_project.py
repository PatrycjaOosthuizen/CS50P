from project import select_country, question, get_result
import pyfiglet
import pytest


def test_select_country():
    assert select_country(['Albania (+355)']) == ('Albania', '+355')
    assert select_country(['Albania  +355']) == None
    assert select_country(['Albania 355']) == None
    assert select_country(['American Samoa (+1-684)']) == ('American Samoa', '+1-684')
    assert select_country(['American Samoa +1-684']) == None
    assert select_country(['American Samoa 1-684']) == None
    assert select_country(['Dominican Republic (+1-809, 1-829, 1-849)']) == ('Dominican Republic', '+1-809, 1-829, 1-849')
    assert select_country(['Dominican Republic +1-809, 1-829, 1-849']) == None
    assert select_country(['Dominican Republic 1-809, 1-829, 1-849']) == None



def test_question():
    assert question('Brazil') == ['_','_','_','_','_','_']
    assert question('brazil') == ['_','_','_','_','_','_']
    assert question('El Salvador') == ['_','_',' ','_','_','_','_','_','_','_','_']
    assert question('Guinea-Bissau') == ['_','_','_','_','_','_','-','_','_','_','_','_','_']


def test_get_result():
    assert get_result(True) == pyfiglet.figlet_format('Correct, well done !', font='standard', width=210)
    assert get_result(False) == pyfiglet.figlet_format('Incorrect, try again !', font='standard', width=210)
