import re
import unicodedata

def tonum(s):
    s = unicodedata.normalize('NFC', s.lower().strip())
    s = re.sub(r'\s+', ' ', s)
    words = s.split()
    if not words: return 0
    
    digits = {'không': 0, 'một': 1, 'hai': 2, 'ba': 3, 'bốn': 4, 'năm': 5, 'sáu': 6, 'bảy': 7, 'tám': 8, 'chín': 9, 'mốt': 1, 'tư': 4, 'lăm': 5}
    digits = {unicodedata.normalize('NFC', k): v for k, v in digits.items()}
    
    multipliers = {'tỷ': (10**9, 4), 'triệu': (10**6, 3), 'nghìn': (1000, 2), 'ngàn': (1000, 2), 'trăm': (100, 1), 'mươi': (10, 0), 'mười': (10, 0)}
    multipliers = {unicodedata.normalize('NFC', k): v for k, v in multipliers.items()}
    
    filtered_words = [w for w in words if w not in ['linh', 'lẻ']]
    if not filtered_words: return 0

    def parse(tokens):
        if not tokens: return 0
        if len(tokens) == 1:
            return digits.get(tokens[0], multipliers.get(tokens[0], [0])[0])
        
        max_rank, split_idx = -1, -1
        for i, word in enumerate(tokens):
            if word in multipliers:
                val, rank = multipliers[word]
                if rank >= max_rank:
                    max_rank, split_idx = rank, i
        
        if split_idx == -1: return digits.get(tokens[-1], 0)
        
        multiplier_val = multipliers[tokens[split_idx]][0]
        left = parse(tokens[:split_idx]) if tokens[:split_idx] else 1
        right = parse(tokens[split_idx+1:])
        
        return left * multiplier_val + right

    return parse(filtered_words)