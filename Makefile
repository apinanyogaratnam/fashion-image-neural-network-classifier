IMAGE := fashion-image-neural-network-classifier

start:
	python3 main.py

build:
	docker build -t ${IMAGE} .

run:
	docker run ${IMAGE}
