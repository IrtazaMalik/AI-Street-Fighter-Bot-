# AI-Street-Fighter-Bot-
AI vs. Street Fighter! 🤖🔥 Excited to share my latest AI project—a bot trained to play Street Fighter using a Multi-Layer Perceptron (MLP) Classifier!

# Game Bot - Street Fighter II Turbo (AI Project - Spring 2025)

This project replaces the rule-based logic of a Street Fighter II Turbo bot with a machine learning model trained on real gameplay data to make intelligent move predictions in real time.

---

## Folder Structure

```
├── bot.py                    # Main bot logic (ML-based)
├── bot_for_data_collection.py # Used for gameplay data collection
├── buttons.py
├── command.py
├── controller.py             # Handles socket communication and game loop
├── game_state.py
├── player.py
├── model.pkl                 # Trained Random Forest model (with SMOTEENN)
├── label_encoder.pkl         # Label encoder for mapping actions to numbers
├── game_data.csv             # Collected gameplay dataset
├── model_training.ipynb      # Notebook with model training and evaluation
├── README.md
```

---

## Requirements

- **OS**: Windows 7 or above (64-bit)
- **Python**: 3.6 or higher
- **Emulator**: [BizHawk Emulator](https://github.com/TASVideos/BizHawk)

### Python Libraries

Install all required libraries:

```bash
pip install pandas numpy scikit-learn imbalanced-learn xgboost joblib
```

---

## Emulator Setup (BizHawk)

1. **Download emulator and Python API**:  
   [Google Drive Link](https://drive.google.com/file/d/18SN8e_XqJFEPZ0wcWXQ8GnzuZk58cn-2/view)

2. **Launch Game**:
   - Open `EmuHawk.exe`
   - Go to **File → Open ROM**
   - Load `Street Fighter II Turbo (U).smc`
   - Go to **Tools → Tool Box** (Shortcut: `Shift + T`)
   - Keep the emulator and toolbox open

---

## How to Train Your Own Bot

### Step-by-Step Guide

1. **Start the Game:**

   - Follow the emulator setup instructions above.

2. **Enable Data Collection Mode:**

   - Copy all code from `bot_for_data_collection.py` and paste it into `bot.py`.

3. **Collect Gameplay Data:**

   - Run the bot for each character one by one using:
     ```bash
     python controller.py 1
     ```
   - A `game_data.csv` file will be generated after collecting actions.

4. **Train the ML Model:**

   - Open `model_training.ipynb` and run all cells.
   - This script will:
     - Apply **SMOTEENN** for class balancing
     - Train multiple models and select the best one (Random Forest)
     - Save the following:
       - `model.pkl`: the trained model
       - `label_encoder.pkl`: maps between action labels and encoded integers

5. **Deploy Your Bot:**
   - Replace the data collection code in `bot.py` with the **original ML prediction code**.
   - Now your bot is ready to play intelligently!

---

## How to Run Your Trained Bot

### Single Player Mode (Bot vs CPU)

```bash
python controller.py 1
```

This controls **Player 1** using the trained ML model.

---

### Two Player Mode (Bot vs Bot)

To run **two bots fighting each other**, follow these steps:

1. **Open two terminal windows** side-by-side.

2. Run the following commands separately:

```bash
# Terminal 1 (Player 1 - Left side)
python controller.py 1

# Terminal 2 (Player 2 - Right side)
python controller.py 2
```

3. In the BizHawk emulator:

   - Select **VS Battle Mode**
   - Pick characters for both players

4. **Enable Bot Connection**:

   - Click the **Gyroscope Bot icon** in the toolbar (2nd icon on the top)
   - Each terminal should display:
     ```
     Connected to game!
     ```

5. The game will now begin with both players controlled by your AI bots.  
   Once one round is over, the program will stop — repeat to play again.

---

## Model Overview

- Evaluated: Random Forest, XGBoost, MLP, Logistic Regression
- Best performer: **Random Forest + SMOTEENN**
- Achieved: ~97.9% accuracy
- Balanced using: SMOTE, ADASYN, and SMOTEENN

---

# By Irtaza Jawad

