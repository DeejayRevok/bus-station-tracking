class MissingCommandTrackingStartException(Exception):
    def __init__(self, command_tracking_id: str):
        self.command_tracking_id = command_tracking_id
        super().__init__(f"Missing command {command_tracking_id} tracking start")
