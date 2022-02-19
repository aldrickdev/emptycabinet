:PHONY update-req
update-req:
	@echo Updating requirements.txt
	@poetry export -o requirements.txt
	@echo Updating requirements_dev.txt
	@poetry export --dev -o requirements_dev.txt
	@echo Requirement Files Update Complete!!


