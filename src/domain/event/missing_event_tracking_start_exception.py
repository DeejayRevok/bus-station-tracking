class MissingEventTrackingStartException(Exception):
    def __init__(self, event_tracking_id: str):
        self.event_tracking_id = event_tracking_id
        super().__init__(f"Missing event {event_tracking_id} tracking start")
