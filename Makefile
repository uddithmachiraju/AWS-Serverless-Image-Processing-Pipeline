.PHONY: all clean build zip deploy api 

LAMBDA_ZIP=lambda_func.zip 
SRC_ZIP=app/lambda_func
BUILD_DIR=build/lambda 
HANDLER=handler.py
APP_DIR=app

# Clean the previous build 
clean:
	rm -rf $(BUILD_DIR) $(LAMBDA_ZIP) 

build:
	mkdir -p $(BUILD_DIR)
	pip install pillow -t $(BUILD_DIR) 
	cp $(SRC_ZIP)/$(HANDLER) $(BUILD_DIR) 
	cp -r $(APP_DIR)/ $(BUILD_DIR) 

# Zip the entire build dir 
zip:
	cd $(BUILD_DIR) && zip -r ../../$(LAMBDA_ZIP) . 

deploy:
	poetry run python -m deploy.main

api:
	poetry run uvicorn main:app --reload