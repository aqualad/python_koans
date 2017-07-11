#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        "Double quoted strings are instances of type basestring"
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, basestring))

    def test_single_quoted_strings_are_also_strings(self):
        "Single quoted strings are instances of type basestring"
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, basestring))

    def test_triple_quote_strings_are_also_strings(self):
        "Triple quote strings are instances of type basestring"
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, basestring))

    def test_triple_single_quotes_work_too(self):
        "Triple single quote strings are instances of type basestring"
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, basestring))

    def test_raw_strings_are_also_strings(self):
        "Raw strings are instnaces of type basestring"
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, basestring))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        "Double quotes can be used inside of single quotes"
        string = 'He said, "Go Away."'
        self.assertEqual(string, string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        "Single quotes can be used inside of double quotes"
        string = "Don't"
        self.assertEqual(string, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        """
        Double quotes can be used inside of double quoted strings by escaping
        Single quotes can be used inside of single quoted strings by escaping
        """
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        "Quoted strings can span multiple lines by using a backslash"
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        "Triple quoted strings can span multiple lines"
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        "Triple quoted strings can contain double quotes without escaping"
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        "Triple quoted strings can't end with double quotes unless they're escaped"
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        "The plus operator concatenates strings"
        string = "Hello, " + "world"
        self.assertEqual('Hello, world', string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        "Adjacent strings are automatically concatenated"
        string = "Hello" ", " "world"
        self.assertEqual('Hello, world', string)

    def test_plus_will_not_modify_original_strings(self):
        "The plus operator doesn't modify the original strings"
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        "The plus equals operator appends to the lhs"
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        "The plus equals operator doesn't modify the rhs"
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        """
        Single, double, and triple quoted strings interpret escape characters like newline
        """
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
