def wow(qpos, kpos):
    qrow, qcol = qpos
    krow, kcol = kpos

    if qrow == krow or qcol == kcol or abs(qrow - krow) == abs(qcol - kcol):
        return True
    return False


def lalala():
    global qpos, kpos
    print("Enter the positions")

    queeninput = input("Enter the queen's position: ")

    qpos = (8 - int(queeninput[1]), ord(queeninput[0]) - ord('a'))

    kinginput = input("Enter the king's position: ")

    kpos = (8 - int(kinginput[1]), ord(kinginput[0]) - ord('a'))

lalala()
if wow(qpos, kpos):
    print("queen attacks king")
else:
    print("queen doesnt attack")
