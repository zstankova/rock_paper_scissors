import rps
import pytest
import subprocess
import sys

# is kontroluje hodnotu- jak ==, ale s true a false se pouziva is

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True
    
def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True
    
def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False  

def test_computer_play_is_valid():
    for _ in range(2000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(5000)]
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors)
    assert  rocks > 200
    assert  papers > 200
    assert  scissors > 200

def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'computer'

def test_rock_beats_scisors():
    result = rps.evaluate_game('rock', 'scissors')
    assert result == 'human'

def input_faked_rock(prompt):
    print(prompt)
    return 'rock'
    
@pytest.fixture
def fake_input_rock(monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_rock)

def test_full_game(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', input_faked_rock)
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()   
    assert 'rock, paper, or scissors?' in captured.out

# misto 'python' muzeme napsat sys.executable (aby se program spustil ve stejne verzi pythonu jako to piseme)

def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run(['python', 'rps.py'], encoding='utf-8', stdout=subprocess.PIPE, input='dragon\nrock\n',check=True)
    assert cp.stdout.count('rock, paper, or scissors?') == 1
    





