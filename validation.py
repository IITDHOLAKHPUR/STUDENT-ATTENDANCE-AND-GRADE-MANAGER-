def valid_marks(marks):
    if marks>=0 and marks<=100:
        return True
    else:
        return False
def valid_attendance(attended,total):
        if attended>=0 and total>0 and attended<=total:
            return True
        else:
             return False
