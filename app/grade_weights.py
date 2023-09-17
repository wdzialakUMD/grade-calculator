

class GradeWeights:
    """
    Specifies the weights assigned to each grade
    category for ENPM611. The weights can be found
    in the introductory slides and in the syllabus.
    """
    
    def __init__(self) -> None:
        self.quizzes = 0.1
        self.midterm = 0.2
        self.project = 0.4
        self.final = 0.3