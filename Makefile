IMAGE := fashion-image-neural-network-classifier

start:
	python3 main.py

build:
	docker build -t ${IMAGE} .

run:
	docker run -p 8080:8080 ${IMAGE}
