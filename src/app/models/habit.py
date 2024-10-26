class Habit:
    def __init__(self, name, description, weekly_time_commitment, goal_length, success_measurement):
        self.name = name
        self.description = description
        self.weekly_time_commitment = weekly_time_commitment
        self.goal_length = goal_length
        self.success_measurement = success_measurement

    def to_dict(self):
        return {
            'description': self.description,
            'weekly_time_commitment': self.weekly_time_commitment,
            'goal_length': self.goal_length,
            'success_measurement': self.success_measurement,
        }
