from employee import calculate_bonus

def test_bonus_high():
    assert calculate_bonus(26) == 5000

def test_bonus_medium():
    assert calculate_bonus(22) == 3000

def test_bonus_low():
    assert calculate_bonus(16) == 1500

def test_bonus_none():
    assert calculate_bonus(10) == 0
