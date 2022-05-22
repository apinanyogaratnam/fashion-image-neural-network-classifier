IMAGE := fashion-image-neural-network-classifier
VERSION := 0.0.1
REGISTRY_URL := ghcr.io/apinanyogaratnam/${IMAGE}:${VERSION}

start:
	python3 main.py

build:
	docker build -t ${IMAGE} .

run:
	docker run -p 8080:8080 ${IMAGE}

auth:
	grep -v '^#' .env.local | grep -e "CR_PAT" | sed -e 's/.*=//' | docker login ghcr.io -u USERNAME --password-stdin

tag:
	docker tag ${IMAGE} ${REGISTRY_URL}
	git tag -m "v${VERSION}" v${VERSION}

push:
	docker push ${REGISTRY_URL}
	git push --tags

all:
	make build && make auth && make tag && make push
