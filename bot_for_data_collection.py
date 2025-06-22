from command import Command
from buttons import Buttons
import numpy as np
import joblib

class Bot:
    def __init__(self):
        self.my_command = Command()
        self.buttn = Buttons()

        # Load trained model and label encoder
        self.model = joblib.load("model.pkl")
        self.label_encoder = joblib.load("label_encoder.pkl")

        # Store current combo
        self.remaining_code = []

        # Action-to-command mapping
        self.action_map = {
            "walk_left": ["<", "!<"],
            "walk_right": [">", "!>"],
            "crouch_special": ["v+R", "v+R", "!v+!R"],
            "far_combo_1": [">+^+Y", ">+^+Y", "!>+!^+!Y"],
            "far_combo_2": ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"],
            "far_uppercut": [">+^+B", ">+^+B", "!>+!^+!B"],
            "close_combo_1": ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"],
            "close_combo_2": [">", "!>", "v+>", "!v+!>", "v", "!v", "v+<", "!v+!<", "<+Y", "!<+!Y"],
            "close_uppercut": ["<+^+B", "<+^+B", "!<+!^+!B"]
        }

    def fight(self, current_game_state, player):
        p = current_game_state.player1 if player == "1" else current_game_state.player2
        o = current_game_state.player2 if player == "1" else current_game_state.player1

        # If commands are left, execute next
        if self.remaining_code:
            self.execute_step(p)
        else:
            # Generate features and predict action
            features = [[
                p.health, p.x_coord, p.y_coord,
                int(p.is_jumping), int(p.is_crouching), p.move_id,
                o.health, o.x_coord, o.y_coord
            ]]

            pred_class = self.model.predict(features)[0]
            pred_label = self.label_encoder.inverse_transform([pred_class])[0]

            print(f"[🤖 Prediction] {pred_label}")

            commands = self.action_map.get(pred_label)
            if commands:
                self.remaining_code = commands.copy()
                self.execute_step(p)
            else:
                print(f"[⚠️ WARNING] '{pred_label}' not in action_map. Performing fallback.")
                self.remaining_code = [">", "!>"]
                self.execute_step(p)

        if player == "1":
            self.my_command.player_buttons = self.buttn
        else:
            self.my_command.player2_buttons = self.buttn

        return self.my_command

    def execute_step(self, player):
        if not self.remaining_code:
            return

        code = self.remaining_code.pop(0)

        if code == "v+<": self.buttn.down, self.buttn.left = True, True
        elif code == "!v+!<": self.buttn.down, self.buttn.left = False, False
        elif code == "v+>": self.buttn.down, self.buttn.right = True, True
        elif code == "!v+!>": self.buttn.down, self.buttn.right = False, False
        elif code == ">+Y": self.buttn.right, self.buttn.Y = True, True
        elif code == "!>+!Y": self.buttn.right, self.buttn.Y = False, False
        elif code == "<+Y": self.buttn.left, self.buttn.Y = True, True
        elif code == "!<+!Y": self.buttn.left, self.buttn.Y = False, False
        elif code == "<+^+B": self.buttn.left, self.buttn.up, self.buttn.B = True, True, True
        elif code == "!<+!^+!B": self.buttn.left, self.buttn.up, self.buttn.B = False, False, False
        elif code == ">+^+B": self.buttn.right, self.buttn.up, self.buttn.B = True, True, True
        elif code == "!>+!^+!B": self.buttn.right, self.buttn.up, self.buttn.B = False, False, False
        elif code == "v+R": self.buttn.down, self.buttn.R = True, True
        elif code == "!v+!R": self.buttn.down, self.buttn.R = False, False
        elif code == "<": self.buttn.left = True
        elif code == "!<": self.buttn.left = False
        elif code == ">": self.buttn.right = True
        elif code == "!>": self.buttn.right = False
        elif code == "v": self.buttn.down = True
        elif code == "!v": self.buttn.down = False
