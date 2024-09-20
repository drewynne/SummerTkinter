import os
import sys
from tkinter import ttk, BooleanVar, IntVar, StringVar
from unittest.mock import patch, MagicMock

import pytest

from UI_Components.StartWindow import StartWindow


def test_StartWindow_init():
    with patch('StartWindow.MyWindow.__init__') as mock_super:
        sw = StartWindow()
        mock_super.assert_called_once_with('Summer')
        assert isinstance(sw.outer_frame, ttk.Frame)
        assert isinstance(sw.start_button, ttk.Button)
        assert isinstance(sw.show_stats_var, BooleanVar)
        assert isinstance(sw.show_stats, ttk.Checkbutton)
        assert isinstance(sw.difficulty_selector_label, ttk.Label)
        assert isinstance(sw.difficulty_selector_inp, ttk.Spinbox)
        assert isinstance(sw.difficulty_selector_var, IntVar)
        assert isinstance(sw.round_number_label, ttk.Label)
        assert isinstance(sw.round_number_var, StringVar)
        assert isinstance(sw.stats_button, ttk.Button)


@patch.object(StartWindow, 'open_game_window')
def test_StartWindow_on_press_start(mock_open_game_window):
    sw = StartWindow()
    sw.on_press_start()
    mock_open_game_window.assert_called_once()


@patch.object(StartWindow, 'open_stats_window')
def test_StartWindow_on_press_open_stats(mock_open_stats_window):
    sw = StartWindow()
    sw.on_press_open_stats()
    mock_open_stats_window.assert_called_once()


@patch('StartWindow.GameWindow.display')
@patch('StartWindow.GameWindow')
def test_StartWindow_open_game_window(mock_GameWindow, mock_display):
    mock_GameWindow.return_value = MagicMock()
    sw = StartWindow()
    sw.open_game_window()
    mock_GameWindow.assert_called_with(sw.root, "Summer Game Window")
    assert mock_display.called


@patch('StartWindow.StatsWindow.display')
@patch('StartWindow.StatsWindow')
def test_StartWindow_open_stats_window(mock_StatsWindow, mock_display):
    mock_StatsWindow.return_value = MagicMock()
    sw = StartWindow()
    sw.open_stats_window()
    mock_StatsWindow.assert_called_with(sw.root, "Summer Stats Window")
    assert mock_display.called


def test_startwindow_on_end_game():
    with patch('StartWindow.MyWindow.destroy') as mock_destroy:
        sw = StartWindow()
        with pytest.raises(SystemExit):
            sw.on_end_game()
        mock_destroy.assert_called_once()
