class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime powers of 2, 3, 5, 7
        temp = t
        t_a = t_b = t_c = t_d7 = 0
        
        while temp % 2 == 0:
            t_a += 1
            temp //= 2
        while temp % 3 == 0:
            t_b += 1
            temp //= 3
        while temp % 5 == 0:
            t_c += 1
            temp //= 5
        while temp % 7 == 0:
            t_d7 += 1
            temp //= 7
            
        # If t has any prime factor > 7, no zero-free number can satisfy it
        if temp > 1:
            return "-1"

        # Step 2: Precompute DP table for prime powers of 2 (max 50) and 3 (max 30)
        MAX_A, MAX_B = 50, 30
        dp = [[None] * (MAX_B + 1) for _ in range(MAX_A + 1)]
        dp[0][0] = (0, ())

        digits_info = [
            (2, 1, 0),
            (3, 0, 1),
            (4, 2, 0),
            (6, 1, 1),
            (8, 3, 0),
            (9, 0, 2),
        ]

        for s in range(1, MAX_A + MAX_B + 1):
            for a in range(min(s, MAX_A) + 1):
                b = s - a
                if b > MAX_B:
                    continue
                best = None
                for d, da, db in digits_info:
                    prev_a = max(0, a - da)
                    prev_b = max(0, b - db)
                    if prev_a == a and prev_b == b:
                        continue
                    prev_cnt, prev_tup = dp[prev_a][prev_b]
                    cand_cnt = prev_cnt + 1
                    cand_tup = tuple(sorted(prev_tup + (d,)))
                    cand = (cand_cnt, cand_tup)
                    if best is None or cand < best:
                        best = cand
                dp[a][b] = best

        # Helper arrays for prime factors contributed by digits 1..9
        digit_a = [0] * 10
        digit_b = [0] * 10
        digit_c = [0] * 10
        digit_d7 = [0] * 10
        for d in range(1, 10):
            v = d
            while v % 2 == 0: digit_a[d] += 1; v //= 2
            while v % 3 == 0: digit_b[d] += 1; v //= 3
            while v % 5 == 0: digit_c[d] += 1; v //= 5
            while v % 7 == 0: digit_d7[d] += 1; v //= 7

        N = len(num)
        first_zero = N
        for idx, char in enumerate(num):
            if char == '0':
                first_zero = idx
                break

        # Check if num itself is zero-free and valid
        if first_zero == N:
            cnt_a = sum(digit_a[int(c)] for c in num)
            cnt_b = sum(digit_b[int(c)] for c in num)
            cnt_c = sum(digit_c[int(c)] for c in num)
            cnt_d7 = sum(digit_d7[int(c)] for c in num)
            if cnt_a >= t_a and cnt_b >= t_b and cnt_c >= t_c and cnt_d7 >= t_d7:
                return num

        # Precompute prefix prime factor counts
        pref_a = [0] * (N + 1)
        pref_b = [0] * (N + 1)
        pref_c = [0] * (N + 1)
        pref_d7 = [0] * (N + 1)
        for i in range(first_zero):
            d = int(num[i])
            pref_a[i + 1] = pref_a[i] + digit_a[d]
            pref_b[i + 1] = pref_b[i] + digit_b[d]
            pref_c[i + 1] = pref_c[i] + digit_c[d]
            pref_d7[i + 1] = pref_d7[i] + digit_d7[d]

        # Step 3: Try matching prefix of length i from min(N - 1, first_zero) down to 0
        start_i = min(N - 1, first_zero)
        for i in range(start_i, -1, -1):
            cur_digit = int(num[i])
            for d in range(cur_digit + 1, 10):
                cur_a = pref_a[i] + digit_a[d]
                cur_b = pref_b[i] + digit_b[d]
                cur_c = pref_c[i] + digit_c[d]
                cur_d7 = pref_d7[i] + digit_d7[d]

                rem_a = max(0, t_a - cur_a)
                rem_b = max(0, t_b - cur_b)
                rem_c = max(0, t_c - cur_c)
                rem_d7 = max(0, t_d7 - cur_d7)

                need_cnt, need_tup = dp[rem_a][rem_b]
                min_digits = rem_c + rem_d7 + need_cnt

                rem_len = N - 1 - i
                if rem_len >= min_digits:
                    suffix_digits = [5] * rem_c + [7] * rem_d7 + list(need_tup)
                    suffix_digits.sort()
                    ones_count = rem_len - min_digits
                    suffix_str = '1' * ones_count + "".join(map(str, suffix_digits))
                    return num[:i] + str(d) + suffix_str

        # Step 4: If no solution of length N exists, construct solution of length L > N
        need_cnt, need_tup = dp[t_a][t_b]
        min_digits = t_c + t_d7 + need_cnt
        L = max(N + 1, min_digits)
        suffix_digits = [5] * t_c + [7] * t_d7 + list(need_tup)
        suffix_digits.sort()
        ones_count = L - min_digits
        return '1' * ones_count + "".join(map(str, suffix_digits))