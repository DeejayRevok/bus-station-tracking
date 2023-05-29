build_chart:
	docker-compose run bus-station-tracking poetry version -s | xargs -I {} helm package -u --version {} --app-version {} helm/bus-station-tracking

run_ui:
	python app/streamlit_runner.py

run_command_tracking_consumer:
	python app/kafka_consumer_runner.py -pt command_tracking

run_event_tracking_consumer:
	python app/kafka_consumer_runner.py -pt event_tracking

run_query_tracking_consumer:
	python app/kafka_consumer_runner.py -pt query_tracking
