IMAGE := fashion-image-neural-network-classifier

start:
	python3 main.py

build:
	docker build -t ${IMAGE} .

run:
	docker run ${IMAGE}

view-plots:
	docker exec -it $(sha) /bin/bash
