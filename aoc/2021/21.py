"""
I guess there is a dp bottom up solution

"""
from functools import lru_cache


def part_1(player_pos):
    player_score = [0, 0]

    turn = 0
    dice = 1
    while all((score < 1000 for score in player_score)):
        turn += 1
        player_idx = (turn + 1) % 2
        roll = (3 * (dice + 1)) % 10

        player_pos[player_idx] += roll
        if player_pos[player_idx] > 10:
            player_pos[player_idx] -= 10
        player_score[player_idx] += player_pos[player_idx]

        dice += 3

        print(f"Player {player_idx+1}", player_score[player_idx])

    losing_score = min(player_score)
    return losing_score * turn * 3


ROLLS = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
# 5: 1 1 3, 1 2 2
# 6: 1 2 3, 2 2 2
# 7: 1 3 3, 2 2 3
# 8: 2 3 3


@lru_cache(None)
def part_2(turn, p1_pos, p2_pos, p1_score, p2_score):
    if p1_score >= 21:
        return (1, 0)
    elif p2_score >= 21:
        return (0, 1)

    win_chances = [0, 0]

    for value, chances in ROLLS:

        # Need to set the scores and positions back to original for each possibility
        scores = [p1_score, p2_score]
        positions = [p1_pos, p2_pos]

        positions[turn] += value % 10
        if positions[turn] > 10:
            positions[turn] -= 10
        scores[turn] += positions[turn]

        # In the next turn, each player wins in `next_state_win_chances` universes
        next_state_win_chances = part_2(1 - turn, *positions, *scores)

        # There are `chances` ways both players ending up in the next state
        win_chances[0] += chances * next_state_win_chances[0]
        win_chances[1] += chances * next_state_win_chances[1]

    return tuple(win_chances)


if __name__ == "__main__":
    print(part_1([1, 6]))
    print(max(part_2(0, 1, 6, 0, 0)))
