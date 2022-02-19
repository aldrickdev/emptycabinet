:PHONY requp
requp:
	@echo Updating requirements.txt
	@poetry export -o requirements.txt
	@echo Updating requirements_dev.txt
	@poetry export --dev -o requirements_dev.txt
	@echo Requirement Files Update Complete!!

:PHONY run
run:
	@uvicorn emptycabinet.main:app

:PHONY rerun
rerun:
	@uvicorn emptycabinet.main:app --reload
