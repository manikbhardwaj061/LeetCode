class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        
        # Segment Tree Arrays (1-based indexing)
        tree_max = [0] * (4 * n)
        tree_pref_char = [''] * (4 * n)
        tree_pref_len = [0] * (4 * n)
        tree_suff_char = [''] * (4 * n)
        tree_suff_len = [0] * (4 * n)

        def push_up(node: int, size_L: int, size_R: int):
            L = node * 2
            R = node * 2 + 1

            l_max, r_max = tree_max[L], tree_max[R]
            l_sc, r_pc = tree_suff_char[L], tree_pref_char[R]
            l_sl, r_pl = tree_suff_len[L], tree_pref_len[R]

            # 1. Update max_len
            mx = max(l_max, r_max)
            if l_sc == r_pc:
                mx = max(mx, l_sl + r_pl)
            tree_max[node] = mx

            # 2. Update prefix
            l_pc, l_pl = tree_pref_char[L], tree_pref_len[L]
            tree_pref_char[node] = l_pc
            if l_pl == size_L and l_pc == r_pc:
                tree_pref_len[node] = size_L + r_pl
            else:
                tree_pref_len[node] = l_pl

            # 3. Update suffix
            r_sc, r_sl = tree_suff_char[R], tree_suff_len[R]
            tree_suff_char[node] = r_sc
            if r_sl == size_R and r_sc == l_sc:
                tree_suff_len[node] = size_R + l_sl
            else:
                tree_suff_len[node] = r_sl

        def build(node: int, l: int, r: int):
            if l == r:
                c = s[l]
                tree_max[node] = 1
                tree_pref_char[node] = c
                tree_pref_len[node] = 1
                tree_suff_char[node] = c
                tree_suff_len[node] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            push_up(node, mid - l + 1, r - mid)

        def update(node: int, l: int, r: int, idx: int, char: str):
            if l == r:
                tree_pref_char[node] = char
                tree_suff_char[node] = char
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)
            push_up(node, mid - l + 1, r - mid)

        # Build initial segment tree
        build(1, 0, n - 1)

        # Process queries
        ans = []
        for idx, c in zip(queryIndices, queryCharacters):
            update(1, 0, n - 1, idx, c)
            ans.append(tree_max[1])

        return ans