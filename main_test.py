from Hiya import main
from Hiya import CallEvent
from Hiya import Call
from Hiya import Hangup



def test_multiple_calls_by_same_caller():
    events = [
        Call("Bob", "Alice", 1711132463),
        Call("Bob", "Dave", 1711132465),
        Hangup("Bob", "Alice", 1711132467),
        Hangup("Bob", "Dave", 1711132470),
    ]
    assert main(events) == ["Bob"]

def test_overlapping_calls():
    events = [
        Call("Alice", "Bob", 1711132463),
        Call("Carl", "Dave", 1711132465),
        Call("Alice", "Carl", 1711132466),
        Hangup("Carl", "Dave", 1711132475),
        Hangup("Alice", "Bob", 1711132473),
        Hangup("Alice", "Carl", 1711132480),
    ]
    assert main(events) == []

def test_caller_with_multiple_recipients():
    events = [
        Call("Ed", "Frank", 1711132481),
        Call("Ed", "Grace", 1711132483),
        Hangup("Ed", "Frank", 1711132491),
        Hangup("Ed", "Grace", 1711132492),
    ]
    assert main(events) == ["Ed"]

def test_callers_with_varied_durations():
    events = [
        Call("Bob", "Alice", 1711132463),
        Hangup("Bob", "Alice", 1711132468),
        Call("Carl", "Zoe", 1711132470),
        Hangup("Carl", "Zoe", 1711132487),
        Call("Ed", "Frank", 1711132490),
        Hangup("Ed", "Frank", 1711132500),
    ]
    assert main(events) == ["Bob"]

def test_specific_scenario():
    events = [
        Call("Bob", "Alice", 1711132463),
        Call("Carl", "Doug", 1711132465),
        Hangup("Alice", "Bob", 1711132467),
        Call("Ed", "Frank", 1711132481),
        Hangup("Carl", "Doug", 1711132482),
        Call("Bob", "Doug", 1711132483),
        Hangup("Doug", "Bob", 1711132484),
        Hangup("Ed", "Frank", 1711132501),
    ]
   
    assert main(events) == ["Bob"]