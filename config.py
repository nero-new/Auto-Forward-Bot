import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split(",")))

STICKER_IDS = [
    "CAADAQADtQIAAqVCUEemuIH_uo6q8wI",
    "CAADAQAD3wADkTtARaGVp5D7hcquAg",
    "BAADBAADiA4AAmxNyVMbG4nB2XuyOwI",
    "BAADBQADahIAAl_qGVSFHlibUahniwI",
    "CAADBQADlgIAAhftWVRLxW71S_lzawI",
    "CAADBQADFwMAAsPPiFRxPNswxRcy0QI",
    "CAADBQADvRQAAv3tKFQdR1aYHasU-gI",
    "BAADAgAD6SoAAnow6Erq4zZboprW4AI",
    "BAADAgADUFUAAqC_EEgpJF6y3q-n7QI",
    "BAADBAADQRAAAiypQFCTfE64pcQeZAI",
    "BAADBQADug8AAk0UMFdiZnbhfRZX6gI"
]
