Card = input().lower()
rank = Card[:-1]
suit = Card[-1]
ranks = {
    "a": "ace", "j": "jack", "q": "queen", "k": "king",
    "2": "2", "3": "3", "4": "4", "5": "5", 
    "6": "6", "7": "7", "8": "8", "9": "9", "10": "10"
}
suits = {
    "d": "diamonds",
    "h": "hearts",
    "s": "spades",
    "c": "clubs"
}
print(f"{ranks[rank]} of {suits[suit]}")