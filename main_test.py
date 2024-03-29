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
    # Bob's calls last 4 and 5 seconds respectively, average is 4.5 seconds.
    assert main(events) == ["Bob"]  # This remains correct under the 5 seconds requirement.

def test_overlapping_calls():
    events = [
        Call("Alice", "Bob", 1711132463),
        Call("Carl", "Dave", 1711132465),
        Call("Alice", "Carl", 1711132466),
        Hangup("Carl", "Dave", 1711132475),
        Hangup("Alice", "Bob", 1711132473),
        Hangup("Alice", "Carl", 1711132480),
    ]
    # Alice's and Carl's calls last longer than 5 seconds.
    assert main(events) == []  # This is correct; none average under 5 seconds.

def test_caller_with_multiple_recipients():
    events = [
        Call("Ed", "Frank", 1711132481),
        Call("Ed", "Grace", 1711132483),
        Hangup("Ed", "Frank", 1711132491),
        Hangup("Ed", "Grace", 1711132492),
    ]
    # Ed's calls last 10 and 9 seconds respectively, average is 9.5 seconds.
    assert main(events) == []  # Should be empty as Ed's average is above 5 seconds.

def test_callers_with_varied_durations():
    events = [
        Call("Bob", "Alice", 1711132463),
        Hangup("Bob", "Alice", 1711132468),  # 5 seconds
        Call("Carl", "Zoe", 1711132470),
        Hangup("Carl", "Zoe", 1711132487),  # 17 seconds
        Call("Ed", "Frank", 1711132490),
        Hangup("Ed", "Frank", 1711132500),  # 10 seconds
    ]
    # Only Bob's call is exactly 5 seconds.
    assert main(events) == []  # Bob's call duration matches 5 seconds, not under.

def test_specific_scenario():
    events = [
        Call("Bob", "Alice", 1711132463),  # 4 seconds
        Call("Carl", "Doug", 1711132465),  # 17 seconds
        Hangup("Alice", "Bob", 1711132467),
        Call("Ed", "Frank", 1711132481),  # 20 seconds
        Hangup("Carl", "Doug", 1711132482),
        Call("Bob", "Doug", 1711132483),  # 1 second
        Hangup("Doug", "Bob", 1711132484),
        Hangup("Ed", "Frank", 1711132501),
    ]
    # Bob's calls last 4 and 1 second respectively, average is 2.5 seconds.
    assert main(events) == ["Bob"]  # Correct under the 5 seconds requirement.


def test_complex_scenario_with_multiple_short_callers():
    events = [
        Call("Alice", "Bob", 1711132460),  # Alice calls Bob, 2s call
        Hangup("Alice", "Bob", 1711132462),
        
        Call("Carl", "Dave", 1711132463),  # Carl calls Dave, 4s call
        Hangup("Carl", "Dave", 1711132467),
        
        Call("Eve", "Frank", 1711132468),  # Eve calls Frank, 6s call
        Hangup("Eve", "Frank", 1711132474),
        
        Call("George", "Helen", 1711132475),  # George calls Helen, 3s call
        Hangup("George", "Helen", 1711132478),
        
        Call("Alice", "Ivan", 1711132479),  # Alice calls Ivan, 2s call (avg for Alice = 2s)
        Hangup("Ivan", "Alice", 1711132481),
        
        Call("Bob", "Carl", 1711132482),  # Bob calls Carl, 10s call
        Hangup("Bob", "Carl", 1711132492),
        
        Call("Dave", "Eve", 1711132493),  # Dave calls Eve, 4s call
        Hangup("Eve", "Dave", 1711132497),
        
        Call("Frank", "George", 1711132498),  # Frank calls George, 20s call
        Hangup("Frank", "George", 1711132518),
        
        Call("Helen", "Alice", 1711132519),  # Helen calls Alice, 1s call
        Hangup("Helen", "Alice", 1711132520),
    ]
    
    # Corrected Expectation: Including Helen for her 1s call, along with Alice, Carl, Dave, and George
    assert sorted(main(events)) == ["Alice", "Carl", "Dave", "George", "Helen"]
