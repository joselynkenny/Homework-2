def find_profitable_path(current_token, visited, path, balance, liquidity,b_token):
    # print(f"Current token: {current_token}, Balance: {balance}, Path: {'->'.join(path)}")
    if balance > 20:
        print(f"path: {'->'.join(path)}, tokenB balance={balance}.")
        return
    new_balance =0
    for next_token in liquidity:
        # print("+++++++++++++++++",new_balance)
        if (current_token == next_token[0] or current_token == next_token[1]):
            if not(b_token == next_token[0] or b_token == next_token[1]):
                # print("testt",balance)
                liquidity_pair = liquidity[next_token]
                if(current_token == next_token[0]):
                    output = balance * 0.997
                    newx =output+liquidity_pair[0]
                    newy = (liquidity_pair[0] * liquidity_pair[1])/newx # Arbitrage calculation
                    output = liquidity_pair[1] - newy
                    # print(output)
                if(current_token == next_token[1]):
                    # print("aaa")
                    output = balance * 0.997
                    newx =output+liquidity_pair[1]
                    newy = (liquidity_pair[1] * liquidity_pair[0])/newx # Arbitrage calculation
                    output =liquidity_pair[0] - newy
                    # print(output)
                
                if new_balance < output:
                    new_balance =output
                    future_token = next_token
                    # print("+++++++++++++++++",new_balance,next_token)

    # print("next_token token: {future_token}, newwwwwwwBalance: {balance}, Path: {'->'.join(path)}")
    if(current_token == future_token[0]):
        new_path = path + [future_token[1]]
        new_visited = visited.copy()
        new_visited.add(future_token[1])

        find_profitable_path(future_token[1], new_visited, new_path, new_balance, liquidity,b_token=current_token)
    else:
        new_path = path + [future_token[0]]
        new_visited = visited.copy()
        new_visited.add(future_token[0])
        find_profitable_path(future_token[0], new_visited, new_path, new_balance, liquidity,b_token=current_token)
        

def main(starting_token, initial_balance, liquidity):
    visited = set()
    visited.add(starting_token)
    # print("start")
    find_profitable_path(starting_token, visited, [starting_token], initial_balance, liquidity,b_token='')

if __name__ == "__main__":
    # Liquidity data
    liquidity = {
        ("tokenA", "tokenB"): (17, 10),
        ("tokenA", "tokenC"): (11, 7),
        ("tokenA", "tokenD"): (15, 9),
        ("tokenA", "tokenE"): (21, 5),
        ("tokenB", "tokenC"): (36, 4),
        ("tokenB", "tokenD"): (13, 6),
        ("tokenB", "tokenE"): (25, 3),
        ("tokenC", "tokenD"): (30, 12),
        ("tokenC", "tokenE"): (10, 8),
        ("tokenD", "tokenE"): (60, 25),
    }

    main('tokenB', 5, liquidity)