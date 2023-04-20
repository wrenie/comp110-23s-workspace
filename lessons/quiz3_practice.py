class Course:
    """Models UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, req: str) -> bool:
        if self.level < 400:
            return False
        else:
            for courses in self.prerequisites:
                if courses == req:
                    return True
            return False
        

