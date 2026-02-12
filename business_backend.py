class BusinessBackend:
    """
    This class represents the backend business logic for the report system.
    """

    def __init__(self):
        self.data = []

    def add_data(self, item):
        """
        Add an item to the data list.
        """
        self.data.append(item)

    def generate_report(self):
        """
        Generate a report based on the current data.
        """
        return f'Report with {len(self.data)} items'

    def clear_data(self):
        """
        Clear all data in the system.
        """
        self.data.clear()