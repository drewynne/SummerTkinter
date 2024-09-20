import pytest
from Game_Components.Game import Game
from Game_Components.Question_Types.Question import Question
from Game_Components.RoundRunner import RoundRunner


@pytest.fixture
def game_fixture():
    game = Game(5)
    return game


def test_game_constructor(game_fixture):
    assert game_fixture.start_difficulty == 5
    assert game_fixture.round_number == 1
    assert isinstance(game_fixture.round_runner, RoundRunner)
    assert isinstance(game_fixture.current_question, Question)


def test_handle_user_response(game_fixture, monkeypatch):
    monkeypatch.setattr(game_fixture.round_runner, 'set_user_input', lambda x: None)
    monkeypatch.setattr(game_fixture.round_runner, 'next_question', lambda: True)
    game_fixture.handle_user_response("user_answer")
    monkeypatch.setattr(game_fixture.round_runner, 'next_question', lambda: False)
    game_fixture.handle_user_response("user_answer")


def test_initiate_round(game_fixture, monkeypatch):
    monkeypatch.setattr(game_fixture, '_end_game', lambda: None)
    monkeypatch.setattr(game_fixture.round_runner, 'begin_round', lambda: True)
    monkeypatch.setattr(game_fixture, '_start_round', lambda: None)
    assert game_fixture.initiate_round()
    monkeypatch.setattr(game_fixture.round_runner, 'begin_round', lambda: False)
    assert not game_fixture.initiate_round()


def test_get_question_bundle(game_fixture, monkeypatch):
    monkeypatch.setattr(game_fixture.round_runner, 'get_question_bundle', lambda: ('question', 'choices', 'answer'))
    question_bundle = game_fixture.get_question_bundle()
    assert question_bundle == ('question', 'choices', 'answer')


def test_get_round_number(game_fixture):
    round_number = game_fixture.get_round_number()
    assert round_number == 1


def test_rounds_within_range(game_fixture):
    for _ in range(Game.ROUNDS_PER_GAME):
        assert game_fixture.rounds_within_range()
        game_fixture.round_number += 1
    assert not game_fixture.rounds_within_range()


def test_next_question(game_fixture, monkeypatch):
    monkeypatch.setattr(game_fixture.round_runner, 'next_question', lambda: None)
    assert game_fixture.next_question() is None


def test_end_of_round(game_fixture):
    old_round_number = game_fixture.round_number
    game_fixture.end_of_round()
    assert game_fixture.round_number == old_round_number + 1


def test_end_of_game(game_fixture):
    for _ in range(Game.ROUNDS_PER_GAME - 1):
        assert not game_fixture.end_of_game()
        game_fixture.round_number += 1
    assert game_fixture.end_of_game()


def test_check_answer(game_fixture, monkeypatch):
    monkeypatch.setattr(game_fixture.current_question, 'check_answer', lambda x: None)
    game_fixture.check_answer("user_answer")
