class MissingQueryTrackingStartException(Exception):
    def __init__(self, query_tracking_id: str):
        self.query_tracking_id = query_tracking_id
        super().__init__(f"Missing query {query_tracking_id} tracking start")
