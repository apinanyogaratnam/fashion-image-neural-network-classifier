IMAGE := fashion-image-neural-network-classifier

run:
	python3 main.py

build:
	docker build -t ${IMAGE} .
