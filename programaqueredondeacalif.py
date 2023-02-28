    #programa de calificaciones que se redondea
    for i in range(0, len(grades)):
        if grades[i] > 37 and grades[i] % 5 != 0:
            diff_ = abs(5 - grades[i] % 5)
            if diff_ < 3:
                grades[i] = grades[i] + diff_
        else:
            pass
    return grades
        
        
