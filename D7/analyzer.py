class Analyzer:
    def analyze(self, marks_list):
        if not marks_list:
            raise ValueError("No student data available to analyze.")

        avg = sum(marks_list) / len(marks_list)
        high = max(marks_list)
        low = min(marks_list)

        return avg, high, low