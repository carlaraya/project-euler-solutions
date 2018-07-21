tot = 1012314
i = 3241101
tot_copy, i_copy, tot_l , i_l = tot, i, [], []

is_perm = True
while tot_copy:
    tot_l.append(tot_copy % 10)
    tot_copy -= tot_l[-1]
    tot_copy //= 10
while i_copy:
    i_d = i_copy % 10
    if i_d in tot_l:
        tot_l.remove(i_d)
    else:
        is_perm = False
        break
    i_copy -= i_d
    i_copy //= 10
print(is_perm)
