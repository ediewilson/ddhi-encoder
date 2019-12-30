# -*- coding: utf-8 -*-
# utterance.py

class Utterance:
    def __init__(self, speaker, speech):
        self.speaker = speaker
        self.speech = speech

    def __len__(self):
        return len(self.speech)
