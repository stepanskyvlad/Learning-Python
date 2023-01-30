# Bouncing Balls
# https://www.codewars.com/kata/5544c7a5cb454edb3c000047
def bouncing_ball(h, bounce, window):
    if any((h <= 0, bounce >= 1, bounce <= 0, window >= h)):
        result = -1
    else:
        result = 1
        current_h = h * bounce
        while current_h > window:
            current_h *= bounce
            result += 2

    return result


if __name__ == "__main__":
    print(bouncing_ball(3, 0.6, 1.5))
